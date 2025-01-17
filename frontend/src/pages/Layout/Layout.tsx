import NavBar from "../../components/NavBar/NavBar";

import { Outlet } from "react-router";

export default function Layout(){
    return(
        <>
            <NavBar/>
            <Outlet/>
        </>
    )
}