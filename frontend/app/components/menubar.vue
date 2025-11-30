<template>
    <div class="flex flex-col gap-3 w-7xl h-auto py-4 px-2 mx-auto">
        <div class="flex flex-row justify-between ">
            <h1 class="font-black text-2xl" @click="router.push('/')">Community Kitchen</h1>
            <button class="border py-2 px-4 rounded-md border-gray-300 hover:bg-black hover:text-white hover:border-black" @click="direct">Add collection Point</button>
        </div>
        <hr class="border-gray-300 shadow-sm">
    </div>
</template>

<script setup>

const router = useRouter()

const direct = () => {
    router.push('/list')
}

</script>