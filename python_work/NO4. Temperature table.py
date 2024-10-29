
def main():
    print("Celsius to Fahrenheit conversion table:")
    print("Celsius | Fahrenheit")
    print("--------------------")
    
    for celsius in range(0, 101, 10):
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius:>7} | {fahrenheit:>10.2f}")

if __name__ == "__main__":
    main()