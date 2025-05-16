import { Client, Account, ID, Databases, Storage } from "appwrite";

export function useAppwrite() {
  const config = useRuntimeConfig();

  const client = new Client();
  client
    .setEndpoint(config.public.appwriteEndpoint)
    .setProject(config.public.appwriteProject);

  const account = new Account(client);
  const databases = new Databases(client);
  const storage = new Storage(client);

  return {
    client,
    databases,
    storage,
    account,
    ID,
  };
}

export { ID } from "appwrite";
