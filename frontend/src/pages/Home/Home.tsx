import Terminal from "../../components/Terminal/Terminal";
import LexemeTable from "../../components/LexemeTable/LexemeTable";
import "./Home.css";

import { useState } from "react";

interface Lexeme {
  lexeme: string;
  token: string;
  line: number;
  column: number;
}

export default function Home() {
  const [lexemes, setLexemes] = useState<Lexeme[]>([]);

  const getLexemes = (input: Lexeme[]) => {
    setLexemes(input);
  };

  return (
    <main id="home-page">
      <Terminal getLexemes={getLexemes} />
      <LexemeTable lexemes={lexemes} />
    </main>
  );
}
