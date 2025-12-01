<template>
    <div class="">
        <Menubar></Menubar>
        <div class="flex flex-col justify-center items-center gap-12 w-7xl h-[90vh] py-4 px-2 mx-auto">
            <div class="card-outline-one flex flex-col gap-7 w-96">
                <h4 class="title-three text-center">Check your messages</h4>
                <div class="flex flex-row justify-around">
                    <input type="text" class="input-two" maxlength="1" size="1" ref="otpNumOne" @keyup="otpNumTwo.focus()">
                    <input type="text" class="input-two" maxlength="1" size="1" ref="otpNumTwo" @keyup="otpNumThree.focus()">
                    <input type="text" class="input-two" maxlength="1" size="1" ref="otpNumThree" @keyup="otpNumFour.focus()">
                    <input type="text" class="input-two" maxlength="1" size="1" ref="otpNumFour">
                </div>
                <button class="btn-three w-full" @click="router.push('/collection/add/infomations')">Vefiry</button>
            </div>
        </div>
    </div>
</template>

<script setup>
const router = useRouter()

const otpNumOne = ref(null)
const otpNumTwo = ref(null)
const otpNumThree = ref(null)
const otpNumFour = ref(null)

</script>