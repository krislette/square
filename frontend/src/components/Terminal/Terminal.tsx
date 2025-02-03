import "./Terminal.css";
import AceEditor from "react-ace";
import "./mode-square";
import "ace-builds/src-noconflict/theme-xcode";
import "ace-builds/src-noconflict/theme-clouds_midnight";
import "ace-builds/src-noconflict/theme-github";
import "ace-builds/src-noconflict/theme-solarized_light";
import "ace-builds/src-noconflict/theme-solarized_dark";
import "ace-builds/src-noconflict/theme-dracula";
import { MdOutlineUploadFile } from "react-icons/md";
import { useState } from "react";

interface TerminalProps {
  getLexerResponse: (response: LexerResponse) => void;
}

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

export default function Terminal({ getLexerResponse }: TerminalProps) {
  const [theme, setTheme] = useState<string>("clouds_midnight");
  const [input, setInput] = useState<string>(`# Type your code here!
my_var: str = "hello world!".
print(my_var).`);
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const handleChangeTheme = (e: React.ChangeEvent<HTMLSelectElement>): void => {
    setTheme(e.target.value);
  };

  const handleChangeInput = (value: string): void => {
    setInput(value);
  };

  const handleGenerate = async (): Promise<void> => {
    try {
      setIsLoading(true);

      const response = await fetch(import.meta.env.VITE_API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          code: input,
        }),
      });

      const data = await response.json();
      console.log("Received response: ", data);
      getLexerResponse(data);
    } catch (error) {
      console.error("Error:", error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleUpload = (event: React.ChangeEvent<HTMLInputElement>): void => {
    const file = event.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        const text = e.target?.result as string;
        setInput(text);
      };
      reader.readAsText(file);
    }
  };

  return (
    <div id="terminal">
      <div className="terminal-btns-container">
        <div className="terminal-btns-misc">
          <div className="terminal-btns-theme">
            <p>THEME</p>
            <select
              onChange={handleChangeTheme}
              className="terminal-theme-dropdown"
            >
              <optgroup label="Dark Themes">
                <option value="clouds_midnight">Clouds Midnight</option>
                <option value="dracula">Dracula</option>
                <option value="solarized_dark">Solarized Dark</option>
              </optgroup>
              <optgroup label="Light Themes">
                <option value="xcode">Xcode</option>
                <option value="github">Github</option>
                <option value="solarized_light">Solarized Light</option>
              </optgroup>
            </select>
          </div>
          <button className="terminal-btns-upload">
            <label htmlFor="file-upload" className="terminal-upload">
              <MdOutlineUploadFile size={25} color="white" />
            </label>
            <input
              id="file-upload"
              type="file"
              accept=".sqr"
              onChange={handleUpload}
            />
          </button>
        </div>
        <button
          className="terminal-generate-btn"
          onClick={handleGenerate}
          disabled={isLoading}
        >
          <p>{isLoading ? "Generating..." : "Generate Lexemes"}</p>
        </button>
      </div>

      <AceEditor
        mode="typescript"
        theme={theme}
        name="editor"
        editorProps={{ $blockScrolling: true }}
        width="100%"
        height="74vh"
        fontSize={16}
        onChange={handleChangeInput}
        value={input}
      />
    </div>
  );
}