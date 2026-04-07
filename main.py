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