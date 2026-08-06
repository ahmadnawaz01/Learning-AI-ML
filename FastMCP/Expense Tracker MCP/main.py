import csv
import json
import os
import sqlite3
import tempfile
from fastmcp import FastMCP

# System temp folder is writable on cloud environments
DB_PATH = os.path.join(tempfile.gettempdir(), "expenses.db")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CATEGORIES_PATH = os.path.join(tempfile.gettempdir(), "categories.json")
BUDGETS_PATH = os.path.join(tempfile.gettempdir(), "budgets.json")

mcp = FastMCP("ExpenseTracker")


def init_db():
    with sqlite3.connect(DB_PATH) as c:
        c.execute("""
            CREATE TABLE IF NOT EXISTS expenses(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                subcategory TEXT DEFAULT '',
                note TEXT DEFAULT ''
            )
        """)


init_db()

# --- CORE TOOLS ---


@mcp.tool()
def add_expense(
    date: str,
    amount: float,
    category: str,
    subcategory: str = "",
    note: str = "",
) -> dict:
    """Add a new expense entry to the database."""
    with sqlite3.connect(DB_PATH) as c:
        cur = c.execute(
            "INSERT INTO expenses(date, amount, category, subcategory, note) VALUES (?,?,?,?,?)",
            (date, amount, category, subcategory, note),
        )
        return {"status": "ok", "id": cur.lastrowid}


@mcp.tool()
def list_expenses(start_date: str, end_date: str) -> list[dict]:
    """List expense entries within an inclusive date range (YYYY-MM-DD)."""
    with sqlite3.connect(DB_PATH) as c:
        cur = c.execute(
            """
            SELECT id, date, amount, category, subcategory, note
            FROM expenses
            WHERE date BETWEEN ? AND ?
            ORDER BY date ASC, id ASC
            """,
            (start_date, end_date),
        )
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, r)) for r in cur.fetchall()]


@mcp.tool()
def summarize(
    start_date: str, end_date: str, category: str = None
) -> list[dict]:
    """Summarize expenses by category within an inclusive date range (YYYY-MM-DD)."""
    with sqlite3.connect(DB_PATH) as c:
        query = """
            SELECT category, SUM(amount) AS total_amount, COUNT(*) AS transaction_count
            FROM expenses
            WHERE date BETWEEN ? AND ?
            """
        params = [start_date, end_date]

        if category:
            query += " AND category = ?"
            params.append(category)

        query += " GROUP BY category ORDER BY total_amount DESC"

        cur = c.execute(query, params)
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, r)) for r in cur.fetchall()]


@mcp.tool()
def delete_expense(expense_id: int) -> dict:
    """Delete an expense record by its unique ID."""
    with sqlite3.connect(DB_PATH) as c:
        cur = c.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        if cur.rowcount == 0:
            return {
                "status": "error",
                "message": f"No expense found with ID {expense_id}",
            }
        return {
            "status": "ok",
            "message": f"Expense #{expense_id} successfully deleted.",
        }


@mcp.tool()
def update_expense(
    expense_id: int,
    date: str = None,
    amount: float = None,
    category: str = None,
    subcategory: str = None,
    note: str = None,
) -> dict:
    """Update an existing expense by its ID. Only fields provided will be updated."""
    updates = []
    params = []

    if date is not None:
        updates.append("date = ?")
        params.append(date)
    if amount is not None:
        updates.append("amount = ?")
        params.append(amount)
    if category is not None:
        updates.append("category = ?")
        params.append(category)
    if subcategory is not None:
        updates.append("subcategory = ?")
        params.append(subcategory)
    if note is not None:
        updates.append("note = ?")
        params.append(note)

    if not updates:
        return {"status": "error", "message": "No fields provided to update."}

    query = f"UPDATE expenses SET {', '.join(updates)} WHERE id = ?"
    params.append(expense_id)

    with sqlite3.connect(DB_PATH) as c:
        cur = c.execute(query, params)
        if cur.rowcount == 0:
            return {
                "status": "error",
                "message": f"No expense found with ID {expense_id}",
            }
        return {
            "status": "ok",
            "message": f"Expense #{expense_id} updated successfully.",
        }


@mcp.tool()
def get_monthly_budget_status(year_month: str) -> dict:
    """Compare spending in a given month (YYYY-MM) against budgets."""
    if not os.path.exists(BUDGETS_PATH):
        default_budgets = {
            "Food": 500.0,
            "Transport": 150.0,
            "Utilities": 200.0,
            "Entertainment": 100.0,
        }
        with open(BUDGETS_PATH, "w", encoding="utf-8") as f:
            json.dump(default_budgets, f, indent=2)

    with open(BUDGETS_PATH, "r", encoding="utf-8") as f:
        budgets = json.load(f)

    start_date = f"{year_month}-01"
    end_date = f"{year_month}-31"

    with sqlite3.connect(DB_PATH) as c:
        cur = c.execute(
            """
            SELECT category, SUM(amount) 
            FROM expenses 
            WHERE date BETWEEN ? AND ?
            GROUP BY category
            """,
            (start_date, end_date),
        )
        actuals = dict(cur.fetchall())

    results = {}
    for category, budget in budgets.items():
        spent = actuals.get(category, 0.0)
        remaining = budget - spent
        results[category] = {
            "budget": budget,
            "spent": spent,
            "remaining": remaining,
            "is_over_budget": spent > budget,
        }

    return {"month": year_month, "budget_status": results}


@mcp.tool()
def get_top_spending_category(start_date: str, end_date: str) -> dict:
    """Identify the single category with the highest spending in a date range."""
    with sqlite3.connect(DB_PATH) as c:
        cur = c.execute(
            """
            SELECT category, SUM(amount) AS total
            FROM expenses
            WHERE date BETWEEN ? AND ?
            GROUP BY category
            ORDER BY total DESC
            LIMIT 1
            """,
            (start_date, end_date),
        )
        row = cur.fetchone()
        if not row:
            return {"message": "No expenses found in this range."}
        return {
            "top_category": row[0],
            "total_spent": row[1],
            "period": f"{start_date} to {end_date}",
        }


@mcp.tool()
def export_expenses_csv(start_date: str, end_date: str, filename: str) -> dict:
    """Export expenses in a date range to a CSV file in temp dir."""
    export_path = os.path.join(tempfile.gettempdir(), filename)

    with sqlite3.connect(DB_PATH) as c:
        cur = c.execute(
            """
            SELECT id, date, amount, category, subcategory, note
            FROM expenses
            WHERE date BETWEEN ? AND ?
            ORDER BY date ASC
            """,
            (start_date, end_date),
        )
        rows = cur.fetchall()

    with open(export_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["ID", "Date", "Amount", "Category", "Subcategory", "Note"]
        )
        writer.writerows(rows)

    return {
        "status": "ok",
        "file_path": export_path,
        "total_records_exported": len(rows),
    }


@mcp.resource("expense://categories", mime_type="application/json")
def categories():
    """Resource returning valid categories from categories.json."""
    if not os.path.exists(CATEGORIES_PATH):
        default_categories = {
            "Food": ["Groceries", "Restaurants"],
            "Transport": ["Fuel", "Public Transit"],
            "Utilities": ["Electricity", "Internet"],
            "Entertainment": ["Movies", "Games"],
        }
        with open(CATEGORIES_PATH, "w", encoding="utf-8") as f:
            json.dump(default_categories, f, indent=2)

    with open(CATEGORIES_PATH, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
<<<<<<< HEAD
    mcp.run(transport="sse", host="0.0.0.0", port=5000)
=======
  mcp.run(transport="sse", host='0.0.0.0',port=5000)
>>>>>>> e96e900fcd3da18b2c6f9d807b781e16c73cb6aa
