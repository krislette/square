import './LexemeTable.css';
import { useState } from 'react';

interface Lexeme {
    lexeme: string;
    token: string;
    line: number;
    column: number;
}

interface LexemeTableProps {
    lexemes: Lexeme[] | null;
}

// Define the list of tokens that belong to the MISCELLANEOUS category
const MISCELLANEOUS = [
    "SCOPE_RESOLUTION_TOKEN",
    "ATTRIBUTE_ACCESS_TOKEN",
    "FUNCTION_TYPE_ASSIGNMENT_TOKEN",
    "DATA_TYPE_ASSIGNMENT_TOKEN",
    "FUNCTION_TOKEN"
];

// Define the list of tokens that belong to the BRACKET category
const BRACKETS = [
    "OPEN_SQUARE_TOKEN",
    "CLOSE_SQUARE_TOKEN",
    "OPEN_PARENTHESIS_TOKEN",
    "CLOSE_PARENTHESIS_TOKEN"
];

export default function LexemeTable({ lexemes }: LexemeTableProps) {
    const [searchTerm, setSearchTerm] = useState<string>('');
    const [filterCategory, setFilterCategory] = useState<string>('');

    const filteredLexemes = lexemes?.filter(lexeme => {
        const matchesSearch = lexeme.lexeme.toLowerCase().includes(searchTerm.toLowerCase());

        let matchesCategory = true;
        if (filterCategory) {
            if (filterCategory === "OP_") {
                matchesCategory = lexeme.token.startsWith("OP_");
            } else if (filterCategory === "MISCELLANEOUS") {
                matchesCategory = MISCELLANEOUS.includes(lexeme.token);
            } else if (filterCategory === "BRACKET") {
                matchesCategory = BRACKETS.includes(lexeme.token);
            } else {
                matchesCategory = lexeme.token.includes(filterCategory);
            }
        }
        return matchesSearch && matchesCategory;
    });

    return (
        <div id="lexeme">
            <div className="lexeme-controls">
                <input
                    type="text"
                    placeholder="Search lexemes..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    className="lexeme-search"
                />
                <select
                    value={filterCategory}
                    onChange={(e) => setFilterCategory(e.target.value)}
                    className="lexeme-filter"
                >
                    <option value="">All Categories</option>
                    <option value="IDENTIFIER">Identifiers</option>
                    <option value="LITERAL">Literals</option>
                    <option value="KW">Keywords</option>
                    <option value="RW">Reserved Words</option>
                    <option value="NW">Noise Words</option>
                    <option value="OP_">Operators</option>
                    <option value="DELIMITER">Delimiters</option>
                    <option value="BRACKET">Brackets</option>
                    <option value="COMMENT">Comments</option>
                    <option value="MISCELLANEOUS">Miscellaneous</option>
                </select>
            </div>
            {filteredLexemes && filteredLexemes.length > 0 ? (
                <div className="lexeme-table-container">
                    <table className="lexeme-table">
                        <thead>
                            <tr>
                                <th className="th-lexeme">Lexeme</th>
                                <th className="th-token">Token</th>
                                <th className="th-line">Line</th>
                                <th className="th-column">Column</th>
                            </tr>
                        </thead>
                        <tbody>
                            {filteredLexemes.map((lexeme, index) => (
                                <tr key={index}>
                                    <td className="td-lexeme">{lexeme.lexeme}</td>
                                    <td className="td-token">
                                        <span className={`token-tag token-${lexeme.token.toLowerCase()}`}>
                                            {lexeme.token}
                                        </span>
                                    </td>
                                    <td className="td-line">{lexeme.line}</td>
                                    <td className="td-column">{lexeme.column}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            ) : (
                <p className="no-lexemes">No lexemes to display.</p>
            )}
        </div>
    );
}