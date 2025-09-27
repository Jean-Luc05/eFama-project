<template>
<body class="bg-gray-50 min-h-screen">
    <!-- Header -->
    <header class="bg-white shadow-sm border-b">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-16">
                <div class="flex items-center">
                    <h1 class="text-2xl font-bold text-primary">E-Fama</h1>
                </div>
                <nav class="hidden md:flex space-x-8">
                    <a href="/dashboard" class="text-gray-700 hover:text-primary transition-colors">Dashboard</a>
                </nav>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-4xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
        <div class="bg-white rounded-lg shadow-md p-6 md:p-8">
            <div class="mb-8">
                <h2 class="text-3xl font-bold text-gray-900 mb-2">Upload Crop Information</h2>
                <p class="text-gray-600">Add your crop details to connect with potential buyers</p>
            </div>

            <form class="space-y-6">
                <!-- Crop Type -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label for="crop" class="block text-sm font-medium text-gray-700 mb-2">
                            Crop Type *
                        </label>
                        <select id="crop" name="crop" required 
                                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-colors">
                            <option value="">Select crop type</option>
                            <option value="wheat">Wheat</option>
                            <option value="corn">Corn</option>
                            <option value="soybeans">Soybeans</option>
                            <option value="rice">Rice</option>
                            <option value="barley">Barley</option>
                            <option value="oats">Oats</option>
                            <option value="canola">Canola</option>
                            <option value="potatoes">Potatoes</option>
                            <option value="tomatoes">Tomatoes</option>
                            <option value="apples">Apples</option>
                            <option value="other">Other</option>
                        </select>
                    </div>

                    <!-- Grade -->
                    <div>
                        <label for="grade" class="block text-sm font-medium text-gray-700 mb-2">
                            Grade *
                        </label>
                        <select id="grade" name="grade" required 
                                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-colors">
                            <option value="">Select grade</option>
                            <option value="premium">Premium (Grade A)</option>
                            <option value="standard">Standard (Grade B)</option>
                            <option value="commercial">Commercial (Grade C)</option>
                            <option value="organic">Organic Certified</option>
                            <option value="non-gmo">Non-GMO</option>
                        </select>
                    </div>
                </div>

                <!-- Quantity and Unit -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label for="quantity" class="block text-sm font-medium text-gray-700 mb-2">
                            Quantity *
                        </label>
                        <input type="number" id="quantity" name="quantity" required min="1" step="0.01"
                               placeholder="Enter quantity"
                               class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-colors">
                    </div>

                    <div>
                        <label for="unit" class="block text-sm font-medium text-gray-700 mb-2">
                            Unit *
                        </label>
                        <select id="unit" name="unit" required 
                                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-colors">
                            <option value="">Select unit</option>
                            <option value="tons">Tons</option>
                            <option value="bushels">Bushels</option>
                            <option value="pounds">Pounds</option>
                            <option value="kilograms">Kilograms</option>
                            <option value="bags">Bags</option>
                            <option value="crates">Crates</option>
                        </select>
                    </div>
                </div>

                <!-- Region -->
                <div>
                    <label for="region" class="block text-sm font-medium text-gray-700 mb-2">
                        Region *
                    </label>
                    <select id="region" name="region" required 
                            class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-colors">
                        <option value="">Select your region</option>
                        <option value="alberta">Alberta</option>
                        <option value="british-columbia">British Columbia</option>
                        <option value="manitoba">Manitoba</option>
                        <option value="new-brunswick">New Brunswick</option>
                        <option value="newfoundland">Newfoundland and Labrador</option>
                        <option value="northwest-territories">Northwest Territories</option>
                        <option value="nova-scotia">Nova Scotia</option>
                        <option value="nunavut">Nunavut</option>
                        <option value="ontario">Ontario</option>
                        <option value="prince-edward-island">Prince Edward Island</option>
                        <option value="quebec">Quebec</option>
                        <option value="saskatchewan">Saskatchewan</option>
                        <option value="yukon">Yukon</option>
                    </select>
                </div>

                <!-- Intended Sell Date -->
                <div>
                    <label for="sell-date" class="block text-sm font-medium text-gray-700 mb-2">
                        Intended Sell Date *
                    </label>
                    <input type="date" id="sell-date" name="sell-date" required
                           class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-colors">
                    <p class="text-sm text-gray-500 mt-1">When do you plan to sell this crop?</p>
                </div>

                <!-- Additional Information -->
                <div>
                    <label for="description" class="block text-sm font-medium text-gray-700 mb-2">
                        Additional Information
                    </label>
                    <textarea id="description" name="description" rows="4" 
                              placeholder="Add any additional details about your crop (storage conditions, certifications, etc.)"
                              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-colors resize-none"></textarea>
                </div>

                <!-- Price Information -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label for="price" class="block text-sm font-medium text-gray-700 mb-2">
                            Expected Price per Unit (CAD)
                        </label>
                        <input type="number" id="price" name="price" min="0" step="0.01"
                               placeholder="Enter expected price"
                               class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-colors">
                    </div>

                    <div>
                        <label for="negotiable" class="block text-sm font-medium text-gray-700 mb-2">
                            Price Negotiable?
                        </label>
                        <select id="negotiable" name="negotiable" 
                                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-colors">
                            <option value="yes">Yes</option>
                            <option value="no">No</option>
                        </select>
                    </div>
                </div>

                <!-- Submit Buttons -->
                <div class="flex flex-col sm:flex-row gap-4 pt-6">
                    <button type="submit" 
                            class="flex-1 bg-primary hover:bg-primary-dark text-white font-semibold py-3 px-6 rounded-lg transition-colors focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-2">
                        Upload Crop Information
                    </button>
                    <button type="button" 
                            class="flex-1 bg-green-600 hover:bg-green-700 text-white font-semibold py-3 px-6 rounded-lg transition-colors focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2">
                        Save as Draft
                    </button>
                </div>
            </form>
        </div>


    </main>

</body>
</template>