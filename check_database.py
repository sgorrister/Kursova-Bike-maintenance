import sqlite3

def check_cpu_table():
    conn = sqlite3.connect('computer_components.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM CPU")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    check_cpu_table()
