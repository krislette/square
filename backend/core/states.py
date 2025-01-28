from enum import Enum, auto


class State(Enum):
    START = auto()          # Initial state
    OPERATOR = auto()       # Processing operators
    NUMBER = auto()         # Processing numbers
    IDENTIFIER = auto()     # Processing identifiers/keywords
    STRING = auto()         # Processing string literals
    DELIMITER = auto()      # Processing delimiters
    WHITESPACE = auto()     # Skipping whitespace
    ERROR = auto()          # Error state
