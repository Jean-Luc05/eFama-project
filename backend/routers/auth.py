from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr
from supabase import create_client, Client
import os
from dotenv import load_dotenv
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

# --- Pydantic Models ---
class UserCreate(BaseModel):
    email: EmailStr
    phone_number: str
    password: str

class UserLogin(BaseModel):
    identifier: str  # Can be email or phone
    password: str

class UserResponse(BaseModel):
    message: str
    user_id: str = None
    
class LoginResponse(BaseModel):
    message: str
    access_token: str = None
    user: dict = None

# --- Supabase Client Initialization ---
try:
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    
    if not url or not key:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in environment variables")
    
    supabase: Client = create_client(url, key)
    logger.info("Supabase client initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize Supabase client: {e}")
    raise

# --- API Router Setup ---
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)

# --- Registration Endpoint ---
@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def register_user(user_data: UserCreate):
    """
    Register a new user with email and phone number
    """
    try:
        logger.info(f"Attempting to register user with email: {user_data.email}")
        
        # Sign up user with Supabase Auth
        response = supabase.auth.sign_up({
            "email": user_data.email,
            "password": user_data.password,
            "options": {
                "data": {
                    "phone_number": user_data.phone_number
                }
            }
        })
        
        if response.user:
            logger.info(f"User registered successfully: {response.user.id}")
            return UserResponse(
                message="User registered successfully. Please check your email to verify.",
                user_id=response.user.id
            )
        else:
            logger.error("Registration failed - no user returned")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Registration failed. Please try again."
            )
            
    except Exception as e:
        logger.error(f"Registration error: {str(e)}")
        # Handle specific Supabase errors
        error_message = str(e)
        if "already registered" in error_message.lower():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with this email already exists"
            )
        elif "password" in error_message.lower():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password does not meet requirements"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Registration failed: {error_message}"
            )

# --- Login Endpoint ---
@router.post("/login", response_model=LoginResponse)
async def login_user(user_data: UserLogin):
    """
    Login user with email/phone and password
    """
    try:
        logger.info(f"Attempting to login user with identifier: {user_data.identifier}")
        
        # Determine if identifier is email or phone
        if '@' in user_data.identifier:
            # Email login
            response = supabase.auth.sign_in_with_password({
                "email": user_data.identifier,
                "password": user_data.password
            })
        else:
            # Phone login
            response = supabase.auth.sign_in_with_password({
                "phone": user_data.identifier,
                "password": user_data.password
            })
        
        if response.session and response.user:
            logger.info(f"User logged in successfully: {response.user.id}")
            return LoginResponse(
                message="Login successful!",
                access_token=response.session.access_token,
                user={
                    "id": response.user.id,
                    "email": response.user.email,
                    "phone": response.user.phone
                }
            )
        else:
            logger.error("Login failed - no session or user returned")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )
            
    except Exception as e:
        logger.error(f"Login error: {str(e)}")
        error_message = str(e)
        if "invalid" in error_message.lower() or "credentials" in error_message.lower():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email/phone or password"
            )
        elif "confirmed" in error_message.lower():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Please verify your email before logging in"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Login failed: {error_message}"
            )

# --- Additional Auth Endpoints ---
@router.post("/logout")
async def logout_user():
    """
    Logout current user
    """
    try:
        supabase.auth.sign_out()
        return {"message": "Logged out successfully"}
    except Exception as e:
        logger.error(f"Logout error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Logout failed: {str(e)}"
        )

@router.get("/me")
async def get_current_user():
    """
    Get current user information
    """
    try:
        user = supabase.auth.get_user()
        if user:
            return {"user": user.user}
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authenticated"
            )
    except Exception as e:
        logger.error(f"Get user error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required"
        )