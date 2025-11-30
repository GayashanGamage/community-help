<template>
    <div class="">
        <Menubar></Menubar>
        <div class="flex flex-col justify-center items-center gap-12 w-7xl h-[90vh] py-4 px-2 mx-auto">
            <div class="border flex flex-col gap-4 p-4">
                <h4 class="text-center">Add collection point</h4>
                <div class="flex flex-col">
                    <div class="flex flex-col gap-2">
                        <label for="name">First Name</label>
                        <input id="name" type="text" class="border" placeholder="Nimesh waduge">
                    </div>
                    <div class="flex flex-col gap-2">
                        <label for="name">Mobile number</label>
                        <input type="text" class="border" placeholder="071 000 0000">
                    </div>
                </div>
                <button class="border" @click="router.push('/collection/add/otp')">Vefiry Mobile Number</button>
            </div>
        </div>
    </div>
</template>

<script setup>
const router = useRouter()
</script>