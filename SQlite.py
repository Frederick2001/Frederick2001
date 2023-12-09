import sqlite3
import json

def convert_db_to_json(db_file, json_file, table_name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    if table_name.lower() == 'all':
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for table in tables:
            print(f"\033[93mConverting table '{table[0]}' to JSON...\033[0m")
            cursor.execute(f"SELECT * FROM {table[0]}")
            data = cursor.fetchall()
            json_data = json.dumps(data, indent=2)

            with open(f"{table[0]}.json", 'w') as f:
                f.write(json_data)
            print(f"\033[92mConversion for table '{table[0]}' completed.\033[0m")
    else:
        print(f"\033[93mConverting table '{table_name}' to JSON...\033[0m")
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()
        json_data = json.dumps(data, indent=2)

        with open(f"{table_name}.json", 'w') as f:
            f.write(json_data)
        print(f"\033[92mConversion for table '{table_name}' completed.\033[0m")

    conn.close()

# Prompt the user for input
db_file_name = input("\033[94mEnter the .db file name: \033[0m")

# Retrieve available tables
conn = sqlite3.connect(db_file_name)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
conn.close()

# Print "Available tables:" in green
print("\033[92mAvailable tables:\033[0m")

# Print table names in cyan
for table in tables:
    print("\033[96m" + table[0] + "\033[0m")

# Prompt the user to choose a table or enter 'all'
table_name_input = input("\033[94mEnter the table name (type 'all' for all tables): \033[0m")

# Convert to JSON
convert_db_to_json(db_file_name, f"{table_name_input}.json", table_name_input)