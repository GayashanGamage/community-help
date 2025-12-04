<template>
    <div class="w-full h-screen relative">
        <Menubar></Menubar>
        <div class="flex flex-col justify-center items-center gap-12 max-w-7xl h-[90vh] py-4 px-2 mx-auto">
            <h1 class="font-black text-5xl">Help to victim of Ditwah cyclone</h1>
            <p class="font-thin text-2xl text-center">Help us provide meals to families devastated by the Ditva Cyclone in Sri Lanka. Your immediate donation delivers vital food and hope. Please give now. Every contribution saves lives.</p>
            <div class="flex flex-row gap-4">
                <button class="border py-2 px-4 rounded-md bg-black text-white hover:bg-black/80 active:bg-black/70" @click="locationPopup = true">Find Collection point</button>
                <button class="border py-2 px-4 rounded-md bg-black text-white hover:bg-black/80 active:bg-black/70" @click="router.push('/map')">View on map</button>
            </div>
        </div>
        <div class="flex flex-col justify-center items-center w-full h-screen fixed top-0 bottom-0 left-0 right-0 z-10 bg-black/80" v-if="locationPopup">
            <div class="flex flex-col justify-center items-center gap-12 max-w-7xl h-[60vh] py-4 px-2 mx-auto border bg-white rounded-2xl relative">
                <h1 class="font-black text-2xl">Select your disctrict</h1>
                <div class="flex flex-row items-center justify-center flex-wrap gap-4 px-10">
                    <div class="border py-3 px-8 rounded-full border-gray-300 text-lg hover:bg-black active::bg-black/90 hover:text-white active:text-white hover:border-black active:border-black cursor-pointer" v-for="item in collectionStore.allDisctrict" @click="router.push(`/place/${item.value}`)">{{ item.location }}</div>
                </div>
                <div class=" absolute right-0 top-0 p-6" @click="locationPopup = false">
                    <Icon name="material-symbols:cancel-outline-rounded" class=" text-gray-400 hover:text-gray-600 text-4xl"/>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>

import { useCollectionPointStore } from '~/store/collectionpoint';

const locationPopup = ref(false)
const router = useRouter()
const collectionStore = useCollectionPointStore()


// const allDisctrict = ref([
//     { location: 'Ampara', value: 'ampara' },
//     { location: 'Anuradhapura', value: 'anuradhapura' },
//     { location: 'Badulla', value: 'badulla' },
//     { location: 'Batticaloa', value: 'batticaloa' },
//     { location: 'Colombo', value: 'colombo' },
//     { location: 'Galle', value: 'galle' },
//     { location: 'Gampaha', value: 'gampaha' },
//     { location: 'Hambantota', value: 'hambantota' },
//     { location: 'Jaffna', value: 'jaffna' },
//     { location: 'Kalutara', value: 'kalutara' },
//     { location: 'Kandy', value: 'kandy' },
//     { location: 'Kegalle', value: 'kegalle' },
//     { location: 'Kilinochchi', value: 'kilinochchi' },
//     { location: 'Kurunegala', value: 'kurunegala' },
//     { location: 'Mannar', value: 'mannar' },
//     { location: 'Matale', value: 'matale' },
//     { location: 'Matara', value: 'matara' },
//     { location: 'Monaragala', value: 'monaragala' },
//     { location: 'Mullaitivu', value: 'mullaitivu' },
//     { location: 'Nuwara Eliya', value: 'nuwara-eliya' },
//     { location: 'Polonnaruwa', value: 'polonnaruwa' },
//     { location: 'Puttalam', value: 'puttalam' },
//     { location: 'Ratnapura', value: 'ratnapura' },
//     { location: 'Trincomalee', value: 'trincomalee' },
//     { location: 'Vavuniya', value: 'vavuniya' }
// ])

</script>