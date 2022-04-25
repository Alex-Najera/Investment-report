"""
Author: Alexander Najera
Date: January 10th, 2020
Purpose: Compute an investment report.
1. The inputs are
    starting investment amount
    number of years
    interest rate (an integer percent)
2. The report is displayed in tabular form with a header.
3.Computations and outputs:
    for each year
        compute the interest and add it to the investment
        print a formatted row of results for that year
4. The ending investment and interest earned are also
    displayed.

"""
# MAIN PROGRAM :
n = 1  # line number for each separator line
# must use your name!
print("Welcome to the Investment Report Tool Made By Alexander Najera!")
print(n, "======================================================")
n += 1

# Accept the inputs
start_balance = float(input("How much would you like to invest? "))
years = int(input("Enter the number of years: "))
rate = float(input("Enter the rate of return as a %: "))

print(n, "======================================================")
n += 1

# Convert the rate to a decimal number
rate = rate / 100

# Initialize the accumulator for the interest
totalInterest = 0.0

# Display the header for the table
print("%4s%18s%10s%16s" %
      ("Year", "Starting Balance", "Interest", "Ending balance"))

# Compute and display thee results for each year
for year in range(1, years + 1):
    interest = start_balance * rate
    endBalance = start_balance + interest
    print("%4d%18.2f%10.2f%16.2f" %
          (year, start_balance, interest, endBalance))
    start_balance = endBalance
    totalInterest += interest

print(n, "======================================================")
n += 1

# Display the totals for the period
print("Ending balance: $%0.2f" % endBalance)
print("Total interest earned: $%0.2f" % totalInterest)

print(n, "======================================================")
n += 1

# must use your name!
print("Thank you for using the Investment Report Tool of Alexander Najera! ")

print(n, "======================================================.")
n += 1

x = input(
    "Press Ctrl+Alt+PrtScn to get a snapshot of this console, then Enter to exit: ")
# End of MAIN PROGRAM
