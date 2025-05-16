import { defineStore } from "pinia";

const { account } = useAppwrite();

export const useAuthStore = defineStore(
  "authStore",
  {
    state: () => ({
      user: null,
      session: null,
    }),
    actions: {
      async createUserSession(userId, secret) {
        this.session = await account.createSession(userId, secret);
        this.user = await account.get();
      },
      async deleteUserSession() {
        await account.deleteSession("current");
        this.session = null;
        this.user = null;
      },
      async updateUserName(name) {
        this.user = await account.updateName(name);
      }
    },
    persist: true
  },
);
