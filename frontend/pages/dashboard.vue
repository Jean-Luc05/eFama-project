<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Navbar -->
    <nav class="bg-white shadow-sm border-b border-gray-200 fixed w-full top-0 z-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          <!-- Logo -->
          <h1 class="text-2xl font-bold text-green-600">E-Fama</h1>

          <!-- User Icon -->
            <div class="relative">
                <!-- User Icon Button -->
                <button
                @click="toggleMenu"
                class="p-2 rounded-full text-gray-600 hover:text-gray-900 hover:bg-gray-100 focus:outline-none"
                aria-label="User menu"
                >
                <i class="fas fa-user text-xl"></i>
                </button>

                <!-- Dropdown Menu -->
                <div
                v-if="menuOpen"
                class="absolute right-0 mt-2 w-56 bg-white border border-gray-200 rounded-lg shadow-lg z-50"
                >
                <div class="px-4 py-3 border-b border-gray-100">
                    <p class="text-sm font-semibold text-gray-900">John Doe</p>
                    <p class="text-xs text-gray-500">john@example.com</p>
                </div>
                <ul class="py-1">
                    <li>
                    <NuxtLink
                        to="/profile"
                        class="flex items-center px-4 py-3 text-sm text-gray-700 hover:bg-gray-100 hover:text-primary transition-colors"
                    >
                        <i class="fas fa-user-circle mr-3 text-lg text-primary"></i>
                        Profile
                    </NuxtLink>
                    </li>
                    <li>
                    <button
                        @click="logout"
                        class="flex items-center w-full text-left px-4 py-3 text-sm text-red-600 hover:bg-red-50 transition-colors"
                    >
                        <i class="fas fa-sign-out-alt mr-3 text-lg"></i>
                        Logout
                    </button>
                    </li>
                </ul>
                </div>
            </div>
        </div>
      </div>
    </nav>

    <!-- Main content -->
    <main class="pt-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Welcome Section -->
      <section class="mb-8">
        <h2 class="text-3xl font-bold text-gray-900 mb-2">Welcome back!</h2>
        <p class="text-gray-600">Here's what's happening with your farm today.</p>
      </section>

    <section class="bg-gradient-to-br from-blue-50 to-blue-100 rounded-xl shadow-lg border border-blue-200 p-6 mb-8 animate-fade-in">
    <div class="flex items-center justify-between mb-4">
        <h3 class="text-2xl font-bold text-blue-900 flex items-center space-x-2">
        <i class="fas fa-chart-line text-blue-700 text-2xl"></i>
        <span>Forecasting Results</span>
        </h3>
        <span class="text-sm text-blue-600 bg-blue-200 px-2 py-1 rounded-full">
        Last updated: 5 mins ago
        </span>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- 7-Day Forecast -->
        <div class="bg-white border border-blue-200 rounded-lg p-5 shadow-sm hover:shadow-md transition">
        <h4 class="text-lg font-semibold text-blue-800 mb-3">Next 7 Days</h4>
        <div class="flex items-center justify-between mb-2">
            <div class="flex items-center space-x-2">
            <i class="fas fa-dollar-sign text-green-600 text-xl"></i>
            <span class="text-gray-700">Forecasted Price</span>
            </div>
            <span class="text-2xl font-bold text-gray-900">R2.45 / kg</span>
        </div>
        <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2">
            <i class="fas fa-boxes text-blue-600 text-xl"></i>
            <span class="text-gray-700">Forecasted Demand</span>
            </div>
            <span class="text-2xl font-bold text-gray-900">1,200 units</span>
        </div>
        </div>

        <!-- 30-Day Forecast -->
        <div class="bg-white border border-blue-200 rounded-lg p-5 shadow-sm hover:shadow-md transition">
        <h4 class="text-lg font-semibold text-blue-800 mb-3">Next 30 Days</h4>
        <div class="flex items-center justify-between mb-2">
            <div class="flex items-center space-x-2">
            <i class="fas fa-dollar-sign text-green-600 text-xl"></i>
            <span class="text-gray-700">Forecasted Price</span>
            </div>
            <span class="text-2xl font-bold text-gray-900">$2.60 / kg</span>
        </div>
        <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2">
            <i class="fas fa-boxes text-blue-600 text-xl"></i>
            <span class="text-gray-700">Forecasted Demand</span>
            </div>
            <span class="text-2xl font-bold text-gray-900">5,100 units</span>
        </div>
        </div>
    </div>
    </section>


      <!-- Stats Cards -->
      <section class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <div class="bg-white rounded-lg shadow-sm p-6 border border-gray-200">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-600">Total Crops</p>
              <p class="text-2xl font-bold text-gray-900">24</p>
            </div>
            <div class="p-3 bg-primary/10 rounded-full">
              <i class="fas fa-seedling text-primary text-xl"></i>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-lg shadow-sm p-6 border border-gray-200">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-600">Active Listings</p>
              <p class="text-2xl font-bold text-gray-900">12</p>
            </div>
            <div class="p-3 bg-blue-100 rounded-full">
              <i class="fas fa-list text-blue-600 text-xl"></i>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-lg shadow-sm p-6 border border-gray-200">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-600">Total Sales</p>
              <p class="text-2xl font-bold text-gray-900">R8,420</p>
            </div>
            <div class="p-3 bg-green-100 rounded-full">
              <i class="fas fa-dollar-sign text-green-600 text-xl"></i>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-lg shadow-sm p-6 border border-gray-200">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-600">Pending Orders</p>
              <p class="text-2xl font-bold text-gray-900">5</p>
            </div>
            <div class="p-3 bg-yellow-100 rounded-full">
              <i class="fas fa-clock text-yellow-600 text-xl"></i>
            </div>
          </div>
        </div>
      </section>


      <!-- Quick Actions -->
      <section class="bg-white rounded-lg shadow-sm p-6 border border-gray-200 mb-8">
        <h3 class="text-lg font-semibold text-gray-900 mb-4">Quick Actions</h3>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            <NuxtLink
            to="/upload-crops"
            class="flex items-center justify-center px-4 py-3 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors"
            >
            <i class="fas fa-plus mr-2"></i> Add Crop
            </NuxtLink>


          <button class="flex items-center justify-center px-4 py-3 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-colors">
            <i class="fas fa-eye mr-2"></i> View Listings
          </button>
          <button class="flex items-center justify-center px-4 py-3 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-colors">
            <i class="fas fa-chart-bar mr-2"></i> View Reports
          </button>
          <button class="flex items-center justify-center px-4 py-3 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-colors">
            <i class="fas fa-envelope mr-2"></i> Messages
          </button>
        </div>
      </section>

      <!-- Recent Activity -->
      <section class="bg-white rounded-lg shadow-sm p-6 border border-gray-200">
        <h3 class="text-lg font-semibold text-gray-900 mb-4">Recent Activity</h3>
        <div class="space-y-4">
          <div class="flex items-center space-x-3">
            <div class="p-2 bg-primary/10 rounded-full">
              <i class="fas fa-seedling text-primary"></i>
            </div>
            <div class="flex-1">
              <p class="text-sm font-medium text-gray-900">New crop listing created</p>
              <p class="text-xs text-gray-500">2 hours ago</p>
            </div>
          </div>
          <div class="flex items-center space-x-3">
            <div class="p-2 bg-green-100 rounded-full">
              <i class="fas fa-check text-green-600"></i>
            </div>
            <div class="flex-1">
              <p class="text-sm font-medium text-gray-900">Order completed</p>
              <p class="text-xs text-gray-500">5 hours ago</p>
            </div>
          </div>
          <div class="flex items-center space-x-3">
            <div class="p-2 bg-blue-100 rounded-full">
              <i class="fas fa-message text-blue-600"></i>
            </div>
            <div class="flex-1">
              <p class="text-sm font-medium text-gray-900">New message received</p>
              <p class="text-xs text-gray-500">1 day ago</p>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const menuOpen = ref(false)

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value
}

const closeMenu = () => {
  menuOpen.value = false
}
</script>

<style scoped>
@keyframes fade-in {
  0% { opacity: 0; transform: translateY(-10px); }
  100% { opacity: 1; transform: translateY(0); }
}

.animate-fade-in {
  animation: fade-in 0.8s ease-in-out;
}
</style>


