import Terminal from "../../components/Terminal/Terminal"
import LexemeTable from "../../components/LexemeTable/LexemeTable"
import "./Home.css"

import { useState } from "react"

export default function Home(){
    const [lexemes, setLexemes] = useState(null); 

    const getLexemes = (input: string) => {
        console.log(input)
        // processing here
    }

    return(
        <main id="home-page">
            <Terminal getLexemes={getLexemes}/>
            <LexemeTable lexemes={lexemes}/>
        </main>
    )
}