# Group names: Ian Martinez, Kiara Guerra, Arturo Roman, Omar Montes
# Final Project Part 3
# Due date : 12/10/2024
# Purpose: Have our program (compiler) check the grammar of the program and display “No Error”
# if the given grammar liked the program or issue “some errors” otherwise
#
#
# Starting with parsing table
parsing_table_q2 = {
    "P": {"program": "program I ; var C begin G end"},
    "I": {"a": "LR", "b": "LR", "c": "LR", "d": "LR", "l": "LR", "f": "LR"},
    "R": {"a": "LR", "b": "LR", "c": "LR", "d": "LR", "l": "LR", "f": "LR", "0": "DR", "1": "DR", "2": "DR", "3": "DR",
          "4": "DR", "5": "DR", "6": "DR", "7": "DR", "8": "DR", "9": "DR", ")": "λ", "+": "λ", "-": "λ", "*": "λ",
          "/": "λ", "=": "λ", ",": "λ", ";": "λ", ":": "λ"},
    "C": {"a": "Z: Y;", "b": "Z: Y;", "c": "Z: Y;", "d": "Z: Y;", "l": "Z: Y;", "f": "Z: Y;"},
    "Z": {"a": "IX", "b": "IX", "c": "IX", "d": "IX", "l": "IX", "f": "IX"},
    "X": {",": ",Z", ":": "λ"},
    "Y": {"integer": "integer"},
    "G": {"print": "HJ", "a": "HJ", "b": "HJ", "c": "HJ", "d": "HJ", "l": "HJ", "f": "HJ"},
    "J": {"print": "G", "a": "G", "b": "G", "c": "G", "d": "G", "l": "G", "f": "G", "end": "λ"},
    "H": {"print": "W", "a": "A", "b": "A", "c": "A", "d": "A", "l": "A", "f": "A"},
    "W": {"print": "print(BI);"},
    "B": {"O": "O", "a": "λ", "b": "λ", "c": "λ", "d": "λ", "l": "λ", "f": "λ", '"value=",': '"value=",'},
    "A": {"a": "I = E;", "b": "I = E;", "c": "I = E;", "d": "I = E;", "l": "I = E;", "f": "I = E;"},
    "E": {"a": "TQ", "b": "TQ", "c": "TQ", "d": "TQ", "l": "TQ", "f": "TQ", "0": "TQ", "1": "TQ", "2": "TQ", "3": "TQ",
          "4": "TQ", "5": "TQ",
          "6": "TQ", "7": "TQ", "8": "TQ", "9": "TQ", "(": "TQ", "+": "TQ", "-": "TQ"},
    "Q": {";": "λ", "+": "+TQ", "-": "-TQ", ")": "λ"},
    "T": {"a": "FV", "b": "FV", "c": "FV", "d": "FV", "l": "FV", "f": "FV", "0": "FV", "1": "FV", "2": "FV", "3": "FV",
          "4": "FV", "5": "FV", "6": "FV", "7": "FV", "8": "FV", "9": "FV", "(": "FV", "+": "FV", "-": "FV"},
    "V": {";": "λ", "*": "*FV", "/": "/FV", "-": "λ", "+": "λ", ")": "λ"},
    "F": {"a": "I", "b": "I", "c": "I", "d": "I", "l": "I", "f": "I", "0": "N", "1": "N", "2": "N", "3": "N", "4": "N",
          "5": "N", "6": "N", "7": "N", "8": "N", "9": "N", "+": "N", "-": "N", "(": "(E)"},
    "N": {"0": "SDK", "1": "SDK", "2": "SDK", "3": "SDK", "4": "SDK", "5": "SDK", "6": "SDK", "7": "SDK", "8": "SDK",
          "9": "SDK", "+": "SDK", "-": "SDK"},
    "K": {"0": "DK", "1": "DK", "2": "DK", "3": "DK", "4": "DK", "5": "DK", "6": "DK", "7": "DK", "8": "DK", "9": "DK",
          "+": "λ", "-": "λ", "*": "λ", "/": "λ", ")": "λ", ";": "λ"},
    "S": {"0": "λ", "1": "λ", "2": "λ", "3": "λ", "4": "λ", "5": "λ", "6": "λ", "7": "λ", "8": "λ", "9": "λ", "+": "+",
          "-": "-"},
    "D": {"0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"},
    "L": {"a": "a", "b": "b", "c": "c", "d": "d", "l": "e", "f": "f"}
}

# Reserved words for the grammar
reserved = {"program", "end", "var", "begin", "integer", "print", "LB"}
LB = '"value=",'

# Function to get the next chunk of input from the given string it skips over white space and checks if there are any
# matches for reserved words till the next whitepace if not then the string is taken char by char
def get_next_chunk(input_string, index):
    while index < len(input_string) and input_string[index].isspace():
        index += 1

    if index >= len(input_string):
        return "$", index

    if input_string.startswith(LB, index):
        return LB, index + len(LB)

    for length in range(len(input_string) - index, 0, -1):
        possible_chunk = input_string[index:index + length]
        if possible_chunk in reserved:
            return possible_chunk, index + length

    return input_string[index], index + 1

# Function to split a production rule into individual chunks so lift of takens using other function
def chunk_production(production):
    chunks = []
    index = 0
    while index < len(production):
        chunk, index = get_next_chunk(production, index)
        chunks.append(chunk)
    return chunks

# Function to accept or reject lines based on the grammar rules
def accept_or_reject_lines(input_lines):
    stack = ["$", "P"]
    step = 1

    for line_number, line in enumerate(input_lines, start=1):
        index = 0
        line += "#"
        print(f"\nLine Tracing: {line}")

        while stack:
            top = stack[-1]
            current_input, next_index = get_next_chunk(line, index)

            if current_input == "$" and top == "$":
                break

            elif top == current_input:
                stack.pop()
                index = next_index
            else:
                grammar = parsing_table_q2.get(top, {}).get(current_input)
                if grammar is None:
                    if current_input == "#":
                        print(f"Accepted at end of line {line_number}")
                        break
                    elif top == "var":
                        if current_input == "var":
                            continue
                        else:
                            print(f"\nERROR on line {line_number}, 'var' misspelled")
                            return False
                    elif top == "Y":
                        if current_input == "integer":
                            continue
                        else:
                            print(f"\nERROR on line {line_number}, 'integer' misspelled")
                            return False
                    elif top == "P":
                        if current_input == "program":
                            continue
                        else:
                            print(f"\nERROR on line {line_number}, 'program' misspelled")
                            return False
                    elif top == "begin":
                        if current_input == "begin":
                            continue
                        else:
                            print(f"\nERROR on line {line_number}, 'begin' misspelled")
                            return False
                    elif top == "J":
                        if current_input == "end":
                            continue
                        elif current_input == "print":
                            continue
                        elif current_input == "p":
                            print(f"\nERROR on line {line_number}, 'print' misspelled")
                            return False
                        elif current_input == "e" or current_input == "n" or current_input == "d":
                            print(f"\nERROR on line {line_number}, 'end' misspelled")
                            return False
                        else:
                            print(f"\nERROR on line {line_number}, unknown identifier {current_input}")
                            return False
                    elif top == "R" or top == ";" or top == "K":
                        if current_input == "print" or current_input == "end" or current_input == "var" or current_input == "begin" or current_input == "b" or current_input == "c":
                            print(f"\nERROR on line {line_number - 1}, ';' is missing")
                            return False
                        else:
                            continue
                    elif top == ")":
                        if current_input == ")":
                            continue
                        else:
                            print(f"\nERROR on line {line_number}, ')' is missing")
                            return False
                    elif top == "(":
                        if current_input == "c" or current_input == '"value=",':
                            print(f"\nERROR on line {line_number}, '(' is missing")
                            return False
                        else:
                            continue
                    else:
                        print(
                            f"{step}\t{' '.join(stack)}\t\t\tPop: {top} | Reject: no matching grammar for '{current_input}'")
                        return False

                stack.pop()
                if grammar != "λ":
                    chunks = chunk_production(grammar)
                    for chunk in reversed(chunks):
                        stack.append(chunk)
                elif top == "B" and current_input == "O":
                    stack.append(LB)

                elif grammar == "λ":
                    continue
                else:
                    return False

            step += 1

        index = 0

    return True

# Main that takes care of opening the file and having the last say of accept or reject
def main():
    input_filename = "final24.txt"
    try:
        with open(input_filename, encoding="utf-8") as file:
            input_lines = file.read().strip().split('\n')

            if input_lines:
                result = accept_or_reject_lines(input_lines)
                if result:
                    print("\nReady to Compile")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")


if __name__ == "__main__":
    main()
