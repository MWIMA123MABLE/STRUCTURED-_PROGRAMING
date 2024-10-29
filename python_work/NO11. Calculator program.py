def main():
    print("Interactive Python Calculator")
    print("You can perform up to 100 calculations. Type your mathematical expression.")
    print("To quit early, you can make the program crash by typing a bad expression or closing the window.")

    for _ in range(100):
        try:
            expression = input("Enter your calculation: ")
            result = eval(expression)
            print(f"The result is: {result}")
        except Exception as e:
            print(f"An error occurred: {e}. Exiting the calculator.")
            break

if __name__ == "__main__":
    main()