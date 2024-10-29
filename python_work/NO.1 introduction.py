def main():
    print("Welcome to the Temperature Converter Program!")
    print("This program converts temperatures from Celsius to Fahrenheit.")
    print("Let's get started.")

    # Original convert.py code
    celsius = float(input("Enter a temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"The temperature in Fahrenheit is {fahrenheit} degrees.")

if __name__ == "__main__":
    main()