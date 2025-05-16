<template>
    <div class="chatdesc">
    <UAvatar alt="user" size="xl" class="profpic"/>
    <div class="namail">
    {{ user_data.name }}({{ user_data.email }})
    </div>
    </div>
</template>

<style setup>
.chatdesc{
    display: flex;
    background-color: darkolivegreen;
    padding: 20px;
    width: 100%;
    margin:0 0 0 0;
    border-radius: 2px;
    height:100%
}
.namail{
    font-size: larger;
    text-align: center;
    padding: 4px;
    padding-left: 20px;
    color: black;
}
</style>

<script setup>
const user_data={name:'apurv',email:'ra@test.com'}
</script>