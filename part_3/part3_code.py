parsing_table_q2 = {
    "P": {"program": "program I ; var C begin G end"},
    "I": {"a": "LR", "b": "LR", "c": "LR", "d": "LR", "l": "LR", "f": "LR"},
    "R": {"a": "LR", "b": "LR", "c": "LR", "d": "LR", "l": "LR", "f": "LR", "0": "DR", "1": "DR", "2": "DR", "3": "DR",
          "4": "DR", "5": "DR", "6": "DR", "7": "DR", "8": "DR", "9": "DR", ")": "λ", "+": "λ", "-": "λ",  "*": "λ",
          "/": "λ",  "=": "λ", ",": "λ", ";": "λ", ":": "λ"},
    "C": {"a": "Z: Y;", "b": "Z: Y;", "c": "Z: Y;", "d": "Z: Y;", "l": "Z: Y;", "f": "Z: Y;"},
    "Z": {"a": "IX", "b": "IX", "c": "IX", "d": "IX", "l": "IX", "f": "IX"},
    "X": {",": ",Z", ":": "λ"},
    "Y": {"integer": "integer" },
    "G": {"print": "HJ", "a": "HJ", "b": "HJ", "c": "HJ", "d": "HJ", "l": "HJ", "f": "HJ"},
    "J": {"print": "G", "a": "G", "b": "G", "c": "G", "d": "G", "l": "G", "f": "G", "end": "λ"},
    "H": {"print": "W", "a": "A", "b": "A",  "c": "A", "d": "A", "l": "A", "f": "A"},
    "W": {"print": "print(BI);"},
    "B": {"O": "O", "a": "λ", "b": "λ", "c": "λ", "d": "λ", "l": "λ", "f": "λ", '"value=",': "λ"},
    "A": {"a": "I = E;", "b": "I = E;", "c": "I = E;", "d": "I = E;", "l": "I = E;", "f": "I = E;"},
    "E": {"a": "TQ", "b": "TQ", "c": "TQ", "d": "TQ", "l": "TQ", "f": "TQ", "0": "TQ", "1": "TQ", "2": "TQ", "3": "TQ", "4": "TQ", "5": "TQ",
          "6": "TQ", "7": "TQ", "8": "TQ", "9": "TQ", "(": "TQ", "+": "TQ", "-": "TQ"},
    "Q": {";": "λ", "+": "+TQ", "-": "-TQ", ")": "λ",  "ε": "λ"},
    "T": {"a": "FV", "b": "FV", "c": "FV", "d": "FV", "l": "FV", "f": "FV", "0": "FV", "1": "FV", "2": "FV", "3": "FV",
          "4": "FV", "5": "FV", "6": "FV", "7": "FV", "8": "FV", "9": "FV", "(": "FV", "+": "FV", "-": "FV",  "ε": "λ"},
    "V": {";": "λ", "*": "*FV", "/": "/FV", "-": "λ", "+": "λ", ")": "λ",  "ε": "λ"},
    "F": {"a": "I", "b": "I", "c": "I", "d": "I", "l": "I", "f": "I", "0": "N", "1": "N", "2": "N", "3": "N", "4": "N",
          "5": "N", "6": "N", "7": "N", "8": "N", "9": "N", "+": "N", "-": "N", "(": "(E)",  "ε": "λ"},
    "N": {"0": "SDK", "1": "SDK", "2": "SDK", "3": "SDK", "4": "SDK", "5": "SDK", "6": "SDK", "7": "SDK", "8": "SDK",
          "9": "SDK", "+": "SDK", "-": "SDK",  "ε": "λ"},
    "K": {"0": "DK", "1": "DK", "2": "DK", "3": "DK", "4": "DK", "5": "DK", "6": "DK", "7": "DK", "8": "DK", "9": "DK",
          "+": "λ", "-": "λ", "*": "λ", "/": "λ", ")": "λ", ";": "λ",  "ε": "λ"},
    "S": {"0": "λ", "1": "λ", "2": "λ", "3": "λ", "4": "λ", "5": "λ", "6": "λ", "7": "λ", "8": "λ", "9": "λ", "+": "+", "-": "-", "ε": "λ"},
    "D": {"0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",  "ε": "λ"},
    "L": {"a": "a", "b": "b", "c": "c", "d": "d", "l": "e", "f": "f",  "ε": "λ"}
}

reserved = {"program", "end", "var", "begin", "integer", "print", "LB"}
LB = '"value=",'

def get_next_chunk(input_string, index):
    while index < len(input_string) and input_string[index].isspace():
        index += 1  # Skip whitespace

    if index >= len(input_string):
        return "$", index  # End of input

    if input_string.startswith('"value=",', index):
        return '"value=",', index + len('"value=",')

        # If no match, continue with existing logic
    for length in range(len(input_string) - index, 0, -1):
        possible_chunk = input_string[index:index + length]
        if possible_chunk in reserved:
            return possible_chunk, index + length  # Return reserved word

    return input_string[index], index + 1  # Return the next character as a single token


def chunk_production(production):
    chunks = []
    index = 0
    while index < len(production):
        chunk, index = get_next_chunk(production, index)
        chunks.append(chunk)
    return chunks


def accept_or_reject(input_string):
    stack = ["$", "P"]
    index = 0
    step = 1

    print("\nLine Tracing:", input_string)
    print("Step\tStack\tPath")

    while stack:
        top = stack.pop()
        current_input, next_index = get_next_chunk(input_string, index)

        if current_input == "$" and top == "$":
            print(f"{step}\t\t\tPop: {top} | Accepted")
            return True

        elif top == current_input:
            print(f"{step}\t{' '.join(stack)}\t\t\tPop: {top} | Match with input '{current_input}'")
            index = next_index

        else:
            grammar = parsing_table_q2.get(top, {}).get(current_input)
            if grammar != "λ" and top != "B":
                path = f"Pop: {top} | Go to [{top}, {current_input}] -> {grammar}"
                chunks = chunk_production(grammar)
                for chunk in reversed(chunks):
                    stack.append(chunk)
                    path += f" | Push {chunk}"
                print(f"{step}\t{' '.join(stack)}\t\t\t{path}")

            elif top == "B" and current_input == "O":
                stack.append('"value=",')
            elif current_input == '"':
                top == current_input;
            elif current_input == '"value=",':
                print(f"{step}\t{' '.join(stack)}\t\t\tPop: {top} | Go to [{top}, {current_input}] -> {grammar}")
                index = next_index
            elif grammar == "λ":
                print(f"{step}\t{' '.join(stack)}\t\t\tPop: {top} | Go to [{top}, {current_input}] -> {grammar}")
            else:
                print(f"{step}\t{' '.join(stack)}\t\t\tPop: {top} | Reject: no matching grammar for '{current_input}'")
                return False

        step += 1

    print(f"Reject: no matching grammar for '{current_input}'")
    return False
def main():
    input_filename = "final24.txt"
    try:
        with open(input_filename, encoding="utf-8") as file:
            all = file.read().strip()
            fall = all +  "$"

            if fall:
                result = accept_or_reject(fall)
                print(f"\nResult for \"{all}\": {'Accepted' if result else 'Rejected'}")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")


if __name__ == "__main__":
    main()