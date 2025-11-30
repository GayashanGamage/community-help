<template>
    <div class="">
        <Menubar></Menubar>
        <div class="flex flex-col justify-center items-center gap-12 w-7xl h-[90vh] py-4 px-2 mx-auto">
            <div class="border flex flex-col gap-4 p-4">
                <h4 class="text-center">Check your messages</h4>
                <div class="flex flex-row">
                    <input type="text" class="border" maxlength="1" size="1">
                    <input type="text" class="border" maxlength="1" size="1">
                    <input type="text" class="border" maxlength="1" size="1">
                    <input type="text" class="border" maxlength="1" size="1">
                </div>
                <button class="border" @click="router.push('/collection/add/infomations')">Vefiry</button>
            </div>
        </div>
    </div>
</template>

<script setup>
const router = useRouter()

</script>