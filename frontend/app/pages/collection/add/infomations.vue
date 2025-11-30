<template>
    <div class="">
        <Menubar></Menubar>
        <div class="flex flex-col justify-center items-center gap-12 w-7xl h-[90vh] py-4 px-2 mx-auto">
            <div class="border flex flex-col gap-4 p-4">
                <h1 class="text-center">Infomation about collection point</h1>
                
                <!-- location infomation -->
                <div class="">
                    <div class="">
                        <h3 class="">Location infomations</h3>
                        <hr class="">
                    </div>
                    <div class="">
                        <div class="">
                            <p class="">District</p>
                            <div class="flex flex-row gap-4 flex-wrap">
                                <p class="border" v-for="item in collectionPoints.allDisctrict">{{ item.location }}</p>
                            </div>
                        </div>
                        <div class="">
                            <p class="">Town</p>
                            <input type="text" class="border">
                        </div>
                        <div class="">
                            <p class="">Nearest place</p>
                            <input type="text" class="border">
                        </div>
                    </div>
                </div>
                
                <!-- collect item infomations -->
                <div class="">
                    <div class="">
                        <h3 class="">Collect items list</h3>
                        <hr class="">
                    </div>
                    <div class="flex flex-row gap-4 flex-wrap">
                        <p class="border" v-for="item in itemList">{{ item }}</p>
                    </div>
                </div>

                <!-- other infomation -->
                <div class="">
                    <div class="">
                        <h3 class="">Other</h3>
                        <hr class="">
                    </div>
                    <div class="">
                        <div class="">
                            <p class="">Where to distribute</p>
                            <input type="text" class="border">
                        </div>
                        <div class="">
                            <p class="">How to deliver</p>
                            <input type="text" class="border">
                        </div>
                        <div class="">
                            <p class="">End date</p>
                            <input type="text" class="border">
                        </div>
                    </div>
                </div>

                <!-- action button -->
                <button class="">Sumite</button>
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
</script>