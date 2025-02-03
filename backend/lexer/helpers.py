
def isAlpha(char: str) -> bool:
    return ('A' <= char <= 'Z') or ('a' <= char <= 'z')

def isNum(char: str) -> bool:
    return '0' <= char <= '9'

def isSpace(char: str) -> bool:
    return char == ' '