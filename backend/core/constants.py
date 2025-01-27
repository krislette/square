from backend.lexer.tokens import TokenType


# Keyword Mapping
KEYWORDS: dict[str, TokenType] = {
    # Type Keywords
    "bool": TokenType.KW_BOOL_TOKEN,
    "char": TokenType.KW_CHAR_TOKEN,
    "const": TokenType.KW_CONST_TOKEN,
    "double": TokenType.KW_DOUBLE_TOKEN,
    "float": TokenType.KW_FLOAT_TOKEN,
    "int": TokenType.KW_INT_TOKEN,
    "long": TokenType.KW_LONG_TOKEN,
    "short": TokenType.KW_SHORT_TOKEN,
    "signed": TokenType.KW_SIGNED_TOKEN,
    "str": TokenType.KW_STRING_TOKEN,
    "unsigned": TokenType.KW_UNSIGNED_TOKEN,
    "void": TokenType.KW_VOID_TOKEN,

    # Control Flow Keywords
    "exit": TokenType.KW_EXIT_TOKEN,
    "loop": TokenType.KW_LOOP_TOKEN,
    "mod": TokenType.KW_MOD_TOKEN,
    "return": TokenType.KW_RETURN_TOKEN,
    "skip": TokenType.KW_SKIP_TOKEN,
    "static": TokenType.KW_STATIC_TOKEN,
    "when": TokenType.KW_WHEN_TOKEN,
    "get": TokenType.KW_GET_TOKEN,

    # Function Keywords
    "print": TokenType.KW_PRINT_TOKEN,
    "range": TokenType.KW_RANGE_TOKEN,
    "fun": TokenType.FUNCTION_TOKEN,

    # Reserved Words
    "true": TokenType.RW_BOOL_TRUE_TOKEN,
    "false": TokenType.RW_BOOL_FALSE_TOKEN,
    "main": TokenType.RW_MAIN_TOKEN,

    # Noise Words
    "in": TokenType.NW_IN_TOKEN
}

# Operator Mapping
OPERATORS: dict[str, TokenType] = {
    # Assignment Operators
    "=": TokenType.OP_ASSIGNMENT_TOKEN,
    "+=": TokenType.OP_ADDITION_ASSIGNMENT_TOKEN,
    "-=": TokenType.OP_SUBTRACTION_ASSIGNMENT_TOKEN,
    "*=": TokenType.OP_MULTIPLICATION_ASSIGNMENT_TOKEN,
    "/=": TokenType.OP_DIVISION_ASSIGNMENT_TOKEN,
    "%=": TokenType.OP_MODULUS_ASSIGNMENT_TOKEN,

    # Arithmetic Operators
    "+": TokenType.OP_PLUS_TOKEN,
    "-": TokenType.OP_MINUS_TOKEN,
    "*": TokenType.OP_MULTIPLY_TOKEN,
    "/": TokenType.OP_DIVIDE_TOKEN,
    "%": TokenType.OP_MODULO_TOKEN,
    "//": TokenType.OP_INT_DIVIDE_TOKEN,
    "**": TokenType.OP_EXPONENT_TOKEN,
    "~/": TokenType.OP_INT_DIVIDE_TOKEN,

    # Attribute Access Operator
    ".": TokenType.ATTRIBUTE_ACCESS_TOKEN,

    # Function Type Assignment Operator
    "->": TokenType.FUNCTION_TYPE_ASSIGNMENT_TOKEN,

    # Increment/Decrement
    "++": TokenType.OP_INCREMENT_TOKEN,
    "--": TokenType.OP_DECREMENT_TOKEN,

    # Logical Operators
    "|": TokenType.OP_JUNCTION_OR_TOKEN,
    "||": TokenType.OP_LOGICAL_OR_TOKEN,
    "&&": TokenType.OP_LOGICAL_AND_TOKEN,
    "not": TokenType.OP_LOGICAL_NOT_TOKEN,

    # Comparison Operators
    "==": TokenType.OP_EQUAL_TOKEN,
    "!=": TokenType.OP_NOT_EQUAL_TOKEN,
    ">": TokenType.OP_GREATER_THAN_TOKEN,
    "<": TokenType.OP_LESS_THAN_TOKEN,
    ">=": TokenType.OP_GREATER_THAN_OR_EQUAL_TOKEN,
    "<=": TokenType.OP_LESS_THAN_OR_EQUAL_TOKEN
}

# Delimiter and Bracket Mapping
DELIMITERS: dict[str, TokenType] = {
    "[": TokenType.OPEN_SQUARE_TOKEN,
    "]": TokenType.CLOSE_SQUARE_TOKEN,
    "(": TokenType.OPEN_PARENTHESIS_TOKEN,
    ")": TokenType.CLOSE_PARENTHESIS_TOKEN,
    ".": TokenType.DELIMITER_TOKEN,
    ",": TokenType.COMMA_TOKEN,
    ":": TokenType.DATA_TYPE_ASSIGNMENT_TOKEN,
    "::": TokenType.SCOPE_RESOLUTION_TOKEN,
}

MISCELLANEOUS: dict[str, TokenType] = {
    ".": TokenType.ATTRIBUTE_ACCESS_TOKEN,
    "->": TokenType.FUNCTION_TYPE_ASSIGNMENT_TOKEN,
}
