<!-- pages/signin.vue -->
<template>
  <div class="bg-white min-h-screen flex items-center justify-center p-4">
    <div class="w-full max-w-md">
      <div class="bg-white shadow-2xl rounded-2xl p-8 border border-gray-100">
        <!-- Header -->
        <div class="text-center mb-8">
          <h1 class="text-3xl font-bold text-black mb-2">Welcome Back</h1>
          <p class="text-gray-600">Sign in to your account</p>
        </div>

        <!-- Form -->
        <form @submit.prevent="handleSubmit" class="space-y-6">
          <!-- Email -->
          <div>
            <label for="email" class="block text-sm font-medium text-black mb-2">
              Email Address
            </label>
            <input 
              type="email" 
              id="email" 
              name="email" 
              v-model="form.email"
              required
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors text-black placeholder-gray-400"
              placeholder="Enter your email"
            >
          </div>

          <!-- Password -->
          <div>
            <label for="password" class="block text-sm font-medium text-black mb-2">
              Password
            </label>
            <input 
              type="password" 
              id="password" 
              name="password" 
              v-model="form.password"
              required
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors text-black placeholder-gray-400"
              placeholder="Enter your password"
            >
          </div>

          <!-- Remember Me & Forgot Password -->
          <div class="flex items-center justify-between">
            <div class="flex items-center">
              <input 
                type="checkbox" 
                id="remember" 
                name="remember"
                v-model="form.remember"
                class="h-4 w-4 text-green-600 focus:ring-blue-500 border-gray-300 rounded"
              >
              <label for="remember" class="ml-2 block text-sm text-black">
                Remember me
              </label>
            </div>
            <NuxtLink to="/forgot-password" class="text-sm text-green-600 hover:text-blue-700 transition-colors">
              Forgot password?
            </NuxtLink>
          </div>

          <!-- Submit Button -->
          <button 
            type="submit"
            class="w-full bg-green-600 hover:bg-green-700 text-white font-semibold py-3 px-4 rounded-lg transition-colors duration-200 focus:ring-2 focus:ring-green-500 focus:ring-offset-2"
          >
            Sign In
          </button>
        </form>

        <!-- Divider -->
        <div class="mt-8 mb-6">
          <div class="relative">
            <div class="absolute inset-0 flex items-center">
              <div class="w-full border-t border-gray-300"></div>
            </div>
            <div class="relative flex justify-center text-sm">
              <span class="px-2 bg-white text-gray-500">Or continue with</span>
            </div>
          </div>
        </div>

        <!-- Social Login Buttons -->
        <div class="space-y-3">
          <button 
            type="button"
            @click="signInWithGoogle"
            class="w-full flex items-center justify-center px-4 py-3 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
          >
            <svg class="w-5 h-5 mr-3" viewBox="0 0 24 24">
              <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
              <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
              <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
              <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
            </svg>
            <span class="text-black font-medium">Continue with Google</span>
          </button>
        </div>

        <!-- Footer -->
        <div class="mt-8 text-center">
          <p class="text-gray-600">
            Don't have an account? 
            <NuxtLink to="/" class="text-green-600 hover:text-green-700 font-medium transition-colors">
              Sign up
            </NuxtLink>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// Define reactive form data
const form = ref({
  email: '',
  password: '',
  remember: false
})

// Handle form submission
const handleSubmit = () => {
  console.log('Form submitted:', form.value)
  // Add your authentication logic here
  // Example: await $fetch('/api/auth/signin', { method: 'POST', body: form.value })
}

// Handle Google sign-in
const signInWithGoogle = () => {
  console.log('Google sign-in clicked')
  // Add your Google OAuth logic here
}

// Set page metadata
useHead({
  title: 'Sign In - Your App Name',
  meta: [
    { name: 'description', content: 'Sign in to your account' }
  ]
})
</script>