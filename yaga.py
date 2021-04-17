
import sys
from yagayaga import valid_file, tokenize
from Token import tokenType

mem_len = 12
mem_pointer = 0
mem_max_right = mem_len - 1
mem_min_left = 0
mem_increment_value = 1
mem_decrement_value = 1

def main():

    if len(sys.argv) == 2:
        run_file(sys.argv[1])
    else:
        print("python3 yaga.py [file]")

def run_file(file):
    is_valid = valid_file(file)
    if not is_valid:
        print("Invalid file")
        sys.exit()

    tokens = tokenize(file)
    run(tokens)

def run(tokens):

    global mem_len
    global mem_pointer
    global mem_max_right
    global mem_min_left
    global mem_increment_value
    global mem_decrement_value

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
            continue
        elif tokens[token_pointer].tokenType == tokenType.left:
            if mem_pointer - 1 >= mem_min_left:
                mem_pointer -= 1
        elif tokens[token_pointer].tokenType == tokenType.right:
            if mem_pointer + 1 <= mem_max_right:
                mem_pointer += 1
        elif tokens[token_pointer].tokenType == tokenType.set_increment:
            mem_increment_value = tokens[token_pointer].value
        elif tokens[token_pointer].tokenType == tokenType.set_decrement:
            mem_decrement_value = tokens[token_pointer].value
        elif tokens[token_pointer].tokenType == tokenType.print_chars:
            arr = ""
            for val in memory:
                arr += chr(val)
            print(arr)
        elif tokens[token_pointer].tokenType == tokenType.print_vals:
            arr = ""
            for val in memory:
                arr += "[" + str(val) + "]"
            print(arr)
        elif tokens[token_pointer].tokenType == tokenType.print_current_char:
            print(chr(tokens[token_pointer]) + "\n")
        elif tokens[token_pointer].tokenType == tokenType.print_current_val:
            print(tokens[token_pointer] + "\n")
        elif tokens[token_pointer].tokenType == tokenType.accept_input:
            stdin = input("> ")
            if type(stdin) is not int:
                raise Exception(f"Input must be of type 'int'")
        elif tokens[token_pointer].tokenType == tokenType.reset:
            for i in range(0, len(memory)):
                memory[i] = 0
            mem_pointer = 0
        else:
            raise Exception(f"Unknown yaga instruction '{tokens[token_pointer]}'")

        token_pointer += 1


if __name__ == "__main__":
    main()