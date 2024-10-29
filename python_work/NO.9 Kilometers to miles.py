def main():
    print("Kilometers to Miles Converter")

    kilometers = float(input("Enter distance in kilometers: "))
    miles = kilometers * 0.62

    print(f"The distance in miles is {miles:.2f} miles.")

if __name__ == "__main__":
    main()