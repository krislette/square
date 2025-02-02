import Layout from "./pages/Layout/Layout";
import Home from "./pages/Home/Home";
import About from "./pages/About/About";

import { Routes, Route, BrowserRouter } from "react-router";

import './App.css';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout/>}>
          <Route path="/" element={<Home/>}/>
          <Route path="/about" element={<About/>}/>
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
