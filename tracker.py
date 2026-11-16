import csv
from datetime import date
from expense import Expense
class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.budget = 0.0
    def add_expense(self, expense):
        if isinstance(expense, Expense):
            self.expenses.append(expense)
            print(f"Added: {expense}")
            return True
        else:
            print("Invalid expense object!")
            return False
        
    def show_all(self):
        if not self.expenses:
            print("No expense yet")
        else:
            for i, e in enumerate(self.expenses):
               print(f"{i}. {e}")

    def __len__(self):
        return len(self.expenses)
    
    def get_total(self):
        return sum(e.amount for e in self.expenses)
    
    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            removed = self.expenses.pop(index)
            print(f"{removed} is remove from expenses.")
            return removed
        else:
            print(f"Invalid index: {index}. Valid range is 0 to {len(self.expenses)-1}")
            return None
        
    def update_expense(self, index, new_title, new_amount, new_category):
        if 0 <= index < len(self.expenses):
            expense = self.expenses[index]
            expense.title = new_title
            expense.amount = float(new_amount)
            expense.category = new_category
            print(f"Updated at {index}: {expense}")
            return True
        else:
            print(f"Invalid index: {index}")
            return False
        
    def search_by_title(self,keyword):
        found = False
        for e in self.expenses:
            if keyword.lower() in e.title.lower():
                print(e)
                found = True
        if not found:
            print("Search title doesn't exist")
    
    def filter_by_category(self, category):
        found = False
        for e in self.expenses:
            if category.lower() == e.category.lower():
                print(e)
                found = True
        if not found:
            print("Required category doesn't exist")

    def set_budget(self, amount):
        self.budget = float(amount)
        print(f"Budget set to Rs. {self.budget}")
    
    def check_budget(self):
        total  = self.get_total()
        if self.budget == 0:
            print("Budget not set yet!")
            return
        if total > self.budget:
            print("💀 Budget exceeded.")
        else:
            remaining = self.budget - total
            print(f"✅ Within budget, Remaining: Rs.{remaining} ")

    def category_summary(self):
        summary = {}
        for e in self.expenses:
            if e.category in summary:
                summary[e.category] += e.amount
            else:
                summary[e.category] = e.amount
        for category, total in summary.items():
            print(f"{category}: Rs. {total}")

    def save_to_file(self, filename="expenses.csv"):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Amount", "Category", "Date"])
            for e in self.expenses:
                writer.writerow([e.title, e.amount, e.category, e.expense_date])
        print("Saved successfully.")
    
    def load_from_file(self, filename="expenses.csv"):
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader, None) # header ko skip krta h
                self.expenses = [] # old data clear
                for row in reader:
                    if len(row) < 3:
                        continue
                    title = row[0]
                    amount = float(row[1])
                    category = row[2]
                    exp_date = row[3] if len(row) > 3 else None
                    if exp_date:
                        try:
                            y, m, d, = map(int, exp_date.split("-"))
                            exp_date = date(y, m, d)
                        except:
                            exp_date = None
                    self.expenses.append(Expense(title, amount, category,))
            print("Loaded successfully.")
        except FileNotFoundError:
            print("No saved file exist")
                     


