import { Routes, Route, BrowserRouter } from "react-router-dom"; 
import Layout from "./pages/Layout/Layout";
import Home from "./pages/Home/Home";
import About from "./pages/About/About";
import LandingPage from "./pages/Landing/Landing"; 

import './App.css';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage />} /> 

        <Route element={<Layout />}>
          <Route path="/home" element={<Home />} />
          <Route path="/about" element={<About />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
