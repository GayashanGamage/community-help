<template>
    <div class="">
        <Menubar></Menubar>
        <div class="flex flex-col justify-center items-center gap-12 w-7xl h-[90vh] py-4 px-2 mx-auto">
            <div class="card-outline-one flex flex-col gap-7 w-96">
                <h4 class="title-three text-center">Check your messages</h4>
                <div class="flex flex-row justify-around">
                    <input type="text" class="input-two" maxlength="1" size="1" ref="otpNumOne" @keyup="otpNumTwo.focus()" v-model="OTPnumber1">
                    <input type="text" class="input-two" maxlength="1" size="1" ref="otpNumTwo" @keyup="otpNumThree.focus()" v-model="OTPnumber2">
                    <input type="text" class="input-two" maxlength="1" size="1" ref="otpNumThree" @keyup="otpNumFour.focus()" v-model="OTPnumber3">
                    <input type="text" class="input-two" maxlength="1" size="1" ref="otpNumFour" v-model="OTPnumber4">
                </div>
                <button class="btn-three w-full" @click="verification">Vefiry</button>
                <div class="flex flex-col w-full h-auto text-gray-400 bg-green-100 p-4 rounded-md text-sm cursor-default">
                    <p class="">Check your {{ collectionstore.mobileNumber }} inbox</p>
                    <div class="flex flex-row justify-between">
                        <p class="hover:text-gray-600" @click="newAccount">Use another account</p>
                        <!-- <p class="hover:text-gray-600" @click="resendcode">Resend</p> -->
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useCollectionPointStore } from '@/store/collectionpoint';
const router = useRouter()

const otpNumOne = ref(null)
const otpNumTwo = ref(null)
const otpNumThree = ref(null)
const otpNumFour = ref(null)

const collectionstore = useCollectionPointStore()
const config =  useRuntimeConfig()

const OTPnumber1 = ref()
const OTPnumber2 = ref()
const OTPnumber3 = ref()
const OTPnumber4 = ref()

definePageMeta({
    middleware : 'check-mobile-number'
})

const verification = async () => {

    // create object for the API requerest body
    const createUserApiBody = {
        "mobile_number": collectionstore.mobileNumber,
        "code": parseInt(OTPnumber1.value + OTPnumber2.value + OTPnumber3.value + OTPnumber4.value),
        }
    
    try{
        const response = await $fetch(
            `${config.public.url}/verification`, 
            {
                method : 'POST',
                body : createUserApiBody
            }
        )
        // success
        console.log('verification successfull')
        cookieStore.set('token', response.token)
        localStorage.removeItem('mobileNumber')
        collectionstore.mobileNumber = null
        setTimeout(() =>{
            navigateTo('/collection/add/infomations')
        }, 400)

    }catch(error){
        console.log(`this is the error ${error}`)
    }
}

// TODO: find the error and allow this functionality
// const resendcode = async () => {
//     OTPnumber1.value = null
//     OTPnumber2.value = null
//     OTPnumber3.value = null
//     OTPnumber4.value = null
    
//     try{
//         const response = await $fetch(gayashan.ran
//             `${config.public.url}/resendcode/${collectionstore.mobileNumber}`, 
//             {
//                 method : 'PATCH'
//             }
//         )
//         // success
//         console.log('code send successfully')
//     }catch(error){
//         console.log(`this is the error ${error.response._data}`)
//     }
// }

const newAccount = () => {
    localStorage.removeItem('mobileNumber')
    collectionstore.mobileNumber = null

    setTimeout(() => {
        navigateTo('/collection/add')
    },1000)
}

onMounted(() => {
    if(collectionstore.mobileNumber === null){
        collectionstore.mobileNumber = localStorage.getItem('mobileNumber')
    }
})

</script>