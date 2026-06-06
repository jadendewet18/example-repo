# Import the math library
# Print the menu options (Investment and Bond)
# Get the user's choice and convert it to lowercase
# IF choice is "investment":
# - Ask for deposit, interest rate, and number of years
# - Ask if they want "simple" or "compound"
# - IF simple: calculate using simple formula
# - ELIF compound: calculate using compound formula
# - Print the result
# - ELIF choice is "bond":
# - Ask for house value, interest rate, and months
# - Calculate monthly repayment
# - Print the result
# - ELSE:
# - Print an error message (invalid choice)

import math

print("Investment - to calculate the amount of interest you'll earn on your investment")

print("Bond   - to calculate the amount you'll have to pay on a home loan")

print("\nEnter either 'investment' or 'bond' from the menu to proceed: ")

user_choice = input().lower()
if user_choice == "investment":

    p = float(input("Enter the amount of money you are going to deposit: "))
    r = float(input("Enter the interest rate (as a number): ")) / 100
    t = float(input("Enter the number of years you plan on investing: "))

    
    interest = input("Do you want 'simple' or 'compound interest?: ").lower()

    if interest == "simple":
                #Formula: A = P * (1 + r * t)
                total = p * (1 + r * t)
                print(f"\nYour total amount after {t} years will be: R{round(total, 2)}")

    elif interest == "compound":
                # Formula: A = P * math.pow((1 + r), t)
                total = p * math.pow((1 + r), t)
                print(f"\nYour total amount after {t} years will be: R{round(total, 2)}")


elif user_choice == "bond":
        
        p = float(input("Enter the present value of the house: "))

        # 'i' is annual rate  / 100 / 12
        annual_rate = float(input("Enter the annual interest rate: "))
        i = (annual_rate / 100) / 12
        n = float(input("Enter the number of months to repay the bond: "))

        # Formula: repayment = (i * P) / (1 - (1 + i)**(-n))
        repayment = (i * p) / (1 - math.pow((1 + i), -n))
        print(f"\nYour monthly repayment will be: R{round(repayment, 2)}")

else:
        print("Error: Invalid selection. Please restart and enter 'investment' or 'bond'.")













