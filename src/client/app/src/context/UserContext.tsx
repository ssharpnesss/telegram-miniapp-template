import { createContext, useContext } from "react";
import type { User } from "../interfaces/user";

export const UserContext = createContext<{ user: User | null }>({ user: null });
export const useUser = () => useContext(UserContext);