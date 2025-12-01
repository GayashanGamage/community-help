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
                        <p class="input-btn-selection" v-for="item in itemList" @click="addItems(item)">{{ item }}</p>
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
                                <p class="input-btn-selection" v-for="item in collectionPoints.allDisctrict">{{ item.location }}</p>
                            </div>
                        </div>
                        <div class="input-one-container">
                            <p class="input-label-one">Town</p>
                            <input type="text" class="input-one">
                        </div>
                        <div class="input-one-container">
                            <p class="input-label-one">Nearest place</p>
                            <input type="text" class="input-one">
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
                            <input type="text" class="input-one">
                        </div>
                        <div class="input-one-container">
                            <p class="input-label-one">How to deliver</p>
                            <input type="text" class="input-one">
                        </div>
                        <div class="input-one-container">
                            <p class="input-label-one">End date</p>
                            <input type="date" class="input-one">
                        </div>
                    </div>
                </div>

                <!-- action button -->
                <button class="btn-three w-full">Sumite</button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useCollectionPointStore } from '~/store/collectionpoint';

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
    console.log(i)
    collectionPoints.value.collectItems.push(i)
}

</script>