## Personal Finance Tracker CLI
A lightweight Command-Line Interface (CLI) application built in Python to help users manage their daily expenses, track categories, and stay within a monthly budget. This project demonstrates core programming concepts including CRUD operations, Data Relationships, and State Management using Python collections.

## Features (8 CRUD Operations)
The application is built around 8 distinct operations to provide a full management suite:

Add Expense (Create): Record new spending with an amount, category, and description.

View All Expenses (Read): Display a formatted table of all recorded transactions.

Edit Expense (Update): Modify the details of an existing expense by its unique ID.

Delete Expense (Delete): Remove a specific transaction from the records.

Add Category (Create): Dynamically expand the system by adding new spending categories.

Filter by Category (Read): View a subset of expenses belonging to a specific category.

Set Monthly Budget (Update): Define or change the total spending limit.

Wipe All Data (Delete): Clear the entire expense history for a fresh start.

## Technical Architecture
## Object Relationship
The system implements a One-to-Many (1:M) relationship:

Category → Expenses: One category (e.g., "Food") can be associated with multiple expense entries.

Validation: The system checks if a category exists before assigning it to an expense, ensuring data integrity.

 ## Data Structures
Lists: Used for storing the collection of categories and the master list of expenses.

Dictionaries: Each expense is represented as a dictionary for labeled data access:
