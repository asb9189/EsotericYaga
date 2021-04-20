
import re
from lexemes import simple_lexemes, simple_lex_to_token_type
from token import token, tokenType
complex_lexemes_pattern = re.compile(r"(^Yaga=\d*$|^yAga=\d*$|^yaga$|^YAGA$)")

def valid_file(file):
    lexemes = open(file, "r").read().split()
    parentheses = []
    for lex in lexemes:
        if lex not in simple_lexemes and complex_lexemes_pattern.match(lex):
            if lex == "yaga":
                parentheses.append(lex)
            elif lex == "YAGA":
                if len(parentheses) == 0:
                    return False
                else:
                    parentheses.pop()
    if len(parentheses) == 0:
        return True
    return False

def tokenize(file):
    lexemes = open(file, "r").read().split()
    tokens = _tokenize(lexemes)

    stack = []
    for index, token in enumerate(tokens):
        if token.tokenType == tokenType.start_loop:
            token.index = index
            stack.append(token)
        if token.tokenType == tokenType.end_loop:
            token.goTo = stack.pop().index

    return tokens

def _tokenize(lexemes):
    tokens = []
    for lex in lexemes:
        if lex in simple_lexemes:
            try:
                tokens.append(token(lex, simple_lex_to_token_type[lex]))
            except KeyError:
                raise Exception(f"unknown simple lexeme '{lex}'")
        elif complex_lexemes_pattern.match(lex):
            if lex.startswith("Yaga="):
                tokens.append(token(lex, tokenType.set_increment))
            elif lex.startswith("yAga="):
                tokens.append(token(lex, tokenType.set_decrement))
            elif lex == "yaga":
                tokens.append(token(lex, tokenType.start_loop))
            elif lex == "YAGA":
                tokens.append(token(lex, tokenType.end_loop))
            else:
                raise Exception(f"unknown complex lexeme '{lex}'")
    return tokens
