import csv
class Expense:
    def __init__(self, title, amount, category):
        self.title = title
        self.amount = amount
        self.category = category
    def to_dict(self):
        
        return {"title": self.title, "amount": self.amount, "category": self.category}

def load_expense():
    try:
        with open("Expense.csv", "r") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []
def save_expense(expenses):
    feildnames = ["title", "amount", "category"]
    with open("Expense.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=feildnames)
        writer.writeheader()
        for exp in expenses:
            writer.writerow(exp)

def add_expense():
    expenses = load_expense()
    title = input("Title:")
    amount = int(input("Amount:"))
    category = input("Category:")
    new_expense = Expense(title, amount, category)
    expenses.append(new_expense.to_dict())
    save_expense(expenses)
    print("Expense Added")

def view_expenses():
    expenses = load_expense()
    if not expenses:
        print("No expenses yet!")
        return
    for exp in expenses:
        print(f"{exp['title']} - {exp['amount']} - {exp['category']}")

def total_expenses():
    expenses = load_expense()
    total = 0
    for exp in expenses:
        total += int(exp['amount'])
    print(f"Total: {total}")

def delete_expense():
    expenses = load_expense()
    title_to_delete = input("Enter title to delete:")

    new_list = []
    found = False
    for exp in expenses:
        if exp['title'] != title_to_delete:
            new_list.append(exp)
        else:
            found = True
    if found:
        save_expense(new_list)
        print(f"{title_to_delete} deleted!")
    else:
        print("Not Found!")


def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Choose: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice")

main()


