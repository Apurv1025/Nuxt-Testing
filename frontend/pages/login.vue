<script setup>
const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()

// In a Vue component or page
const { account, ID } = useAppwrite();

const config = useRuntimeConfig();

const userId = route.query?.userId
const secret = route.query?.secret

if (secret && userId) {
    if (authStore.user?.name) {
        router.push({ path: "/" })
    }
    await authStore.createUserSession(userId, secret);
    console.info('User session created:', authStore.user);
} else {
    console.info('No secret or userId provided in the URL');
}

const email = ref('');
const name = ref('');
const token = ref(null);

const login = async (email) => {
    token.value = await account.createMagicURLToken(
        ID.unique(),
        email,
        config.public.appUrl + '/login', // redirect URL
    );
    console.log(token);
};

const updateNameAndRedirect = async (name) => {
    await authStore.updateUserName(name);
    router.push({ path: "/" });
};

</script>

<template>
    <UCard variant="subtle" class="w-128 mx-auto mt-64 flex flex-col gap-4">
        <p class="text-center text-2xl font-bold mb-8">
            {{ !authStore.user ? 'Log in or create an account' : authStore.user?.name ? `Welcome!!!
            ${authStore.user?.name}` : 'Add a Name' }}
        </p>

        <form v-show="!authStore.user" class="flex flex-col gap-8 align-center-safe" @submit.prevent
            @submit="login(email)">
            <UInput v-model="email" :disabled="token" required trailing-icon="i-lucide-at-sign"
                placeholder="Enter your email" size="xl" type="email" />
            <UButton :loading="token" type="submit" class="ml-42 w-32 font-bold" size="xl" block="true">
                Login</UButton>
        </form>

        <UAlert v-show="token" class="mt-8" color="success" variant="subtle" title="Email Sent!"
            description="You can now login using the link you have received in your email inbox."
            icon="i-lucide-mail" />

        <form v-if="authStore.user !== null && !authStore.user?.name" class="flex flex-col gap-8 align-center-safe mb-8"
            @submit.prevent @submit="updateNameAndRedirect(name)">
            <UInput v-model="name" required trailing-icon="i-lucide-a-large-small" placeholder="Enter your name"
                size="xl" />
            <UButton loading-auto type="submit" color="neutral" class="ml-42 w-32 font-bold" size="xl" block>
                Add Name</UButton>
        </form>

        <UButton v-if="authStore.user?.name" type="button" color="error" variant="outline" block="true"
            class="ml-42 w-32 font-bold" size="xl" @click="authStore.deleteUserSession()">
            Logout
        </UButton>
    </UCard>
</template>
