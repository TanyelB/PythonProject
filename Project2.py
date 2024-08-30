# Python Expense Tracker

def display_welcome_message():
    print("=======================================")
    print("  Welcome to the Expense Tracker App  ")
    print("  Track your expenses easily!  ")
    print("=======================================\n")

def display_thank_you_message():
    print("\n=======================================")
    print("  Thank you for using the Expense Tracker!  ")
    print("  We hope this helps you manage your finances better.  ")
    print("=======================================\n")

def log_expense():
    while True:
        try:
            amount = float(input("Enter the expense amount: $"))
            if amount <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive number for the amount.")
    
    categories = ["Food", "Transport", "Entertainment", "Utilities", "Other"]
    print("\nExpense Categories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    
    while True:
        try:
            category_index = int(input("Select a category by number (1-5): "))
            if category_index not in range(1, 6):
                raise ValueError
            category = categories[category_index - 1]
            break
        except ValueError:
            print("Please select a valid category number (1-5).")
    
    description = input("Enter a description for the expense: ")
    
    return {"amount": amount, "category": category, "description": description}

def display_summary(expenses):
    total_spent = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal amount spent: ${total_spent:.2f}")
    
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]
    
    print("\nSpending by category:")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")
    
    print("\nDetailed list of all expenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. ${expense['amount']:.2f} on {expense['category']} - {expense['description']}")

def run_expense_tracker():
    display_welcome_message()
    
    expenses = []
    
    while True:
        expenses.append(log_expense())
        
        more_expenses = input("Do you want to log another expense? (y/n): ").strip().lower()
        if more_expenses != 'y':
            break
    
    display_summary(expenses)
    display_thank_you_message()

if __name__ == "__main__":
    run_expense_tracker()
