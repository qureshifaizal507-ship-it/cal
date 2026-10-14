def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")
    print("Type 'q' at any prompt to quit.\n")

    while True:
        a = input("Enter first number: ").strip()
        if a.lower() == "q":
            break

        op = input("Enter operation (+, -, *, /): ").strip()
        if op.lower() == "q":
            break

        b = input("Enter second number: ").strip()
        if b.lower() == "q":
            break

        try:
            x, y = float(a), float(b)
        except ValueError:
            print("Please enter valid numbers.\n")
            continue

        if op == "+":
            result = x + y
        elif op == "-":
            result = x - y
        elif op == "*":
            result = x * y
        elif op == "/":
            if y == 0:
                print("Error: cannot divide by zero.\n")
                continue
            result = x / y
        else:
            print("Invalid operation. Use +, -, * or /.\n")
            continue

        print(f"Result: {x} {op} {y} = {result}\n")

    print("Goodbye!")


if __name__ == "__main__":
    calculator()
