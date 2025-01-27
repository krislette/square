import os
import sys
from typing import List, NoReturn

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.lexer.lexer import Lexer
from backend.lexer.tokens import Token


def read_source_file(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)


def print_tokens(tokens: List[Token]) -> None:
    if not tokens:
        print("No tokens found.")
        return

    # Define column widths
    type_width = 30
    lexeme_width = 60
    location_width = 20

    # Print header
    print("Tokens:")
    print("-" * 100)
    print(f"{'Type'.ljust(type_width)} {'Lexeme'.ljust(lexeme_width)} {'Location'.ljust(location_width)}")
    print("-" * 100)

    # Print each token
    for token in tokens:
        location = f"Line: {token.line}, Column: {token.column}"
        print(f"{token.token_type.name.ljust(type_width)} {token.lexeme.ljust(lexeme_width)} {location.ljust(location_width)}")

    print("-" * 100)


def main() -> NoReturn:
    if len(sys.argv) != 2:
        print("Usage: python main.py <source_file>")
        sys.exit(1)

    # Read the source file
    file_path: str = sys.argv[1]
    source_code: str = read_source_file(file_path)

    # Tokenize the source code
    lexer: Lexer = Lexer(source_code)
    tokens: List[Token] = lexer.tokenize()

    # Print the tokens
    print_tokens(tokens)

    # Successful exit
    sys.exit(0)


if __name__ == "__main__":
    main()
