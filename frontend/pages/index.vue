<template>
  
  <div style="display: flex;">
  <div style="width: 30%;">
      <header style="height:80px"><Navbar/></header>
    <ChatOption/>
  </div>
  <div style="width:70%; "><header style="height:80px"><ChatDescription/></header>
    <Chats/>
    <footer style="position: fixed;bottom: 0; width:100%;">
      <ChatInput/>
    </footer>
  </div>
  </div>
</template>


