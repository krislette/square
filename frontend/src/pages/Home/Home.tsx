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

interface LexerResponse {
  status: string;
  tokens?: Lexeme[];
  error?: {
    type: string;
    message: string;
    details: {
      line: number;
      column: number;
      invalid_token: string;
    };
  };
}

export default function Home() {
  const [lexerResponse, setLexerResponse] = useState<LexerResponse | null>(
    null
  );

  const handleLexerResponse = (response: LexerResponse) => {
    setLexerResponse(response);
  };

  return (
    <main id="home-page">
      <Terminal getLexerResponse={handleLexerResponse} />
      <LexemeTable lexerResponse={lexerResponse} />
    </main>
  );
}
