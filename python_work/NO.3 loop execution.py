def main():
    print("Welcome to the Temperature Converter Program!")
    print("This program converts temperatures from Celsius to Fahrenheit.")
    print("It will convert 5 temperatures in a row.")
    
    for i in range(5):
        celsius = float(input(f"Enter temperature {i+1} in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"Temperature {i+1} in Fahrenheit is {fahrenheit:.2f} degrees.")
        
    print("Temperature conversion complete.")

if __name__ == "__main__":
    main()