from openai import OpenAI
import sqlite3

# # Set up the OpenAI API client
# client = OpenAI()  # Assumes OPENAI_API_KEY environment variable is set
# MODEL_NAME = "gpt-4o"  # Using GPT-4o model, adjust as needed

# Step 1 :: Connect to the test database (or create it if it doesn't exist)
conn = sqlite3.connect("test_db.db")
cursor = conn.cursor()

# Drop if exists
cursor.execute("DROP TABLE IF EXISTS employees")

# Create a sample table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        salary INTEGER
    )
""")

# Insert sample data
sample_data = [
    (1, "John Doe", "Sales", 50000),
    (2, "Jane Smith", "Engineering", 75000),
    (3, "Mike Johnson", "Sales", 60000),
    (4, "Emily Brown", "Engineering", 80000),
    (5, "David Lee", "Marketing", 55000)
]
cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", sample_data)
conn.commit()