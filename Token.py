
from enum import Enum

class tokenType(Enum):
    increment = 1
    decrement = 2
    left = 3
    right = 4
    print_chars = 5
    print_vals = 6
    print_current_char = 7
    print_current_val = 8
    start_loop = 9
    end_loop = 10
    set_increment = 11
    set_decrement = 12
    accept_input = 13
    reset = 14

class token:
    def __init__(self, lex, tokenType):
        self.lex = lex
        self.tokenType = tokenType
        self.index = None
        self.goTo = None
        self.value = None

        if tokenType == tokenType.set_increment or tokenType == tokenType.set_decrement:
            self.value = int(lex[5:])

    def __str__(self):
        token_as_string = f"Lex: {self.lex}\nToken Type: {self.tokenType}\nIndex: {self.index}\nGo To: {self.goTo}"
        return token_as_string