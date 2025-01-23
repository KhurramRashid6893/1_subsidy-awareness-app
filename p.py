import sqlite3

# Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect("todo_list.db")

# Create a cursor to interact with the database
cursor = connection.cursor()

# Step 1: Create the table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT 0
)
''')
print("Table created successfully!")

# Step 2: Insert tasks into the table
cursor.execute("INSERT INTO tasks (task, completed) VALUES (?, ?)", ("Learn SQLite", 0))
cursor.execute("INSERT INTO tasks (task, completed) VALUES (?, ?)", ("Complete Python project", 0))

# Commit the changes to the database
connection.commit()
print("Tasks added successfully!")

# Step 3: Retrieve and display all tasks
cursor.execute("SELECT * FROM tasks")
tasks = cursor.fetchall()

print("\nCurrent tasks:")
for task in tasks:
    print(f"ID: {task[0]}, Task: {task[1]}, Completed: {'Yes' if task[2] else 'No'}")

# Step 4: Update a task's completion status
cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (1,))
connection.commit()
print("\nTask updated successfully!")

# Display updated tasks
cursor.execute("SELECT * FROM tasks")
tasks = cursor.fetchall()

print("\nUpdated tasks:")
for task in tasks:
    print(f"ID: {task[0]}, Task: {task[1]}, Completed: {'Yes' if task[2] else 'No'}")

# Step 5: Delete a task
cursor.execute("DELETE FROM tasks WHERE id = ?", (2,))
connection.commit()
print("\nTask deleted successfully!")

# Display remaining tasks
cursor.execute("SELECT * FROM tasks")
tasks = cursor.fetchall()

print("\nRemaining tasks:")
for task in tasks:
    print(f"ID: {task[0]}, Task: {task[1]}, Completed: {'Yes' if task[2] else 'No'}")

# Close the database connection
connection.close()
print("\nDatabase connection closed!")
