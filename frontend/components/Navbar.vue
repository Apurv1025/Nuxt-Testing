<template>
    <div class="navbar">
      <NuxtLink to="/profile" class="profile" as="button"><UIcon name="mdi-light:account" size="40px" /></NuxtLink>
      <UModal>
    <UButton
      label="Search users..."
      color="neutral"
      variant="subtle"
      icon="i-lucide-search"
    />

    <template #content>
      <UCommandPalette
        v-model:search-term="searchTerm"
        :loading="status === 'pending'"
        :groups="groups"
        placeholder="Search users..."
        class="h-80"
      />
    </template>
  </UModal>
    </div>
</template>


<script setup lang="ts">
const searchTerm = ref('')

const { data: users, status } = await useFetch('https://jsonplaceholder.typicode.com/users', {
  key: 'command-palette-users',
  params: { q: searchTerm },
  transform: (data: { id: number, name: string, email: string }[]) => {
    return data?.map(user => ({ id: user.id, label: user.name, suffix: user.email, avatar: { src: `https://i.pravatar.cc/120?img=${user.id}` } })) || []
  },
  lazy: true
})

const groups = computed(() => [{
  id: 'users',
  label: searchTerm.value ? `Users matching “${searchTerm.value}”...` : 'Users',
  items: users.value || [],
  ignoreFilter: true
}])
</script>

<style>
.navbar{
    display: flex;
    background-color: black;
    padding: 20px;
    width: 100%;
    height:100%
}
.profile{
    color: azure;
    padding-right: 100px;
    
}

</style>