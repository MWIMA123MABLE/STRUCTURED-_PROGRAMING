def main():
    print("Future Value Calculator")
    
    principal = float(input("Enter the initial principal: "))
    rate = float(input("Enter the annual interest rate (as a decimal): "))
    years = int(input("Enter the number of years for the investment: "))
    
    for i in range(years):
        principal = principal * (1 + rate)
    
    print(f"The value of the investment after {years} years is {principal:.2f}")

if __name__ == "__main__":
    main()