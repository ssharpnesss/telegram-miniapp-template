import { useEffect } from "react";
import { Route, Routes } from "react-router-dom";
import { tmaInit } from "./utils/tma";
import Home from "./pages/home";

const App = () => {
  useEffect(() => {
    tmaInit()
  }, [])
  
  return <>

    <Routes>
      <Route path="/" element={<Home/>}>
    </Routes>
    
  </>
}

export default App;