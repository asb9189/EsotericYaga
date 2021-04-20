from token import tokenType

simple_lexemes = [
    "Yaga",
    "yAga",
    "yaGa",
    "yagA",
    "yagayaga",
    "YAGAYAGA",
    "yagaYAGA",
    "YAGAyaga",
    "agay",
    "AGAY"
]

simple_lex_to_token_type = {
    "Yaga": tokenType.increment,
    "yAga": tokenType.decrement,
    "yaGa": tokenType.left,
    "yagA": tokenType.right,
    "yagayaga": tokenType.print_chars,
    "YAGAYAGA": tokenType.print_vals,
    "yagaYAGA": tokenType.print_current_char,
    "YAGAyaga": tokenType.print_current_val,
    "agay": tokenType.accept_input,
    "AGAY": tokenType.reset
}