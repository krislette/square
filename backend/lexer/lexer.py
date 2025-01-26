from backend.lexer.tokens import Token, TokenType
from backend.lexer.errors import LexicalError
from backend.core.constants import KEYWORDS, OPERATORS, DELIMITERS
from typing import List, Optional

class Lexer:
    """
    Note: This class imitates an automaton by moving
    through states and checking those sequence of states.
    """
    def __init__(self, source_code: str) -> None:
        self.source: List[str] = list(source_code)
        self.tokens: List[Token] = []
        self.line: int = 1
        self.column: int = 1
        self.current_pos: int = 0

    def _peek(self, offset: int = 1) -> str:
        """Look ahead in the source code without consuming characters.

        This is used to check the next character(s) without advancing the state.

        Args:
            offset (int): The number of characters to look ahead.

        Returns:
            str: The character at the offset position, or an empty string if out of bounds.
        """
        if self.current_pos + offset < len(self.source):
            return self.source[self.current_pos + offset]
        return ''

    def _advance(self) -> Optional[str]:
        """Consume and return the current character.

        This advances the lexer's state to the next character in the input.

        Returns:
            Optional[str]: The current character, or None if the end of the source is reached.
        """
        if self.current_pos >= len(self.source):
            return None
        
        # Get the current character and move the position forward
        char: str = self.source[self.current_pos]
        self.current_pos += 1
        self.column += 1
        
        # Update line and column tracking if a newline is encountered
        if char == '\n':
            self.line += 1
            self.column = 1

        return char

    def _match(self, expected: str) -> bool:
        """Check if the next character matches the expected character.
        
        If it matches, the lexer advances to the next state by consuming the character.
        
        Args:
            expected (str): The character to match.
        
        Returns:
            bool: True if the next character matches, False otherwise.
        """
        if self.current_pos >= len(self.source):
            return False
        if self.source[self.current_pos] != expected:
            return False
        self._advance()

        return True

    def tokenize(self) -> List[Token]:
        """Tokenize the entire source code.

        This is the main loop of the lexer that processes the input character by character
        and transitions between states based on the current character.

        Returns:
            List[Token]: A list of tokens generated from the source code.
        """
        while self.current_pos < len(self.source):
            current: str = self.source[self.current_pos]

            # State: Operator
            # Transition to operator tokenization if the current character is a potential operator
            if current in '+-*/<>=!':
                self._tokenize_operator()

            # State: Number
            # Transition to number tokenization if the current character is a digit
            elif current.isdigit():
                self._tokenize_number()

            # State: Identifier or Keyword
            # Transition to identifier tokenization if the current character is a letter or underscore
            elif current.isalpha() or current == '_':
                self._tokenize_identifier()
            
            # State: Whitespace
            # Transition to the next character if the current character is whitespace
            elif current.isspace():
                self._advance()

            # State: String Literal
            elif current == '"':
                self._tokenize_string()

            # State: Delimiter
            # Transition to delimiter tokenization if the current character is a delimiter
            elif current in '()[].:,':
                self._tokenize_delimiter()

            else:
                # State: Error
                # If no valid transition is found, raise a lexical error
                raise LexicalError(current, self.line, self.column)

        return self.tokens

    def _tokenize_operator(self) -> None:
        """Tokenize operators, including multi-character operators.

        This method handles the state transitions for operators, which can be single-character
        (e.g., '+', '-') or multi-character (e.g., '==', '!=', '++').
        """
        line: int = self.line
        column: int = self.column

        # Peek at the current and next character without advancing
        current: str = self.source[self.current_pos]
        next_char: str = self._peek()

        # Check if the current and next characters form a valid multi-character operator
        if current + next_char in OPERATORS:
            # Found a multi-character operator
            self._advance()  # Consume the first character
            self._advance()  # Consume the second character
            self.tokens.append(Token(OPERATORS[current + next_char], current + next_char, line, column))
            return

        # Check if the current character is a valid single-character operator
        if current in OPERATORS:
            self._advance()  # Consume the single character
            self.tokens.append(Token(OPERATORS[current], current, line, column))
            return

        # Unrecognized operator error
        raise ValueError(f"Unrecognized operator: {current}")

    def _tokenize_number(self) -> None:
        """Tokenize numbers, including integers and floating-point numbers.

        This method handles the state transitions for numbers, which can be integers or
        floating-point numbers.
        """
        line: int = self.line
        column: int = self.column
        number: str = ""

        # State: Integer part
        # Consume digits until a non-digit character is encountered
        while self.current_pos < len(self.source) and self.source[self.current_pos].isdigit():
            char: Optional[str] = self._advance()
            if char is not None:
                number += char
        
        # State: Floating-point part
        # Check if the next character is a decimal point followed by digits
        if self._peek() == '.' and self.current_pos + 1 < len(self.source) and self.source[self.current_pos + 1].isdigit():
            # Consume the decimal point
            number += self._advance()
            # Consume the fractional digits.
            while self.current_pos < len(self.source) and self.source[self.current_pos].isdigit():
                char = self._advance()
                if char is not None:
                    number += char
            self.tokens.append(Token(TokenType.FLOAT_LITERAL_TOKEN, number, line, column))
        else:
            # State: Integer
            # If no decimal point is found, treat the number as an integer
            self.tokens.append(Token(TokenType.INT_LITERAL_TOKEN, number, line, column))

    def _tokenize_identifier(self) -> None:
        """Tokenize identifiers and keywords.

        This method handles the state transitions for identifiers, which can be variable names
        or reserved keywords.
        """
        line: int = self.line
        column: int = self.column
        identifier: str = ""

        # State: Identifier
        # Consume alphanumeric characters and underscores
        while self.current_pos < len(self.source) and (self.source[self.current_pos].isalnum() or self.source[self.current_pos] == '_'):
            char: Optional[str] = self._advance()
            if char is not None:
                identifier += char

        # State: Keyword or Identifier
        # Check if the identifier is a reserved keyword
        token_type: TokenType = KEYWORDS.get(identifier, TokenType.IDENTIFIER_TOKEN)
        self.tokens.append(Token(token_type, identifier, line, column))

    def _tokenize_string(self) -> None:
        """Tokenize string literals enclosed in quotes."""
        line: int = self.line
        column: int = self.column

        # Consume the opening quote
        opening_quote: Optional[str] = self._advance()
        if opening_quote not in ['"', "'"]:
            raise ValueError(f"Unexpected character {opening_quote} when expecting a string literal.")

        # Accumulate the characters inside the string
        string_value = []
        while True:
            current: Optional[str] = self._advance()

            # End of file before closing the quote
            if current is None:
                raise ValueError("Unterminated string literal.")

            # Closing quote ends the string
            if current == opening_quote:
                break

            else:
                # Regular character
                string_value.append(current)

        # Combine characters into a full string
        full_string = ''.join(string_value)

        # Add token with the string literal value
        self.tokens.append(Token(TokenType.STRING_LITERAL_TOKEN, full_string, line, column))

    def _tokenize_delimiter(self) -> None:
        """Tokenize delimiters.

        This method handles the state transitions for delimiters, which can be single-character
        or multi-character.
        """
        line: int = self.line
        column: int = self.column

        # Peek at the current and next character without advancing
        current: str = self.source[self.current_pos]
        next_char: str = self._peek()

        if current == ':' and next_char == ':':
            # Found a scope resolution token '::'
            self._advance()  # Consume the first ':'
            self._advance()  # Consume the second ':'
            self.tokens.append(Token(TokenType.SCOPE_RESOLUTION_TOKEN, '::', line, column))
            return

        if current == ':':
            # Single ':' token
            self._advance()  # Consume the ':'
            self.tokens.append(Token(TokenType.DATA_TYPE_ASSIGNMENT_TOKEN, ':', line, column))
            return

        # Handle other delimiters if necessary
        if current in DELIMITERS:
            self._advance()  # Consume the single delimiter
            self.tokens.append(Token(DELIMITERS[current], current, line, column))
            return

        # Unrecognized delimiter error
        raise ValueError(f"Unrecognized delimiter: {current}")
