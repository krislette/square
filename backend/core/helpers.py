class CharacterClassifier:
    """
    Implements a Deterministic Finite Automaton (DFA) for character classification.
    """
    def is_alpha(self, char: str) -> bool:
        """
        DFA implementation for alphabetic character recognition.
        Transitions through states to determine if a character is alphabetic.
        """
        if not char:
            return False
        
        # States: 0 (start), 1 (accept uppercase), 2 (accept lowercase)
        state = 0
        for c in char:
            if state == 0:
                if 'A' <= c <= 'Z':
                    state = 1
                elif 'a' <= c <= 'z':
                    state = 2
                else:
                    return False
        
        return state in [1, 2]
    
    @staticmethod
    def is_digit(self, char: str) -> bool:
        """
        DFA implementation for digit recognition.
        Transitions through states to determine if a character is a digit.
        """
        if not char:
            return False
        
        # States: 0 (start), 1 (accept digit)
        state = 0
        for c in char:
            if state == 0:
                if '0' <= c <= '9':
                    state = 1
                else:
                    return False
        
        return state == 1
    
    @staticmethod
    def is_skippable(self, char: str) -> bool:
        """
        DFA implementation for skippable character recognition.
        Checks for whitespace characters.
        """
        skippable_chars = {' ', '\t', '\n', '\r'}
        return char in skippable_chars
