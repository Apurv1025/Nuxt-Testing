<template>
    <div class="navbar">
      <NuxtLink to="/" class="profile"><UIcon name="mdi-light:account" class="size-10" /></NuxtLink>
      <UInput icon="i-lucide-search" placeholder="Search..." size="xl"  class="searchinp"/>
      <NuxtLink to="/profile" class="chat"><UIcon name="material-symbols-light:border-color" class="size-10" /></NuxtLink>
    </div>
</template>

<script setup lang="ts">
const value=ref('')
</script>

<style>
.searchinp{
  color: brown;
}
.chat{
    justify-content: flex-end;
    padding-left: 400px;
    color: azure
}
.navbar{
    display: flex;
    background-color: black;
    padding: 20px;
    width: 100%;
    margin:0 0 0 0;
    border-top: none;
}
.profile{
    color: azure;
}

</style>