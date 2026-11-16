from datetime import date

class Expense:
    def __init__(self, title, amount, category, expense_date=None):
        self.title = title
        self.amount = float(amount)
        self.category = category
        self.expense_date = expense_date if expense_date else date.today()

    def __str__(self):
        return f"{self.expense_date} | {self.title} [{self.category}] - Rs. {self.amount}"
    def __repr__(self):
        return f"Expense(title='{self.title}', amount={self.amount}, category='{self.category}', date={self.expense_date})"
    def __add__(self, other):
        if isinstance(other, Expense):
            return self.amount + other.amount
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, Expense):
            return self.amount > other.amount
        return NotImplemented
