BRACKETS = "([{)]}"


def main() -> None:
    line = input()
    bracket_type_stack = []
    bracket_position_stack = []
    i = -1
    for character in line:
        i += 1
        bracket_type = BRACKETS.find(character)
        if bracket_type == -1:
            continue
        elif bracket_type < 3:
            bracket_type_stack.append(bracket_type)
            bracket_position_stack.append(i)
        else:
            if bracket_type_stack and bracket_type - 3 == bracket_type_stack[-1]:
                bracket_type_stack.pop()
                bracket_position_stack.pop()
            else:
                print(" " * i + "^")
                print(f"Problem at position {i}: {BRACKETS[bracket_type]}")
                break
    else:
        if bracket_position_stack:
            print(" " * bracket_position_stack[-1] + "^")
            print(
                f"Problem at position {bracket_position_stack[-1]}: {BRACKETS[bracket_type_stack[-1]]}"
            )
        else:
            print("Balanced")


if __name__ == "__main__":
    main()
