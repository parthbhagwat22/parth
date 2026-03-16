from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide

def main():
    while True:
        print("\nSimple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("Select operation (1-5): ")

        if choice == '5':
            print("Exiting the calculator.")
            break

        if choice in ['1', '2', '3', '4']:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {add(a, b)}")
            elif choice == '2':
                print(f"Result: {subtract(a, b)}")
            elif choice == '3':
                print(f"Result: {multiply(a, b)}")
            elif choice == '4':
                result = divide(a, b)
                if result is not None:
                    print(f"Result: {result}")
        else:
            print("Invalid input. Please select a valid operation.")

if __name__ == '__main__':
    main()