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
            
            # 2. READ: View All Expenses
    def view_all(self):
        print(f"\n{'ID':<5} {'Amount':<10} {'Category':<15} {'Description'}")
        print("-" * 50)
        for e in self.expenses:
            print(f"{e['id']:<5} ${e['amt']:<9.2f} {e['cat']:<15} {e['desc']}")

    # 3. UPDATE: Edit Expense
    def edit_expense(self):
        try:
            eid = int(input("Enter Expense ID to edit: "))
            for e in self.expenses:
                if e['id'] == eid:
                    e['amt'] = float(input(f"New Amt (${e['amt']}): ") or e['amt'])
                    e['desc'] = input(f"New Desc ({e['desc']}): ") or e['desc']
                    print("Updated!")
                    return
            print("ID not found.")
        except ValueError:
            print("Invalid input.")

    # 4. DELETE: Remove Specific Expense
    def delete_expense(self):
        eid = int(input("Enter Expense ID to delete: "))
        self.expenses = [e for e in self.expenses if e['id'] != eid]
        print("Expense deleted.")
        # --- CATEGORY & BUDGET OPERATIONS ---

    # 5. CREATE: Add New Category (List Method: .append)
    def add_category(self):
        new_cat = input("New category name: ").strip()
        if new_cat and new_cat not in self.categories:
            self.categories.append(new_cat)
            print(f"'{new_cat}' added.")

    # 6. READ: Filter by Category (List Method: List Comprehension)
    def filter_by_cat(self):
        cat = input("Filter by which category? ")
        filtered = [e for e in self.expenses if e['cat'].lower() == cat.lower()]
        if filtered:
            for f in filtered: print(f)
        else:
            print("No expenses found for that category.")

    # 7. UPDATE: Set Monthly Budget
    def set_budget(self):
        self.budget = float(input(f"Current Budget (${self.budget}). Set new: "))
        print("Budget updated.")
       # 8. DELETE: Clear All Expenses (List Method: .clear)
    def reset_data(self):
        confirm = input("Are you sure you want to delete ALL expenses? (y/n): ")
        if confirm.lower() == 'y':
            self.expenses.clear()
            print("All data wiped.") 
            
def main():
    ft = FinanceTracker()
    menu = {
        "1": ("Add Expense", ft.add_expense),
        "2": ("View All", ft.view_all),
        "3": ("Edit Expense", ft.edit_expense),
        "4": ("Delete Expense", ft.delete_expense),
        "5": ("Add Category", ft.add_category),
        "6": ("Filter by Category", ft.filter_by_cat),
        "7": ("Set Budget", ft.set_budget),
        "8": ("Wipe All Data", ft.reset_data),
        "9": ("Exit", exit)
    }

    while True:
        print("\n--- PRO FINANCE TRACKER ---")
        for k, v in menu.items(): print(f"{k}. {v[0]}")
        
        choice = input("\nSelect: ")
        if choice in menu:
            if choice == "9": break
            menu[choice][1]()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()