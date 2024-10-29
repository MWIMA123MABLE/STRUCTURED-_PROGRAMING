def main():
    print("Welcome to the Average Calculator for Three Exam Scores!")
    
    score1 = float(input("Enter the first exam score: "))
    score2 = float(input("Enter the second exam score: "))
    score3 = float(input("Enter the third exam score: "))
    
    average = (score1 + score2 + score3) / 3
    print(f"The average of the three exam scores is {average:.2f}.")

if __name__ == "__main__":
    main()