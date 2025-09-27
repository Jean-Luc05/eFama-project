<template>
<body class="bg-gray-50 font-sans">
     Navigation Bar 
    <nav class="bg-white shadow-sm border-b border-gray-200 fixed w-full top-0 z-50">
        <div class="px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-16">
                 Logo 
                <div class="flex items-center">
                    <div class="flex-shrink-0">
                        <h1 class="text-2xl font-bold text-primary">E-Fama</h1>
                    </div>
                </div>

                 Navigation Buttons 
                <div class="hidden md:block">
                    <div class="ml-10 flex items-baseline space-x-4">
                        <button class="text-gray-700 hover:text-primary px-3 py-2 rounded-md text-sm font-medium transition-colors">
                            Dashboard
                        </button>
                        <button class="text-gray-700 hover:text-primary px-3 py-2 rounded-md text-sm font-medium transition-colors">
                            Analytics
                        </button>
                        <button class="text-gray-700 hover:text-primary px-3 py-2 rounded-md text-sm font-medium transition-colors">
                            Reports
                        </button>
                        <button class="text-gray-700 hover:text-primary px-3 py-2 rounded-md text-sm font-medium transition-colors">
                            Settings
                        </button>
                    </div>
                </div>

                 User Menu 
                <div class="flex items-center space-x-4">
                    <button class="text-gray-700 hover:text-primary p-2 rounded-md transition-colors">
                        <i data-lucide="bell" class="w-5 h-5"></i>
                    </button>
                    <div class="relative">
                        <button class="flex items-center space-x-2 text-gray-700 hover:text-primary p-2 rounded-md transition-colors">
                            <div class="w-8 h-8 bg-primary rounded-full flex items-center justify-center">
                                <span class="text-white text-sm font-medium">JD</span>
                            </div>
                            <i data-lucide="chevron-down" class="w-4 h-4"></i>
                        </button>
                    </div>
                </div>

                 Mobile menu button 
                <div class="md:hidden">
                    <button class="text-gray-700 hover:text-primary p-2 rounded-md transition-colors" onclick="toggleMobileMenu()">
                        <i data-lucide="menu" class="w-6 h-6"></i>
                    </button>
                </div>
            </div>
        </div>

         Mobile Navigation Menu 
        <div id="mobile-menu" class="md:hidden hidden bg-white border-t border-gray-200">
            <div class="px-2 pt-2 pb-3 space-y-1">
                <button class="text-gray-700 hover:text-primary block px-3 py-2 rounded-md text-base font-medium w-full text-left transition-colors">
                    Dashboard
                </button>
                <button class="text-gray-700 hover:text-primary block px-3 py-2 rounded-md text-base font-medium w-full text-left transition-colors">
                    Analytics
                </button>
                <button class="text-gray-700 hover:text-primary block px-3 py-2 rounded-md text-base font-medium w-full text-left transition-colors">
                    Reports
                </button>
                <button class="text-gray-700 hover:text-primary block px-3 py-2 rounded-md text-base font-medium w-full text-left transition-colors">
                    Settings
                </button>
            </div>
        </div>
    </nav>

    <div class="flex pt-16">
         Sidebar 
        <div class="hidden lg:flex lg:flex-shrink-0">
            <div class="flex flex-col w-64">
                <div class="flex flex-col flex-grow bg-white border-r border-gray-200 pt-5 pb-4 overflow-y-auto">
                    <div class="flex-grow flex flex-col">
                        <nav class="flex-1 px-2 space-y-1">
                             Dashboard Section 
                            <div class="space-y-1">
                                <button class="bg-primary text-white group flex items-center px-2 py-2 text-sm font-medium rounded-md w-full text-left transition-colors">
                                    <i data-lucide="home" class="text-white mr-3 flex-shrink-0 h-5 w-5"></i>
                                    Overview
                                </button>
                                <button class="text-gray-700 hover:text-primary hover:bg-gray-50 group flex items-center px-2 py-2 text-sm font-medium rounded-md w-full text-left transition-colors">
                                    <i data-lucide="bar-chart-3" class="text-gray-400 group-hover:text-primary mr-3 flex-shrink-0 h-5 w-5"></i>
                                    Analytics
                                </button>
                                <button class="text-gray-700 hover:text-primary hover:bg-gray-50 group flex items-center px-2 py-2 text-sm font-medium rounded-md w-full text-left transition-colors">
                                    <i data-lucide="users" class="text-gray-400 group-hover:text-primary mr-3 flex-shrink-0 h-5 w-5"></i>
                                    Customers
                                </button>
                                <button class="text-gray-700 hover:text-primary hover:bg-gray-50 group flex items-center px-2 py-2 text-sm font-medium rounded-md w-full text-left transition-colors">
                                    <i data-lucide="shopping-bag" class="text-gray-400 group-hover:text-primary mr-3 flex-shrink-0 h-5 w-5"></i>
                                    Orders
                                </button>
                                <button class="text-gray-700 hover:text-primary hover:bg-gray-50 group flex items-center px-2 py-2 text-sm font-medium rounded-md w-full text-left transition-colors">
                                    <i data-lucide="package" class="text-gray-400 group-hover:text-primary mr-3 flex-shrink-0 h-5 w-5"></i>
                                    Products
                                </button>
                            </div>

                             Management Section 
                            <div class="pt-6">
                                <h3 class="px-3 text-xs font-semibold text-gray-500 uppercase tracking-wider">
                                    Management
                                </h3>
                                <div class="mt-2 space-y-1">
                                    <button class="text-gray-700 hover:text-primary hover:bg-gray-50 group flex items-center px-2 py-2 text-sm font-medium rounded-md w-full text-left transition-colors">
                                        <i data-lucide="file-text" class="text-gray-400 group-hover:text-primary mr-3 flex-shrink-0 h-5 w-5"></i>
                                        Reports
                                    </button>
                                    <button class="text-gray-700 hover:text-primary hover:bg-gray-50 group flex items-center px-2 py-2 text-sm font-medium rounded-md w-full text-left transition-colors">
                                        <i data-lucide="credit-card" class="text-gray-400 group-hover:text-primary mr-3 flex-shrink-0 h-5 w-5"></i>
                                        Billing
                                    </button>
                                    <button class="text-gray-700 hover:text-primary hover:bg-gray-50 group flex items-center px-2 py-2 text-sm font-medium rounded-md w-full text-left transition-colors">
                                        <i data-lucide="settings" class="text-gray-400 group-hover:text-primary mr-3 flex-shrink-0 h-5 w-5"></i>
                                        Settings
                                    </button>
                                </div>
                            </div>

                             Support Section 
                            <div class="pt-6">
                                <h3 class="px-3 text-xs font-semibold text-gray-500 uppercase tracking-wider">
                                    Support
                                </h3>
                                <div class="mt-2 space-y-1">
                                    <button class="text-gray-700 hover:text-primary hover:bg-gray-50 group flex items-center px-2 py-2 text-sm font-medium rounded-md w-full text-left transition-colors">
                                        <i data-lucide="help-circle" class="text-gray-400 group-hover:text-primary mr-3 flex-shrink-0 h-5 w-5"></i>
                                        Help Center
                                    </button>
                                    <button class="text-gray-700 hover:text-primary hover:bg-gray-50 group flex items-center px-2 py-2 text-sm font-medium rounded-md w-full text-left transition-colors">
                                        <i data-lucide="message-circle" class="text-gray-400 group-hover:text-primary mr-3 flex-shrink-0 h-5 w-5"></i>
                                        Contact Support
                                    </button>
                                </div>
                            </div>
                        </nav>
                    </div>

                     User Profile Section 
                    <div class="flex-shrink-0 flex border-t border-gray-200 p-4">
                        <div class="flex items-center">
                            <div class="w-10 h-10 bg-primary rounded-full flex items-center justify-center">
                                <span class="text-white text-sm font-medium">JD</span>
                            </div>
                            <div class="ml-3">
                                <p class="text-sm font-medium text-gray-700">John Doe</p>
                                <p class="text-xs text-gray-500">john@e-fama.com</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

         Main Content 
        <div class="flex-1 overflow-auto">
            <div class="p-6">
                 Page Header 
                <div class="mb-8">
                    <h1 class="text-3xl font-bold text-gray-900">Dashboard Overview</h1>
                    <p class="mt-2 text-gray-600">Welcome back! Here's what's happening with your business today.</p>
                </div>

                 Stats Cards 
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
                    <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
                        <div class="flex items-center">
                            <div class="flex-shrink-0">
                                <div class="w-8 h-8 bg-primary bg-opacity-10 rounded-md flex items-center justify-center">
                                    <i data-lucide="dollar-sign" class="w-5 h-5 text-primary"></i>
                                </div>
                            </div>
                            <div class="ml-4">
                                <p class="text-sm font-medium text-gray-600">Total Revenue</p>
                                <p class="text-2xl font-bold text-gray-900">$45,231</p>
                            </div>
                        </div>
                        <div class="mt-4">
                            <span class="text-sm text-primary font-medium">+12.5%</span>
                            <span class="text-sm text-gray-500 ml-1">from last month</span>
                        </div>
                    </div>

                    <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
                        <div class="flex items-center">
                            <div class="flex-shrink-0">
                                <div class="w-8 h-8 bg-primary bg-opacity-10 rounded-md flex items-center justify-center">
                                    <i data-lucide="users" class="w-5 h-5 text-primary"></i>
                                </div>
                            </div>
                            <div class="ml-4">
                                <p class="text-sm font-medium text-gray-600">New Customers</p>
                                <p class="text-2xl font-bold text-gray-900">1,234</p>
                            </div>
                        </div>
                        <div class="mt-4">
                            <span class="text-sm text-primary font-medium">+8.2%</span>
                            <span class="text-sm text-gray-500 ml-1">from last month</span>
                        </div>
                    </div>

                    <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
                        <div class="flex items-center">
                            <div class="flex-shrink-0">
                                <div class="w-8 h-8 bg-primary bg-opacity-10 rounded-md flex items-center justify-center">
                                    <i data-lucide="shopping-bag" class="w-5 h-5 text-primary"></i>
                                </div>
                            </div>
                            <div class="ml-4">
                                <p class="text-sm font-medium text-gray-600">Total Orders</p>
                                <p class="text-2xl font-bold text-gray-900">5,678</p>
                            </div>
                        </div>
                        <div class="mt-4">
                            <span class="text-sm text-primary font-medium">+15.3%</span>
                            <span class="text-sm text-gray-500 ml-1">from last month</span>
                        </div>
                    </div>

                    <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
                        <div class="flex items-center">
                            <div class="flex-shrink-0">
                                <div class="w-8 h-8 bg-primary bg-opacity-10 rounded-md flex items-center justify-center">
                                    <i data-lucide="trending-up" class="w-5 h-5 text-primary"></i>
                                </div>
                            </div>
                            <div class="ml-4">
                                <p class="text-sm font-medium text-gray-600">Growth Rate</p>
                                <p class="text-2xl font-bold text-gray-900">23.5%</p>
                            </div>
                        </div>
                        <div class="mt-4">
                            <span class="text-sm text-primary font-medium">+2.1%</span>
                            <span class="text-sm text-gray-500 ml-1">from last month</span>
                        </div>
                    </div>
                </div>

                 Content Grid 
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                     Recent Activity 
                    <div class="bg-white rounded-lg shadow-sm border border-gray-200">
                        <div class="p-6 border-b border-gray-200">
                            <h3 class="text-lg font-semibold text-gray-900">Recent Activity</h3>
                        </div>
                        <div class="p-6">
                            <div class="space-y-4">
                                <div class="flex items-center space-x-3">
                                    <div class="w-8 h-8 bg-primary bg-opacity-10 rounded-full flex items-center justify-center">
                                        <i data-lucide="user-plus" class="w-4 h-4 text-primary"></i>
                                    </div>
                                    <div class="flex-1">
                                        <p class="text-sm text-gray-900">New customer registered</p>
                                        <p class="text-xs text-gray-500">2 minutes ago</p>
                                    </div>
                                </div>
                                <div class="flex items-center space-x-3">
                                    <div class="w-8 h-8 bg-primary bg-opacity-10 rounded-full flex items-center justify-center">
                                        <i data-lucide="shopping-cart" class="w-4 h-4 text-primary"></i>
                                    </div>
                                    <div class="flex-1">
                                        <p class="text-sm text-gray-900">Order #1234 completed</p>
                                        <p class="text-xs text-gray-500">5 minutes ago</p>
                                    </div>
                                </div>
                                <div class="flex items-center space-x-3">
                                    <div class="w-8 h-8 bg-primary bg-opacity-10 rounded-full flex items-center justify-center">
                                        <i data-lucide="credit-card" class="w-4 h-4 text-primary"></i>
                                    </div>
                                    <div class="flex-1">
                                        <p class="text-sm text-gray-900">Payment received</p>
                                        <p class="text-xs text-gray-500">10 minutes ago</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                     Quick Actions 
                    <div class="bg-white rounded-lg shadow-sm border border-gray-200">
                        <div class="p-6 border-b border-gray-200">
                            <h3 class="text-lg font-semibold text-gray-900">Quick Actions</h3>
                        </div>
                        <div class="p-6">
                            <div class="grid grid-cols-2 gap-4">
                                <button class="flex flex-col items-center p-4 border border-gray-200 rounded-lg hover:border-primary hover:bg-primary hover:bg-opacity-5 transition-colors">
                                    <i data-lucide="plus" class="w-8 h-8 text-primary mb-2"></i>
                                    <span class="text-sm font-medium text-gray-900">Add Product</span>
                                </button>
                                <button class="flex flex-col items-center p-4 border border-gray-200 rounded-lg hover:border-primary hover:bg-primary hover:bg-opacity-5 transition-colors">
                                    <i data-lucide="user-plus" class="w-8 h-8 text-primary mb-2"></i>
                                    <span class="text-sm font-medium text-gray-900">Add Customer</span>
                                </button>
                                <button class="flex flex-col items-center p-4 border border-gray-200 rounded-lg hover:border-primary hover:bg-primary hover:bg-opacity-5 transition-colors">
                                    <i data-lucide="file-text" class="w-8 h-8 text-primary mb-2"></i>
                                    <span class="text-sm font-medium text-gray-900">Generate Report</span>
                                </button>
                                <button class="flex flex-col items-center p-4 border border-gray-200 rounded-lg hover:border-primary hover:bg-primary hover:bg-opacity-5 transition-colors">
                                    <i data-lucide="settings" class="w-8 h-8 text-primary mb-2"></i>
                                    <span class="text-sm font-medium text-gray-900">Settings</span>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</template>

<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  // If lucide was loaded via CDN
  if (typeof lucide !== 'undefined') {
    lucide.createIcons()
  }
})
</script>


