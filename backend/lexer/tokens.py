from enum import Enum, auto
from dataclasses import dataclass


class TokenType(Enum):
    # Identifiers
    IDENTIFIER_TOKEN = auto()

    # Literals
    STRING_LITERAL_TOKEN = auto()
    COMMENT_TOKEN = auto()
    INT_LITERAL_TOKEN = auto()
    FLOAT_LITERAL_TOKEN = auto()

    # Keywords
    KW_BOOL_TOKEN = auto()
    KW_CHAR_TOKEN = auto()
    KW_CONST_TOKEN = auto()
    KW_DOUBLE_TOKEN = auto()
    KW_EXIT_TOKEN = auto()
    KW_FLOAT_TOKEN = auto()
    KW_GET_TOKEN = auto()
    KW_INT_TOKEN = auto()
    KW_LONG_TOKEN = auto()
    KW_LOOP_TOKEN = auto()
    KW_MOD_TOKEN = auto()
    KW_PRINT_TOKEN = auto()
    KW_RANGE_TOKEN = auto()
    KW_RETURN_TOKEN = auto()
    KW_SHORT_TOKEN = auto()
    KW_SIGNED_TOKEN = auto()
    KW_SKIP_TOKEN = auto()
    KW_STATIC_TOKEN = auto()
    KW_STRING_TOKEN = auto()
    KW_UNSIGNED_TOKEN = auto()
    KW_VOID_TOKEN = auto()
    KW_WHEN_TOKEN = auto()

    # Reserved Words
    RW_BOOL_TRUE_TOKEN = auto()
    RW_BOOL_FALSE_TOKEN = auto()
    RW_MAIN_TOKEN = auto()

    # Noise Words
    NW_IN_TOKEN = auto()

    # Operators
    OP_ASSIGNMENT_TOKEN = auto()
    OP_ADDITION_ASSIGNMENT_TOKEN = auto()
    OP_SUBTRACTION_ASSIGNMENT_TOKEN = auto()
    OP_MULTIPLICATION_ASSIGNMENT_TOKEN = auto()
    OP_DIVISION_ASSIGNMENT_TOKEN = auto()
    OP_MODULUS_ASSIGNMENT_TOKEN = auto()

    OP_PLUS_TOKEN = auto()
    OP_MINUS_TOKEN = auto()
    OP_MULTIPLY_TOKEN = auto()
    OP_DIVIDE_TOKEN = auto()
    OP_MODULO_TOKEN = auto()
    OP_INT_DIVIDE_TOKEN = auto()
    OP_EXPONENT_TOKEN = auto()

    OP_INCREMENT_TOKEN = auto()
    OP_DECREMENT_TOKEN = auto()

    OP_JUNCTION_OR_TOKEN = auto()
    OP_LOGICAL_OR_TOKEN = auto()
    OP_LOGICAL_AND_TOKEN = auto()
    OP_LOGICAL_NOT_TOKEN = auto()

    OP_EQUAL_TOKEN = auto()
    OP_NOT_EQUAL_TOKEN = auto()
    OP_GREATER_THAN_TOKEN = auto()
    OP_LESS_THAN_TOKEN = auto()
    OP_GREATER_THAN_OR_EQUAL_TOKEN = auto()
    OP_LESS_THAN_OR_EQUAL_TOKEN = auto()

    # Delimiters
    DELIMITER_TOKEN = auto()
    COMMA_TOKEN = auto()

    # Brackets
    OPEN_SQUARE_TOKEN = auto()
    CLOSE_SQUARE_TOKEN = auto()
    OPEN_PARENTHESIS_TOKEN = auto()
    CLOSE_PARENTHESIS_TOKEN = auto()

    # Miscellaneous
    SCOPE_RESOLUTION_TOKEN = auto()
    ATTRIBUTE_ACCESS_TOKEN = auto()
    FUNCTION_TYPE_ASSIGNMENT_TOKEN = auto()
    DATA_TYPE_ASSIGNMENT_TOKEN = auto()
    SINGLE_COMMENT_TOKEN = auto()
    MULTI_COMMENT_TOKEN = auto()


@dataclass
class Token:
    token_type: TokenType
    lexeme: str
    line: int = 1
    column: int = 1

    def __init__(self, token_type: TokenType, lexeme: str, line: int = 1, column: int = 1):
        """
        Initialize a Token instance.
        
        Args:
            token_type (TokenType): The type of the token
            lexeme (str): The actual text of the token
            line (int, optional): Line number. Defaults to 1.
            column (int, optional): Column number. Defaults to 1.
        """
        self.token_type = token_type
        self.lexeme = lexeme
        self.line = line
        self.column = column
