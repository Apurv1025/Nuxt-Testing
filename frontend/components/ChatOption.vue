<template>
    <div class="msgs">
    <UCard v-for="user in user_dets">
    <div style="display:flex">
<UAvatar :alt="user.name" size="xl" class="icon"/>
<div class="name">{{user.name}}</div>
<div class="time">
    {{user.time}}
</div>
</div>
<div style="padding-left:20%" class="chat">
   {{ user.from }} : {{user.last_chat}}
</div>
    </UCard>
    </div>
</template>

<style>
.icon{
    width:10%;
}
.name{
    padding-left: 35px;
    font-size: large;
    width: 80%;
    padding-top: 3px;
}
.time{
    width:10%;
    font-size: small;
    padding-top: 3px;
}
.chat{
    font-size: medium;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
.msgs{
    overflow: auto;
    height:100%
}
</style>

<script setup>
const user_dets=[{name:'apurv',from:'idk',last_chat:"hellosdfgasdbfudsavfghdfiushgiubhdsifbdsygfsdfbisfdbv",time:"12:36"},
{name:'asies',from:'asies',last_chat:"bye",time:"12:30"},
{name:'asies',from:'asies',last_chat:"bye",time:"12:30"},

]
</script>