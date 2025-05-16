import { defineStore } from "pinia";

export const useChatStore = defineStore("chatStore", {
  state: () => ({
    chats: [],
  }),
  actions: {},
  persist: {
    enabled: true,
    strategies: [
      {
        key: "chatStore",
        storage: localStorage,
      },
    ],
  },
});
