expenses = []


def add_expense():
    name = input("Enter expense name: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    expense = {
        "name": name,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("\nExpense added successfully!")


def view_expenses():
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n===== ALL EXPENSES =====")

    for i, expense in enumerate(expenses, start=1):
        print(f"\nExpense {i}")
        print("Name:", expense["name"])
        print("Category:", expense["category"])
        print("Amount: ₹", expense["amount"])


def total_expense():
    if not expenses:
        print("\nNo expenses found.")
        return

    total = sum(expense["amount"] for expense in expenses)

    print("\nTotal Expense: ₹", total)


def category_expense():
    if not expenses:
        print("\nNo expenses found.")
        return

    category = input("Enter category: ")

    total = 0

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            total += expense["amount"]

    print(f"\nTotal expense in {category}: ₹{total}")


def highest_expense():
    if not expenses:
        print("\nNo expenses found.")
        return

    highest = max(expenses, key=lambda x: x["amount"])

    print("\n===== HIGHEST EXPENSE =====")
    print("Name:", highest["name"])
    print("Category:", highest["category"])
    print("Amount: ₹", highest["amount"])


def main():

    while True:

        print("\n========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Expense")
        print("4. Category-wise Expense")
        print("5. Find Highest Expense")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            category_expense()

        elif choice == "5":
            highest_expense()

        elif choice == "6":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("\nInvalid choice. Please try again.")


main()