def main():
    print("Liters to Gallons Converter")
    print("This program converts volumes from liters to gallons.")

    liters = float(input("Enter volume in liters: "))
    gallons = liters * 0.264172

    print(f"The volume in gallons is {gallons:.2f} gallons.")

if __name__ == "__main__":
    main()