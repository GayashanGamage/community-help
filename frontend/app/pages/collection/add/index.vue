<template>
    <div class="">
        <Menubar></Menubar>
        <div class="flex flex-col justify-center items-center gap-12 w-7xl h-[90vh] py-4 px-2 mx-auto">
            <div class="card-outline-one flex flex-col gap-8 w-96">
                <h4 class="title-three text-center">Add collection point</h4>
                <div class="flex flex-col gap-6">
                    <div class="flex flex-col gap-2">
                        <label for="name" class="input-label-one">Organization type</label>
                        <div class="flex flex-row gap-2 flex-wrap">
                            <p class="border py-1 px-2 rounded-md border-gray-300 cursor-default" :class="collectionstore.organization == item ? 'bg-black text-white' : 'bg-white text-black'" v-for="item in collectionstore.organizationTypes" @click="collectionstore.organization = item">{{ item }}</p>
                        </div>
                    </div>
                    <div class="flex flex-col gap-2">
                        <label for="name" class="input-label-one">First Name</label>
                        <input id="name" type="text" class="input-one" placeholder="Nimesh waduge" spellcheck="false" v-model="collectionstore.firstName">
                    </div>
                    <div class="flex flex-col gap-2">
                        <label for="name" class="input-label-one">Mobile number</label>
                        <input type="text" class="input-one" placeholder="071 000 0000" v-model="collectionstore.mobileNumber">
                    </div>
                </div>
                <button class="btn-three" @click="createUser">Vefiry Mobile Number</button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useCollectionPointStore } from '@/store/collectionpoint';

const router = useRouter()

const collectionstore = useCollectionPointStore()
const config =  useRuntimeConfig()

const pageReDirection = () => {
    // this is for redirect to another page
    router.push('/collection/add/otp')
}

const clearPiniaStore = () => {
    // this is for clear pinia store unwanted data

    collectionstore.firstName = null
    collectionstore.organization = null
}

const createUser = async () => {

    // create object for the API requerest body
    const createUserApiBody = {
        "organization_type": collectionstore.organization,
        "first_name": collectionstore.firstName,
        "mobile_number": collectionstore.mobileNumber,
    }
    
    try{
        const response = await $fetch(
            `${config.public.url}/createaccount`, 
            {
                method : 'POST',
                body : createUserApiBody
            }
        )

        // success api requres
        console.log('acceount creation success')
        localStorage.setItem('mobileNumber', collectionstore.mobileNumber) //store mobile number in local storage
        clearPiniaStore()
        pageReDirection()

    }catch(error){
        console.log(`this is the error ${error}`)
    }
}

onBeforeMount(() => {
    if(localStorage.getItem('mobileNumber')){
        collectionstore.mobileNumber = localStorage.getItem('mobileNumber')
        return navigateTo('/collection/add/otp')
    }
})

</script>