import os
import sys
import json
from typing import Dict, List, NoReturn

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.lexer.lexer import Lexer
from backend.lexer.tokens import Token
from backend.lexer.errors import LexicalError, TokenizationError


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
    type_width = 35
    lexeme_width = 60
    location_width = 20

    # Print header
    print("Tokens:")
    print("-" * 120)
    print(f"{'Type'.ljust(type_width)} {'Lexeme'.ljust(lexeme_width)} {'Location'.ljust(location_width)}")
    print("-" * 120)

    # Print each token
    for token in tokens:
        location = f"Line: {token.line}, Column: {token.column}"
        print(f"{token.token_type.name.ljust(type_width)} {token.lexeme.ljust(lexeme_width)} {location.ljust(location_width)}")

    print("-" * 120)


def get_tokens_as_json(tokens: List[Token], output_path: str) -> None:
    token_list = convert_tokens_to_dict(tokens)

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Write to JSON file
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(token_list, f, indent=4)


def tokenize_string(source_code: str) -> List[Dict]:
    try:
        # Tokenize the source code
        lexer: Lexer = Lexer(source_code)
        tokens: List[Token] = lexer.tokenize()
        return convert_tokens_to_dict(tokens)
    except LexicalError as e:
        # Convert LexicalError to TokenizationError
        raise TokenizationError(e.character, e.line, e.column)
    except Exception as e:
        # Convert other exceptions to a more general error (pass for now)
        pass


def convert_tokens_to_dict(tokens: List[Token]) -> List[Dict]:
    return [{
        "token": token.token_type.name,
        "lexeme": token.lexeme,
        "line": token.line,
        "column": token.column
    } for token in tokens]


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

    # Save tokens to JSON file
    output_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'backend',
        'output',
        'tokens.json'
    )

    get_tokens_as_json(tokens, output_path)
    print(f"\nTokens have been saved to: {output_path}")

    # Successful exit
    sys.exit(0)


if __name__ == "__main__":
    main()
