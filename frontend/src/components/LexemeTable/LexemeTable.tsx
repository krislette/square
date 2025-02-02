import './LexemeTable.css';

interface Lexeme {
    lexeme: string;
    token: string;
}

interface LexemeTableProps {
    lexemes: Lexeme[] | null;
}

export default function LexemeTable({ lexemes }: LexemeTableProps) {
    return (
        <div id="lexeme">
            {lexemes && lexemes.length > 0 ? (
                <div className="lexeme-table-container">
                    <div className="lex-table-head-container">
                        <table className="lexeme-table-head">
                            <thead>
                                <tr>
                                    <th className="th-lexeme">Lexeme</th>
                                    <th className="th-token">Token</th>
                                </tr>
                            </thead>
                        </table>
                    </div>
                    <div className="lex-table-body-container">
                        <table className="lexeme-table-body">
                            <tbody>
                                {lexemes.map((lexeme, index) => (
                                    <tr key={index}>
                                        <td className="td-lexeme">{lexeme.lexeme}</td>
                                        <td className="td-token">{lexeme.token}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </div>
            ) : (
                <p className="no-lexemes">No lexemes to display.</p>
            )}
        </div>
    );
}
