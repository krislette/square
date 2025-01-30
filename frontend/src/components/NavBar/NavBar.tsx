import { NavLink, useLocation } from "react-router-dom"
import { FaRegSquare } from "react-icons/fa";
import "./NavBar.css"

export default function NavBar(){
    const location = useLocation();

    return(
        <header id="navbar">
            <div className="navbar-title">
                <FaRegSquare size={50} />
                <h1>Square</h1>
            </div>
            <nav className="navbar-tabs">
                <NavLink 
                    to="/home" 
                    className={location.pathname == "/" ? "active" : ""}>
                    Terminal
                </NavLink>
                <NavLink 
                    to="/about" 
                    className={location.pathname == "/about" ? "active" : ""}>
                    About
                </NavLink>
            </nav>
        </header>
    )
}