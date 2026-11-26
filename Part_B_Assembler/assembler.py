
def clean_code(filename):
    instructions = []

    with open(filename, "r") as file:
        for line in file:
            # Remove comments
            line = line.split("//")[0]

            # Remove extra spaces
            line = line.strip()

            # Ignore blank lines
            if line:
                instructions.append(line)

    return instructions


# Test our function
if __name__ == "__main__":
    code = clean_code("Add.asm")

    for instruction in code:
        print(instruction)


def first_pass(instructions):
    symbol_table = {}

    # Predefined Hack symbols
    for i in range(16):
        symbol_table["R" + str(i)] = i

    symbol_table["SP"] = 0
    symbol_table["LCL"] = 1
    symbol_table["ARG"] = 2
    symbol_table["THIS"] = 3
    symbol_table["THAT"] = 4
    symbol_table["SCREEN"] = 16384
    symbol_table["KBD"] = 24576

    for i in range(16):
        symbol_table["R" + str(i)] = i

    instruction_address = 0

    for instruction in instructions:

        if instruction.startswith("(") and instruction.endswith(")"):
            label = instruction[1:-1]

            symbol_table[label] = instruction_address

        else:
            instruction_address += 1

    return symbol_table

