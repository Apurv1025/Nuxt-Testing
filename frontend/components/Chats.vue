<template>
    <div v-for="content in contents">
    <div style="float:right" v-if="content.from === 'user1'">
    <UCard variant="subtle">
    <template #header>
      <div style="font-size: small;">{{content.from}}</div>
    </template>
    {{ content.content }}
    <template #footer>
    <div style="font-size: small;">{{content.time}}</div>
    </template>
  </UCard></div>

  <div style="float:left" v-if="content.from === 'user2'">
    <UCard variant="subtle">
    <template #header>
      <div style="font-size: small;">{{content.from}}</div>
    </template>
    {{ content.content }}
    <template #footer>
    <div style="font-size: small;">{{content.time}}</div>
    </template>
  </UCard></div></div>
</template>

<script setup>
const contents=[
    {from:"user1" , content:"hello bro!", time:"1234"},
    {from:"user2",content:"hi!", time:"5678"}
]
</script>