from enum import Enum


class TokenType(Enum):
    # Identifiers
    IDENTIFIER_TOKEN = 'IDENTIFIER_TOKEN'

    # Literals
    STRING_LITERAL_TOKEN = 'STRING_LITERAL_TOKEN'
    INT_LITERAL_TOKEN = 'INT_LITERAL_TOKEN'
    FLOAT_LITERAL_TOKEN = 'FLOAT_LITERAL_TOKEN'

    # Keywords
    KW_BOOL_TOKEN = 'KW_BOOL_TOKEN'
    KW_CHAR_TOKEN = 'KW_CHAR_TOKEN'
    KW_CONST_TOKEN = 'KW_CONST_TOKEN'
    KW_DOUBLE_TOKEN = 'KW_DOUBLE_TOKEN'
    KW_EXIT_TOKEN = 'KW_EXIT_TOKEN'
    KW_FLOAT_TOKEN = 'KW_FLOAT_TOKEN'
    KW_GET_TOKEN = 'KW_GET_TOKEN'
    KW_INT_TOKEN = 'KW_INT_TOKEN'
    KW_LONG_TOKEN = 'KW_LONG_TOKEN'
    KW_LOOP_TOKEN = 'KW_LOOP_TOKEN'
    KW_MOD_TOKEN = 'KW_MOD_TOKEN'
    KW_PRINT_TOKEN = 'KW_PRINT_TOKEN'
    KW_RETURN_TOKEN = 'KW_RETURN_TOKEN'
    KW_SHORT_TOKEN = 'KW_SHORT_TOKEN'
    KW_SIGNED_TOKEN = 'KW_SIGNED_TOKEN'
    KW_SKIP_TOKEN = 'KW_SKIP_TOKEN'
    KW_STATIC_TOKEN = 'KW_STATIC_TOKEN'
    KW_UNSIGNED_TOKEN = 'KW_UNSIGNED_TOKEN'
    KW_VOID_TOKEN = 'KW_VOID_TOKEN'
    KW_WHEN_TOKEN = 'KW_WHEN_TOKEN'

    # Reserved Words
    RW_BOOL_TRUE_TOKEN = 'RW_BOOL_TRUE_TOKEN'
    RW_BOOL_FALSE_TOKEN = 'RW_BOOL_FALSE_TOKEN'
    RW_MAIN_TOKEN = 'RW_MAIN_TOKEN'

    # Noise Words
    NW_IN_TOKEN = 'NW_IN_TOKEN'

    # Operators
    OP_ASSIGNMENT_TOKEN = 'OP_ASSIGNMENT_TOKEN'
    OP_ADDITION_ASSIGNMENT_TOKEN = 'OP_ADDITION_ASSIGNMENT_TOKEN'
    OP_SUBTRACTION_ASSIGNMENT_TOKEN = 'OP_SUBTRACTION_ASSIGNMENT_TOKEN'
    OP_MULTIPLICATION_ASSIGNMENT_TOKEN = 'OP_MULTIPLICATION_ASSIGNMENT_TOKEN'
    OP_DIVISION_ASSIGNMENT_TOKEN = 'OP_DIVISION_ASSIGNMENT_TOKEN'
    OP_MODULUS_ASSIGNMENT_TOKEN = 'OP_MODULUS_ASSIGNMENT_TOKEN'

    OP_PLUS_TOKEN = 'OP_PLUS_TOKEN'
    OP_MINUS_TOKEN = 'OP_MINUS_TOKEN'
    OP_MULTIPLY_TOKEN = 'OP_MULTIPLY_TOKEN'
    OP_DIVIDE_TOKEN = 'OP_DIVIDE_TOKEN'
    OP_MODULO_TOKEN = 'OP_MODULO_TOKEN'
    OP_INT_DIVIDE_TOKEN = 'OP_INT_DIVIDE_TOKEN'
    OP_EXPONENT_TOKEN = 'OP_EXPONENT_TOKEN'

    OP_INCREMENT_TOKEN = 'OP_INCREMENT_TOKEN'
    OP_DECREMENT_TOKEN = 'OP_DECREMENT_TOKEN'

    OP_JUNCTION_OR_TOKEN = 'OP_JUNCTION_OR_TOKEN'
    OP_LOGICAL_OR_TOKEN = 'OP_LOGICAL_OR_TOKEN'
    OP_LOGICAL_AND_TOKEN = 'OP_LOGICAL_AND_TOKEN'
    OP_LOGICAL_NOT_TOKEN = 'OP_LOGICAL_NOT_TOKEN'

    OP_EQUAL_TOKEN = 'OP_EQUAL_TOKEN'
    OP_NOT_EQUAL_TOKEN = 'OP_NOT_EQUAL_TOKEN'
    OP_GREATER_THAN_TOKEN = 'OP_GREATER_THAN_TOKEN'
    OP_LESS_THAN_TOKEN = 'OP_LESS_THAN_TOKEN'
    OP_GREATER_THAN_OR_EQUAL_TOKEN = 'OP_GREATER_THAN_OR_EQUAL_TOKEN'
    OP_LESS_THAN_OR_EQUAL_TOKEN = 'OP_LESS_THAN_OR_EQUAL_TOKEN'

    # Delimiters
    DELIMITER_TOKEN = 'DELIMITER_TOKEN'

    # Brackets
    OPEN_SQUARE_TOKEN = 'OPEN_SQUARE_TOKEN'
    CLOSE_SQUARE_TOKEN = 'CLOSE_SQUARE_TOKEN'
    OPEN_PARENTHESIS_TOKEN = 'OPEN_PARENTHESIS_TOKEN'
    CLOSE_PARENTHESIS_TOKEN = 'CLOSE_PARENTHESIS_TOKEN'

    # Comments
    SINGLE_COMMENT_TOKEN = 'SINGLE_COMMENT_TOKEN'
    MULTI_COMMENT_TOKEN = 'MULTI_COMMENT_TOKEN'

    # Miscellaneous
    SCOPE_RESOLUTION_TOKEN = 'SCOPE_RESOLUTION_TOKEN'
    ATTRIBUTE_ACCESS_TOKEN = 'ATTRIBUTE_ACCESS_TOKEN'
    FUNCTION_TYPE_ASSIGNMENT_TOKEN = 'FUNCTION_TYPE_ASSIGNMENT_TOKEN'


class Token:
    def __init__(self, type: TokenType, value: str = None):
        self.type = type
        self.value = value

    def __repr__(self):
        return f'{self.type.name}: {self.value}' if self.value else f'{self.type.name}'
