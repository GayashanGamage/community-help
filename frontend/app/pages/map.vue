<template>
    <div class="">
        <Menubar></Menubar>
        <div class="max-w-7xl h-[90vh] relative mx-auto px-2">
            <LMap
                class="w-full h-full"
                :zoom="8.4"
                :center="[7.8731, 80.7718]"
                :use-global-leaflet="false"
            >
                <LTileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution="&amp;copy; <a href=&quot;https://www.openstreetmap.org/&quot;>OpenStreetMap</a> contributors"
                layer-type="base"
                name="OpenStreetMap"
                />
            </LMap>
        </div>
    </div>
</template>

<script setup>
</script>