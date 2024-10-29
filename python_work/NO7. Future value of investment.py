def main():
    print("Future Value Calculator with Compounding Periods")

    principal = float(input("Enter the initial principal: "))
    rate = float(input("Enter the annual interest rate (as a decimal): "))
    periods = int(input("Enter the number of times that interest is compounded each year: "))

    total_periods = 10 * periods  # 10 years
    rate_per_period = rate / periods  # Interest rate per period

    for i in range(total_periods):
        principal = principal * (1 + rate_per_period)

    print(f"The value of the investment after 10 years is {principal:.2f}")

if __name__ == "__main__":
    main()