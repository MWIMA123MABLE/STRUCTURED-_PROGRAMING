def main():
    print("Fahrenheit to Celsius Converter")

    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9

    print(f"The temperature in Celsius is {celsius:.2f} degrees.")

if __name__ == "__main__":
    main()