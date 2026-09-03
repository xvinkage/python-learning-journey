import  art

print(art.logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,

}


result = ""

while True:
    if result == "":
        n1 = int(input("What's the first number?: "))
    else:
        n1 = result
    for operators in operations:
        print(operators)
    operator = input("Pick an operation: ")
    n2 = int(input("What's the next number?: "))
    result = operations[operator](n1, n2)
    print(f"{n1} {operator} {n2} = {result}")
    more_math = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

    if more_math == "y":
        n1 = result

    if more_math == 'n':
        print("\n" * 50)
        result = ""
