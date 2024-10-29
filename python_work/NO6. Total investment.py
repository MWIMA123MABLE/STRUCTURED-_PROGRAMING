def main():
    print("Future Value Calculator with Annual Investments")

    annual_investment = float(input("Enter the amount to invest each year: "))
    rate = float(input("Enter the annual interest rate (as a decimal): "))
    years = int(input("Enter the number of years for the investment: "))
    
    total = 0

    for i in range(years):
        total = (total + annual_investment) * (1 + rate)
    
    print(f"The total accumulation after {years} years is {total:.2f}")

if __name__ == "__main__":
    main()