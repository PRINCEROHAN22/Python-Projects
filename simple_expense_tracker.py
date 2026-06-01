expenses = []

def add_expense(expense_name, category, amount):
    """Add an expense to the tracker."""
    expense = {
        "name": expense_name,
        "category": category,
        "amount": amount
    }
    expenses.append(expense)

def show_all_expenses():
    """Display all expenses."""
    try:
        if not expenses:
            print("No expenses to show.")
        else:
            print("Expenses:")
            for expense in expenses:
                print(f"{expense['name']} | {expense['category']} | ${expense['amount']:.2f}")
    except Exception as e:
        print(f"An error occurred while showing expenses")

def total_expenses():
    """Calculate and display the total amount of expenses."""
    try:
        total = sum(expense['amount'] for expense in expenses)
        print(f"Total Expenses: ${total:.2f}")
    except Exception as e:
        print(f"An error occurred while calculating total expenses")

def show_highest_category():
    """Display the category with the highest total expenses."""
    try:
        if not expenses:
            print("No expenses to analyze.")
            return
        
        category_totals = {}
        for expense in expenses:
            category = expense['category']
            if category in category_totals:
                category_totals[category] += expense['amount']
            else:
                category_totals[category] = expense['amount']
        highest_category = max(category_totals, key=category_totals.get)
        print(f"Highest Expense Category: {highest_category} with total ${category_totals[highest_category]:.2f}")
    except Exception as e:
        print(f"An error occurred while determining the highest category")

count=int(input("How many expenses do you want to add? "))
for _ in range(count):
    expense_name = input("Enter the expense name: ").lower().strip()
    category = input("Enter the expense category: ").lower().strip()
    amount = float(input("Enter the expense amount: "))
    add_expense(expense_name, category, amount)

show_all_expenses()
total_expenses()
show_highest_category()