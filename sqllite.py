import sqlite3

# Connect to a database (creates it if it doesn't exist)
conn = sqlite3.connect('/Users/kiransripathi/Desktop/Python/test_database.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

# Define the SQL query
sql = '''INSERT INTO users (name, email)
         VALUES (?, ?)'''

# Define the data to be inserted
users_data = [
    ('John Doe', 'john.doe@abc.com'),
    ('Jane Smith', 'jane.smith@abc.com'),
    ('Mike Gabe', 'mike.gabe@abc.com')
]

# Execute the query with multiple records
cursor.executemany(sql, users_data)

# Commit the changes
conn.commit()

# Query the database
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Close the connection
conn.close()
