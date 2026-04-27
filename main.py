from app.calculator import Calculator
from resources.messages import (
    WELCOME, PROMPT_A, PROMPT_B, PROMPT_OP,
    INVALID_NUMBER, INVALID_OP, RESULT_TEMPLATE,
)

OPERATIONS = {
    "+": "add",
    "-": "subtract",
    "*": "multiply",
    "/": "divide",
}


def run():
    calc = Calculator()
    print(WELCOME)

    try:
        a = float(input(PROMPT_A))
        b = float(input(PROMPT_B))
    except ValueError:
        print(INVALID_NUMBER)
        return

    op = input(PROMPT_OP).strip()
    method_name = OPERATIONS.get(op)

    if method_name is None:
        print(INVALID_OP)
        return

    try:
        result = getattr(calc, method_name)(a, b)
        print(RESULT_TEMPLATE.format(result))
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    run()
