class LexicalError(Exception):
    """Custom exception for lexical analysis errors."""
    def __init__(self, character: str, line: int, column: int):
        self.character = character
        self.line = line
        self.column = column
        self.message = self._generate_error_message()
        super().__init__(self.message)
    
    def _generate_error_message(self) -> str:
        """Generate a detailed, helpful error message."""
        suggestions = {
            '"': "String literal parsing not implemented. Did you mean to use quotes?",
            "'": "Character literal parsing not implemented.",
            '`': "Raw string or template literal parsing not implemented.",
        }
        
        suggestion = suggestions.get(self.character, "")
        
        return (
            "\n" + "-" * 80 + "\n"
            f"Lexical Error: Unrecognized character '{self.character}'\n"
            f"Location: Line {self.line}, Column {self.column}\n"
            f"{suggestion}\n"
            "\nPossible actions:\n"
            "1. Check for typos or unexpected characters\n"
            "2. Make sure that the character is part of your language syntax\n"
            "3. Implement parsing for this character type"
            "\n" + "-" * 80
        )


class TokenizationError(Exception):
    """Custom exception for tokenization errors."""
    def __init__(self, character: str, line: int, column: int):
        self.token = character
        self.line = line
        self.column = column
        self.message = self._generate_error_message()
        super().__init__(self.message)
    
    def _generate_error_message(self) -> str:
        return f"Invalid token '{self.token}' at line {self.line}, column {self.column}"
