import Layout from "./pages/Layout/Layout";
import Terminal from "./pages/Terminal/Terminal";
import About from "./pages/About/About";

import { Routes, Route, BrowserRouter } from "react-router";

import './App.css';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout/>}>
          <Route path="/" element={<Terminal/>}/>
          <Route path="/about" element={<About/>}/>
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
