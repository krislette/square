import { NavLink } from "react-router-dom";
import "./NavBar.css";

export default function NavBar() {

  return (
    <header id="navbar">
      <NavLink
        to="/"
        className={({ isActive }) => (isActive ? "navbar-title active" : "navbar-title")}
      >
        <img src="sqr.png" alt="Square Logo" width={50} height={50} />
        <h1>Square</h1>
      </NavLink>
      <nav className="navbar-tabs">
        <NavLink
          to="/home"
          className={({ isActive }) => (isActive ? "active" : "")}
        >
          Terminal
        </NavLink>
      </nav>
    </header>
  );
}