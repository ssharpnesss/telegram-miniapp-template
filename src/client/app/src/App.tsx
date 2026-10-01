import { useEffect, useState } from "react";
import { Route, Routes } from "react-router-dom";
import { tmaInit } from "./utils/tma";
import Home from "./pages/home";
import { UserContext } from "./context/UserContext";
import { useQuery } from "@tanstack/react-query";
import type { User } from "./interfaces/user";
import request from "./utils/api";

const App = () => {
  const [isTelegramReady, setIsTelegramReady] = useState(false);
  useEffect(() => {
    void tmaInit().then(() => setIsTelegramReady(true));
  }, [])

  const { data: user, isPending, isError } = useQuery({
    queryKey: ["user"],
    enabled: isTelegramReady,
    queryFn: async () => {
      return request("users/me");
    },
    select: (data) => data.data as User,
  });

  if (isPending) return <>Loading...</>
  if (isError) return <p role="alert">Не удалось загрузить пользователя. Проверьте подключение и откройте приложение заново.</p>
  if (!user) return <p role="alert">API не вернул данные пользователя.</p>
  
  return (
    <>
      <UserContext.Provider value={{user: user ?? null}}>
        <Routes>
          <Route path="/" element={<Home />} />
        </Routes>
      </UserContext.Provider>
    </>
  )
}

export default App;
