<template>
    <div class="">
        <Menubar></Menubar>
        <div class="flex flex-col justify-center items-center gap-12 w-7xl h-auto py-4 px-2 mx-auto">
            <div class="card-outline-one max-w-7xl flex flex-col gap-10">
                <h1 class="title-three text-center">Infomation about collection point</h1>
                
                <!-- collect item infomations -->
                <div class="flex flex-col gap-6">
                    <div class="flex flex-col gap-2">
                        <h3 class="title-four">Collect items list</h3>
                        <hr class="">
                    </div>
                    <div class="flex flex-row gap-2 flex-wrap">
                        <p class="input-btn-selection cursor-default" :class="collectionPoints.collectItems.includes(item) ? 'bg-black text-white' : 'bg-white text-black'" v-for="item in itemList" @click="addItems(item)">{{ item }}</p>
                    </div>
                </div>

                <!-- location infomation -->
                <div class="flex flex-col gap-6">
                    <div class="flex flex-col gap-2">
                        <h3 class="title-four">Location infomations</h3>
                        <hr class="">
                    </div>
                    <div class="flex flex-col gap-4">
                        <div class="flex flex-col gap-2">
                            <p class="input-label-one">District</p>
                            <div class="flex flex-row gap-2 flex-wrap">
                                <p class="input-btn-selection cursor-default" :class="collectionPoints.district == item.value ? 'bg-black text-white' : 'bg-white text-black'" v-for="item in collectionPoints.allDisctrict" @click="selectDisctrict(item.value)">{{ item.location }}</p>
                            </div>
                        </div>
                        <div class="input-one-container">
                            <p class="input-label-one">Town</p>
                            <input type="text" class="input-one" v-model="collectionPoints.town">
                        </div>Location-specific Information

                        <div class="input-one-container">
                            <p class="input-label-one">Nearest place</p>
                            <input type="text" class="input-one" v-model="collectionPoints.nearestPlace">
                        </div>
                        <div class="input-one-container" v-if="collectionPoints.district != null && collectionPoints.town != null && collectionPoints.nearestPlace != null">
                            <p class="input-label-one">Your exact location</p>
                            <button class="btn-three" @click="getLocation">{{ collectionPoints.geoLocation == null ? 'Not set yet' : 'Seted' }}</button>
                        </div>
                    </div>
                </div>

                <!-- other infomation -->
                <div class="flex flex-col gap-6">
                    <div class="flex flex-col gap-2">
                        <h3 class="title-four">Other</h3>
                        <hr class="">
                    </div>
                    <div class="flex flex-col gap-4">
                        <div class="input-one-container">
                            <p class="input-label-one">Where to distribute</p>
                            <input type="text" class="input-one" v-model="collectionPoints.distributedTo">
                        </div>
                        <div class="input-one-container">
                            <p class="input-label-one">End date</p>
                            <input type="date" class="input-one" v-model="collectionPoints.endDate">
                        </div>
                        <div class="input-one-container">
                            <p class="input-label-one">Description</p>
                            <textarea type="date" class="input-one" v-model="collectionPoints.description"/>
                        </div>
                    </div>
                </div>

                <!-- action button -->
                <button class="btn-three w-full" @click="addCollectionPoint">Sumite</button>
            </div>
        </div>
    </div>
</template>

<script setup>
// import { useCollectionPointStore } from '~/store/collectionpoint.js'
import { useCollectionPointStore } from '@/store/collectionpoint'
import { useCookie } from '#app'
const config =  useRuntimeConfig()

const collectionPoints = useCollectionPointStore()

const itemList = ref([
    'Rice',
    'Dhal',
    'Chilli Powder',
    'Canned Fish',
    'Milk Powder',
    'Bottled Water',
    'Bread',
    'Sugar',
    'Salt',
    'Cooking Oil',
    'Biscuits',
    'Baby Food',
    'Soap',
    'Toothpaste',
    'Shampoo',
    'Sanitary Pads',
    'Mosquito Repellent',
    'First Aid Kit',
    'Medicine',
    'Blankets',
    'Clothes',
    'Slippers',
    'Towels',
    'Torch',
    'Batteries'
])

const addItems = (i) => {
    // check if items is available or not. then push to the selected items
    if(!collectionPoints.collectItems.includes(i)){
        collectionPoints.collectItems.push(i)
    }else if(collectionPoints.collectItems.includes(i)){
        collectionPoints.collectItems = collectionPoints.collectItems.filter((item) => item != i)
    }
    
}

const selectDisctrict = (i) => {
    collectionPoints.district = i
}

const getLocation = () => {
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(
            (position) => {
                collectionPoints.geoLocation = [position.coords.latitude,  position.coords.longitude]
                // console.log('Lat:', position.coords.latitude)
                // console.log('Lng:', position.coords.longitude)
            },
            (error) => {
                console.error('Error:', error.message)
            }
        )
    }else{
        console.error('Geolocation not supported')
    }
}

const resetPiniaStore = () => {
    collectionPoints.collectItems = [],
    collectionPoints.district = null,
    collectionPoints.town = null,
    collectionPoints.nearestPlace = null,
    collectionPoints.geoLocation = null,
    collectionPoints.distributedTo = null,
    collectionPoints.description = null,
    collectionPoints.endDate = null
}

const addCollectionPoint = async () => {

    // create object for the API requerest body
    const createUserApiBody = {
        "item_list": collectionPoints.collectItems,
        "district": collectionPoints.district,
        "town": collectionPoints.town,
        "exact_place": collectionPoints.nearestPlace,
        "cordination": collectionPoints.geoLocation,
        "distributed_to": collectionPoints.distributedTo,
        "descriptions": collectionPoints.description,
        "end_date": collectionPoints.endDate
    }
    
    const token = useCookie('token').value
    console.log(token)
    console.log(createUserApiBody)

    try{
        const response = await $fetch(
            `${config.public.url}/details`, 
            {
                method : 'POST',
                body : createUserApiBody,
                headers: {
                    'Authorization': `Bearer ${token}`, 
                    'Content-Type': 'application/json',
                }
            },
        )
        // success
        alert('item add succesfully')
        resetPiniaStore()

    }catch(error){
        console.log(`this is the error ${error}`)
    }
}

</script>