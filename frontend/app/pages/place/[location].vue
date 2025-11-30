<template>
    <Menubar></Menubar>
    <div class="flex flex-col gap-12 w-7xl h-[90vh] mx-auto py-10 px-2">
        <h1 class="font-medium text-xl">Collection points in <span class="font-black">{{ route.params.location }}</span></h1>
        
        <!-- filter section -->
        <div class="flex flex-row items-center gap-5 w-full h-auto">
            <h3 class="">Organize by : </h3>
            <div class="flex flex-row gap-4">
                <div class="border py-1 px-4 rounded-md border-gray-300 cursor-default" :class="index == selectedFiter ? 'bg-black text-white border-black' : 'border-gray-300 bg-white text-black'" v-for="(item, index) in filters" @click="selectedFiter = index">{{ item.name }}</div>
            </div>
        </div>
        <hr class="border-gray-200">
        
        <!-- location list -->
        <div class="grid grid-cols-1 gap-6">
            <div class="grid grid-cols-10 gap-2 h-fit border p-2 rounded-md border-gray-200 shadow-md" v-for="(item, index) in locationDetials">
                <img src="" alt="" class="col-span-3 border border-gray-200 rounded-md">
                <div class="flex flex-col gap-3 col-span-7">
                    <!-- organization type -->
                    <div class="">
                        <p class="font-light">Organized by <span class=" ml-10 border border-gray-300 py-1 px-4 rounded-full text-gray-800 text-sm">{{ item.organizeBy }}</span></p>
                    </div>

                    <!-- organization contacts -->
                    <div class="flex flex-row justify-between">
                        <p class="font-light">Organizer : <span class="font-semibold text-lg">{{ item.organizerName }}</span></p>
                        <p class="font-light">Contact : <span class="font-semibold text-lg">{{ item.contactNumber }}</span></p>
                    </div>

                    <!-- location -->
                    <div class="flex flex-col gap-3">
                        <div class="flex flex-row justify-between">
                            <p class="font-light">District : <span class="font-semibold text-lg">{{ item.district }}</span></p>
                            <p class="font-light">Town : <span class="font-semibold text-lg">{{ item.town }}</span></p>
                        </div>
                        <p class="font-light">nearest place : <span class="font-semibold text-lg">{{ item.nearestLocation }}</span></p>
                    </div>

                    <!-- action button -->
                    <button class="border rounded-sm w-fit py-1 px-8 ml-auto border-gray-400 hover:bg-black hover:text-white hover:border-black" @click="selectedCollectionPoint = index" :class="index == selectedCollectionPoint ? 'hidden' : 'block'">More</button>

                    <!-- hidden content -->
                    <div class="" :class="index == selectedCollectionPoint ? 'block' : 'hidden'">
                        <div class="flex felx-row justify-between">
                            <p class="font-light">Where to deliver <span class="font-semibold text-lg">{{ item.deliveryLocation }}</span></p>
                            <p class="font-light">Delivery methord <span class="font-semibold text-lg">{{ item.deliveryMethod }}</span></p>
                        </div>

                        <!-- collection items -->
                        <div class="flex flex-col gap-2 py-2">
                            <h4 class="font-light">Collected Items</h4>
                            <div class="flex flex-row gap-4 flex-wrap">
                                <p class="border border-gray-200 py-1 px-4 rounded-md bg-gray-200" v-for="i in item.accepteList">{{ i }}</p>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    
    </div>
</template>

<script setup>
const route =  useRoute()
const selectedCollectionPoint = ref(null)
const selectedFiter = ref(0)
const filters = ref(
    [
        {
            name : 'All',
            value : 'all'
        },
        {
            name : 'Individual',
            value : 'inidvidual'
        },
        {
            name : 'Non profit organization',
            value : 'nonprofit'
        },
        {
            name : 'Community',
            value : 'community'
        },
        {
            name : 'Temple',
            value : 'temple'
        },
        {
            name : 'Mosque',
            value : 'mosque'
        },
    ]
)

const locationDetials = ref(
    [
        {
            image : '',
            organizeBy : 'Individual',
            organizerName : 'Kalinga',
            contactNumber : '0717374076',
            district : 'galle',
            town : 'udugama',
            nearestLocation : 'infront of udugama maha vidyalaya',
            accepteList : ['cloths', 'shampoo', 'weifo'],
            deliveryLocation : 'Kandy - Galaha',
            deliveryMethod : 'By lorry',
            end : '2025.12.02'
        },
        {
            image : '',
            organizeBy : 'Individual',
            organizerName : 'Kalinga',
            contactNumber : '0717374076',
            district : 'galle',
            town : 'udugama',
            nearestLocation : 'infront of udugama maha vidyalaya',
            accepteList : ['cloths', 'shampoo', 'weifo'],
            deliveryLocation : 'Kandy - Galaha',
            deliveryMethod : 'By lorry',
            end : '2025.12.02'
        },
        {
            image : '',
            organizeBy : 'Individual',
            organizerName : 'Kalinga',
            contactNumber : '0717374076',
            district : 'galle',
            town : 'udugama',
            nearestLocation : 'infront of udugama maha vidyalaya',
            accepteList : ['cloths', 'shampoo', 'weifo'],
            deliveryLocation : 'Kandy - Galaha',
            deliveryMethod : 'By lorry',
            end : '2025.12.02'
        },
    ]
)

</script>