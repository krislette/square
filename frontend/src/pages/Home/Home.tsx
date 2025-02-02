import Terminal from "../../components/Terminal/Terminal";
import LexemeTable from "../../components/LexemeTable/LexemeTable";
import "./Home.css";

import { useState, useEffect } from "react";

interface Lexeme {
    lexeme: string;
    token: string;
}

export default function Home(){

    const [lexemes, setLexemes] = useState<Lexeme[]>([]);

    const getLexemes = (input: Lexeme[]) => {
        setLexemes(input)
    }

  const getLexemes = (input: string) => {
    console.log(input);
    // processing here
  };

  return (
    <main id="home-page">
      <Terminal getLexemes={getLexemes} />
      <LexemeTable lexemes={lexemes} />
    </main>
  );
}