
###BUILD A TOOL TO TRACK AND MANAGE PERSONAL EXPENSE AND GENERATE MONTHLY REPORTS........

#import library
import csv
from collections import defaultdict
from datetime import datetime

# Function to record expenses
def record_expense(expense, amount, date):
    with open('expenses.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([expense, amount, date])

# Function to generate monthly reports
def generate_monthly_report(year, month):
    expenses = defaultdict(float)
    with open('expenses.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            expense, amount, date = row
            date = datetime.strptime(date, "%Y-%m-%d")
            if date.year == year and date.month == month:
                expenses[expense] += float(amount)

    print(f"Monthly Report for {datetime(year, month, 1).strftime('%B %Y')}")
    for expense, amount in expenses.items():
        print(f"{expense}: ${amount:.2f}")

# Main program loop
while True:
    print("Personal Expense Tracking Tool")
    print("1. Record Expense")
    print("2. Generate Monthly Report")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        expense = input("Enter the expense name: ")
        amount = float(input("Enter the amount: "))
        date = input("Enter the date (YYYY-MM-DD): ")
        record_expense(expense, amount, date)
        print("Expense recorded successfully.")

    elif choice == '2':
        year = int(input("Enter the year (e.g., 2023): "))
        month = int(input("Enter the month (1-12): "))
        generate_monthly_report(year, month)

    elif choice == '3':
        print("Exiting the program.")
        break
