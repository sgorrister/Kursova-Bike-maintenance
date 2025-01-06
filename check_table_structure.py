import sqlite3

def check_table_structure():
    conn = sqlite3.connect('computer_components.db')
    cursor = conn.cursor()

    # Check structure of PSU table
    cursor.execute("PRAGMA table_info(PSU);")
    columns = cursor.fetchall()

    for column in columns:
        print(column)

    conn.close()

if __name__ == "__main__":
    check_table_structure()
