<template>
    <div class="msg">
        <div class="inp">
    <UTextarea v-model="value" :rows="1" size="lg" variant="subtle"/></div>
    <div style="padding-left: 10px;">
     <UButton trailing-icon="i-lucide-arrow-right" color="neutral" size="lg">Send</UButton>
     </div>
    </div>
</template>

<style scoped>
.msg{
    background-color: darkolivegreen;
    display: flex;
    padding: 8px;
    border-radius: 2px ;
    justify-content: center;
    width: 70%;
}
</style>

<script setup lang="ts">
const value = ref('')
</script>