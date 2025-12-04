<template>
    <ClientOnly>
        <div class="">
            <Menubar></Menubar>
            <div class="max-w-7xl h-[90vh] relative mx-auto px-2">
                <LMap
                    ref="map"
                    class="w-full h-full"
                    :zoom="8.4"
                    :center="[7.8731, 80.7718]"
                    :use-global-leaflet="false"
                    @ready="onMapReady"
                >
                <LMarker 
                v-for="point in collectionpoint.allLocationList" 
                    :key="point.name" 
                    :lat-lng="[point.cordination[0], point.cordination[1]]"
                >
                    <LPopup class="flex flex-col gap-0">
                        <div class="font-semibold text-indigo-800">collect by {{ point.first_name }} - {{ point.mobile_number }}</div>
                        <p class=""><span class="border-0 py-1 px-2 rounded-full bg-gray-300 text-white text-xs">{{ point.organization_type }}</span></p>
                        <div class="text-sm text-gray-600">{{ point.description }}</div>
                        <button class="border py-1 px-2 rounded-md bg-black text-white">More</button>
                    </LPopup>
                </LMarker>
                <LTileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />
                </LMap>
            </div>
        </div>
    </ClientOnly>
</template>

<script setup>
import { useCollectionPointStore } from '~/store/collectionpoint';

const map = ref(null);
const config = useRuntimeConfig()
const collectionpoint =  useCollectionPointStore()

const {data:locationData} = await useFetch(`${config.public.url}/location/all`)

if(locationData){
    console.log(locationData.value.locations)
    collectionpoint.allLocationList =  locationData.value.locations
}


const collectionPoints = [
  { 
    name: 'Galle Fort Entrance', 
    lat: 6.0336, 
    lng: 80.2170, 
    description: 'Historical main collection point (UNESCO site)' 
  },
  { 
    name: 'Galle International Cricket Stadium', 
    lat: 6.0347, 
    lng: 80.2155, 
    description: 'Near the sea face, good for large gathering' 
  },
  { 
    name: 'Unawatuna Beach', 
    lat: 6.0150, 
    lng: 80.2520, 
    description: 'Southern beach-side community collection spot' 
  }
];

</script>
