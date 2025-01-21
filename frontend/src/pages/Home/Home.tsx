import Terminal from "../../components/Terminal/Terminal"
import LexemeTable from "../../components/LexemeTable/LexemeTable"
import "./Home.css"

import { useState } from "react"

export default function Home(){
    const mockLexemes = [
        { lexeme: "gender", token: "IDENTIFIER_TOKEN" },
        { lexeme: "=", token: "ASSIGNMENT_OP_TOKEN" },
        { lexeme: "int", token: "KW_INT_TOKEN" },
        { lexeme: "main", token: "RW_MAIN_TOKEN" },
        { lexeme: "(", token: "OPEN_PARENTHESIS_TOKEN" }
    ];

    const [lexemes, setLexemes] = useState(mockLexemes);


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