import { Client, Account, ID } from "appwrite";

export function useAppwrite() {
  const config = useRuntimeConfig();

  const client = new Client();
  client
    .setEndpoint(config.public.appwriteEndpoint)
    .setProject(config.public.appwriteProject);

  const account = new Account(client);

  return {
    client,
    account,
    ID,
  };
}

export { ID } from "appwrite";
