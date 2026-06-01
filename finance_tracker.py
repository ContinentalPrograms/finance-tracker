from database import create_table, add_transaction, view_all, summary

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def add_income():
    category = input("Category (e.g. Salary, Freelance, Gift): ")
    amount = get_number("Amount: ")
    note = input("Note (optional, press Enter to skip): ")
    add_transaction("income", category, amount, note)

def add_expense():
    category = input("Category (e.g. Food, Rent, Travel): ")
    amount = get_number("Amount: ")
    note = input("Note (optional, press Enter to skip): ")
    add_transaction("expense", category, amount, note)

def main():
    create_table()
    while True:
        print("\n==== Personal Finance Tracker ====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Transactions")
        print("4. Summary and Balance")
        print("5. Exit")
        choice = input("Choose 1-5: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_all()
        elif choice == "4":
            summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")

main()