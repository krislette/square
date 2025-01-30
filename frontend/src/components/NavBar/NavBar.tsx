import { NavLink, useLocation } from "react-router-dom";
import "./NavBar.css";

export default function NavBar() {
  const location = useLocation();

  return (
    <header id="navbar">
      <div className="navbar-title">
        <img src="sqr.png" alt="Square Logo" width={50} height={50} />
        <h1>Square</h1>
      </div>
      <nav className="navbar-tabs">
        <NavLink
          to="/home"
          className={location.pathname === "/" ? "active" : ""}
        >
          Terminal
        </NavLink>
      </nav>
    </header>
  );
}