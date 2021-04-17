
import sys
from yagayaga import valid_file, tokenize
from Token import tokenType

mem_len = 12
mem_pointer = 0
mem_max_right = mem_len - 1
men_min_left = 0
mem_increment_value = 1
mem_decrement_value = 1

def main():

    if len(sys.argv) == 1:
        run_repl()
    elif len(sys.argv) == 2:
        run_file(sys.argv[1])
    else:
        print("python3 yaga.py [file]")

def run_repl():
    pass

def run_file(file):
    is_valid = valid_file(file)
    if not is_valid:
        print("Invalid file")
        sys.exit()

    tokens = tokenize(file)
    run(tokens)

def run(tokens):
    memory = [0] * mem_len
    token_pointer = 0

    while token_pointer < len(tokens):
        if tokens[token_pointer].tokenType == tokenType.increment:
            memory[mem_pointer] = memory[mem_pointer] + mem_increment_value
        elif tokens[token_pointer].tokenType == tokenType.decrement:
            memory[mem_pointer] = memory[mem_pointer] - mem_decrement_value
        elif tokens[token_pointer].tokenType == tokenType.start_loop:
            continue
        elif tokens[token_pointer].tokenType == tokenType.end_loop:
            if memory[mem_pointer] != 0:
                token_pointer = tokens[token_pointer].goTo
        elif tokens[token_pointer].tokenType == tokenType.left:
            pass
        elif tokens[token_pointer].tokenType == tokenType.right:
            pass
        elif tokens[token_pointer].tokenType == tokenType.set_increment:
            pass
        elif tokens[token_pointer].tokenType == tokenType.set_decrement:
            pass
        elif tokens[token_pointer].tokenType == tokenType.print_chars:
            pass
        elif tokens[token_pointer].tokenType == tokenType.print_vals:
            pass
        elif tokens[token_pointer].tokenType == tokenType.print_current_char:
            pass
        elif tokens[token_pointer].tokenType == tokenType.print_current_val:
            pass
        elif tokens[token_pointer].tokenType == tokenType.accept_input:
            pass
        elif tokens[token_pointer].tokenType == tokenType.reset:
            pass
        else:
            raise Exception(f"Unknown yaga instruction '{tokens[token_pointer]}'")


if __name__ == "__main__":
    main()