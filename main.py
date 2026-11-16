from expense import Expense
from tracker import ExpenseTracker

tracker = ExpenseTracker()
tracker.load_from_file()

while True:
    print("\n---  MENU   ---")
    print("1. Add Expense ")
    print("2. Show All")
    print("3. Total")
    print("4. Delete")
    print("5. Update")
    print("6. Search")
    print("7. Filter By Category")
    print("8. Set budget and check")
    print("9. Category Summary")
    print("10. Save and Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            title = input("Title:")
            amount = float(input("Amount:"))
            category = input("Category:")
            tracker.add_expense(Expense(title, amount, category))
        elif choice == "2":
            tracker.show_all()
        elif choice == "3":
            print(f"Total: Rs. {tracker.get_total()}")
        elif choice == "4":
            index = int(input("Enter index:"))
            tracker.delete_expense(index)
        elif choice == "5":
            index =  int(input("Enter index:"))
            new_title = input("Title:")
            new_amount = float(input("Amount:"))
            new_category = input("Category:")
            tracker.update_expense(index,new_title, new_amount, new_category )
        elif choice == "6":
            keyword = input("Enter keyword:")
            tracker.search_by_title(keyword)
        elif choice == "7":
            category = input("Enter Category:")
            tracker.filter_by_category(category)
        elif choice == "8":
            amount = float(input("Enter your budget:"))
            tracker.set_budget(amount)
            tracker.check_budget()
        elif choice == "9":
            tracker.category_summary()
        elif choice == "10":
            tracker.save_to_file("expenses.csv")
            print("See you!")
            break
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid Input! Enter number not text.")