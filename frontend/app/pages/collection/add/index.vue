<template>
    <div class="">
        <Menubar></Menubar>
        <div class="flex flex-col justify-center items-center gap-12 w-7xl h-[90vh] py-4 px-2 mx-auto">
            <div class="card-outline-one flex flex-col gap-8 w-96">
                <h4 class="title-three text-center">Add collection point</h4>
                <div class="flex flex-col gap-6">
                    <div class="flex flex-col gap-2">
                        <label for="name" class="input-label-one">First Name</label>
                        <input id="name" type="text" class="input-one" placeholder="Nimesh waduge" spellcheck="false">
                    </div>
                    <div class="flex flex-col gap-2">
                        <label for="name" class="input-label-one">Mobile number</label>
                        <input type="text" class="input-one" placeholder="071 000 0000">
                    </div>
                </div>
                <button class="btn-three" @click="router.push('/collection/add/otp')">Vefiry Mobile Number</button>
            </div>
        </div>
    </div>
</template>
<script setup>
const router = useRouter()
</script>