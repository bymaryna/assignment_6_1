def main():
    print("Welcome to CLI calculator!")
    num1 = float(input("Enter first number: "))
    op = input("Enter operation (+ or -): ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    else:
        print("Unsupported operation.")

if __name__ == "__main__":
    main()

    