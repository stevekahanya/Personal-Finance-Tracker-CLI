class FinanceTracker:
    def __init__(self):
        # 1:M Relationship - Expenses linked to Categories
        self.categories = ["Food", "Rent", "Transport", "Entertainment"]
        self.expenses = [
            {"id": 1, "amt": 50.0, "cat": "Food", "desc": "Grocery Store", "date": "2024-03-20"},
            {"id": 2, "amt": 1200.0, "cat": "Rent", "desc": "March Rent", "date": "2024-03-01"}
        ]
        self.next_id = 3
        self.budget = 2000.0

    # --- EXPENSE OPERATIONS (CRUD) ---
    
    # 1. CREATE: Add Expense
    def add_expense(self):
        try:
            amt = float(input("Amount: "))
            print(f"Available Categories: {self.categories}")
            cat = input("Category: ")
            if cat not in self.categories:
                print("Warning: Category doesn't exist. Adding to 'Misc'.")
                cat = "Misc"
            desc = input("Description: ")
            date = datetime.date.today().strftime("%Y-%m-%d")
            
            self.expenses.append({"id": self.next_id, "amt": amt, "cat": cat, "desc": desc, "date": date})
            self.next_id += 1
            print("Expense recorded!")
        except ValueError:
            print("Invalid amount.")