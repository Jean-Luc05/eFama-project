<template>
<body class="bg-white min-h-screen flex items-center justify-center p-4">
    <div class="w-full max-w-4xl">
        <div class="bg-white rounded-2xl shadow-xl border border-gray-100 overflow-hidden">
            <!-- Header -->
            <div class="bg-gradient-to-r from-green-50 to-green-100 px-8 py-6 text-center">
                <h1 class="text-3xl font-bold text-black mb-2">Create Your Account</h1>
                <p class="text-gray-600">Join us today and get started with your business</p>
            </div>

            <div class="p-8">
                <!-- Google Sign Up Button -->
                <button class="w-full flex items-center justify-center gap-3 bg-white border-2 border-gray-200 rounded-lg px-6 py-3 text-gray-700 font-medium hover:border-gray-300 hover:shadow-md transition-all duration-200 mb-6">
                    <svg class="w-5 h-5" viewBox="0 0 24 24">
                        <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                        <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                        <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
                        <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
                    </svg>
                    Sign up with Google
                </button>

                <!-- Divider -->
                <div class="relative mb-6">
                    <div class="absolute inset-0 flex items-center">
                        <div class="w-full border-t border-gray-200"></div>
                    </div>
                    <div class="relative flex justify-center text-sm">
                        <span class="px-4 bg-white text-gray-500">Or sign up with email</span>
                    </div>
                </div>

                <!-- Form -->
                <form class="space-y-6">
                    <!-- Two Column Grid for Large Screens -->
                    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                        <!-- Left Column -->
                        <div class="space-y-6">
                            <!-- Email -->
                            <div>
                                <label for="email" class="block text-sm font-medium text-black mb-2">Email Address</label>
                                <input 
                                    type="email" 
                                    id="email" 
                                    name="email" 
                                    required 
                                    class="w-full px-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors duration-200 text-black placeholder-gray-400"
                                    placeholder="Enter your email"
                                >
                            </div>

                            <!-- Phone Number -->
                            <div>
                                <label for="phone" class="block text-sm font-medium text-black mb-2">Phone Number</label>
                                <input 
                                    type="tel" 
                                    id="phone" 
                                    name="phone" 
                                    required 
                                    class="w-full px-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors duration-200 text-black placeholder-gray-400"
                                    placeholder="(555) 123-4567"
                                >
                            </div>

                            <!-- Business Name -->
                            <div>
                                <label for="business" class="block text-sm font-medium text-black mb-2">Business Name</label>
                                <input 
                                    type="text" 
                                    id="business" 
                                    name="business" 
                                    required 
                                    class="w-full px-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors duration-200 text-black placeholder-gray-400"
                                    placeholder="Enter your business name"
                                >
                            </div>
                        </div>

                        <!-- Right Column -->
                        <div class="space-y-6">
                            <!-- Province -->
                            <div>
                                <label for="province" class="block text-sm font-medium text-black mb-2">Province</label>
                                <select 
                                    id="province" 
                                    name="province" 
                                    required 
                                    class="w-full px-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors duration-200 text-black"
                                >
                                    <option value="">Select your province</option>
                                    <option value="AB">Alberta</option>
                                    <option value="BC">British Columbia</option>
                                    <option value="MB">Manitoba</option>
                                    <option value="NB">New Brunswick</option>
                                    <option value="NL">Newfoundland and Labrador</option>
                                    <option value="NS">Nova Scotia</option>
                                    <option value="ON">Ontario</option>
                                    <option value="PE">Prince Edward Island</option>
                                    <option value="QC">Quebec</option>
                                    <option value="SK">Saskatchewan</option>
                                    <option value="NT">Northwest Territories</option>
                                    <option value="NU">Nunavut</option>
                                    <option value="YT">Yukon</option>
                                </select>
                            </div>

                            <!-- Password -->
                            <div>
                                <label for="password" class="block text-sm font-medium text-black mb-2">Password</label>
                                <input 
                                    type="password" 
                                    id="password" 
                                    name="password" 
                                    required 
                                    minlength="8"
                                    class="w-full px-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors duration-200 text-black placeholder-gray-400"
                                    placeholder="Create a strong password"
                                >
                            </div>

                            <!-- Confirm Password -->
                            <div>
                                <label for="confirm-password" class="block text-sm font-medium text-black mb-2">Confirm Password</label>
                                <input 
                                    type="password" 
                                    id="confirm-password" 
                                    name="confirm-password" 
                                    required 
                                    minlength="8"
                                    class="w-full px-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors duration-200 text-black placeholder-gray-400"
                                    placeholder="Confirm your password"
                                >
                            </div>
                        </div>
                    </div>

                    <!-- Terms and Conditions -->
                    <div class="flex items-start gap-3">
                        <input 
                            type="checkbox" 
                            id="terms" 
                            name="terms" 
                            required 
                            class="mt-1 w-4 h-4 text-green-600 border-gray-300 rounded focus:ring-green-500"
                        >
                        <label for="terms" class="text-sm text-gray-600">
                            I agree to the <a href="#" class="text-green-600 hover:text-green-700 font-medium">Terms of Service</a> and <a href="#" class="text-green-600 hover:text-green-700 font-medium">Privacy Policy</a>
                        </label>
                    </div>

                    <!-- Submit Button -->
                    <button 
                        type="submit" 
                        class="w-full bg-green-600 text-white py-3 px-6 rounded-lg font-medium hover:bg-green-700 focus:ring-4 focus:ring-green-200 transition-all duration-200 shadow-lg hover:shadow-xl"
                    >
                        Create Account
                    </button>

                    <!-- Sign In Link -->
                    <div class="text-center">
                        <p class="text-gray-600">
                            Already have an account? 
                            <a href="signin.html" class="text-green-600 hover:text-green-700 font-medium">Sign in here</a>
                        </p>
                    </div>
                </form>
            </div>
        </div>
    </div>
</body>
</template>
