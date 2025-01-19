import "./Terminal.css"

import AceEditor from "react-ace";
import "ace-builds/src-noconflict/mode-javascript";
import "ace-builds/src-noconflict/theme-xcode"; 
import "ace-builds/src-noconflict/theme-clouds_midnight"; 
import "ace-builds/src-noconflict/theme-github"; 
import "ace-builds/src-noconflict/theme-solarized_light"; 
import "ace-builds/src-noconflict/theme-solarized_dark"; 
import "ace-builds/src-noconflict/theme-dracula"; 

import { MdOutlineUploadFile } from "react-icons/md";

import { useState } from "react";

export default function Terminal(){
    const [theme, setTheme] = useState<string>("clouds_midnight"); 
    const [input, setInput] = useState<string>(`// type your code here!
my_var: string = "hello world!"`)

    const handleChangeTheme = (e: React.ChangeEvent<HTMLSelectElement>): void => {
        setTheme(e.target.value);
    }

    const handleChangeInput = (value: string): void => {
        setInput(value);
    }

    const handleGenerate = (): void => {
        console.log(input); 
    }

    return(
        <div id="terminal">
            <div className="terminal-btns-container">
                <div className="terminal-btns-misc">
                    <div className="terminal-btns-theme">
                        <p>THEME</p>
                        <select onChange={handleChangeTheme} className="terminal-theme-dropdown">
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
                            <MdOutlineUploadFile size={25} color="white"/>
                        </label>
                        <input id="file-upload" type="file" accept=".sqr"/>
                    </button>
                </div>
                <button className="terminal-generate-btn" onClick={handleGenerate}><p>Generate Lexemes</p></button>
            </div>

        
            <AceEditor
                mode="javascript"
                theme= {theme}
                name="editor"
                editorProps={{ $blockScrolling: true }}
                width="100%"
                height="75vh"
                fontSize={16}
                onChange={handleChangeInput}
                value={input}
            />
        </div>
    )
}