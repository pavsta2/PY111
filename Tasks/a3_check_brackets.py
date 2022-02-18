def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    stack_brackets_init = list(brackets_row)
    stack_brackets_sec = ["queue_is_cleared"]
    if len(stack_brackets_init) == 1:
        return False
    if len(stack_brackets_init) == 0:
        return True
    if stack_brackets_init[-1] == "(":
        return False
    if stack_brackets_init[0] == ")":
        return False

    while stack_brackets_init:
        if stack_brackets_sec[-1] + stack_brackets_init[0] == "()":
            stack_brackets_init.pop(0)
            stack_brackets_sec.pop(-1)
        else:
            stack_brackets_sec.append(stack_brackets_init[0])
            stack_brackets_init.pop(0)

    if stack_brackets_sec[-1] == "queue_is_cleared":
        return True
    else:
        return False


if __name__ == "__main__":
    print(check_brackets("()()(()())"))
