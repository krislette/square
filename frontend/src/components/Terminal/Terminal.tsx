import "./Terminal.css"
import AceEditor from "react-ace";

import "ace-builds/src-noconflict/mode-javascript";
import "ace-builds/src-noconflict/theme-xcode"; 

export default function Terminal(){
    return(
        <div>
            <div>
                <div>
                    <button>Theme</button>
                    <button>
                        <label htmlFor="file-upload" className="terminal-upload">
                            Upload
                        </label>
                        <input id="file-upload" type="file" accept=".sqr"/>
                    </button>
                </div>
                <button>Generate Lexemes</button>
            </div>

            <div>
                <AceEditor
                    mode="javascript"
                    theme="xcode"
                    name="editor"
                    editorProps={{ $blockScrolling: true }}
                    width="60%"
                    height="80vh"
                />
            </div>

        </div>
    )
}