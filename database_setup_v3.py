import sqlite3

def create_database():
    conn = sqlite3.connect('computer_components.db')
    cursor = conn.cursor()

    # Create CPU table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS CPU (
        id INTEGER PRIMARY KEY,
        brand TEXT,
        model TEXT,
        series TEXT,
        generation TEXT,
        socket_type TEXT,
        cores INTEGER,
        frequency REAL,
        cache INTEGER,
        power_consumption INTEGER
    )
    ''')

    # Create Motherboard table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Motherboard (
        id INTEGER PRIMARY KEY,
        brand TEXT,
        model TEXT,
        socket_type TEXT,
        chipset TEXT,
        ram_slots INTEGER,
        pcie_version TEXT,
        power_consumption INTEGER
    )
    ''')

    # Create RAM table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS RAM (
        id INTEGER PRIMARY KEY,
        brand TEXT,
        model TEXT,
        memory_type TEXT,
        size INTEGER,
        frequency INTEGER,
        power_consumption INTEGER
    )
    ''')

    # Create GPU table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS GPU (
        id INTEGER PRIMARY KEY,
        brand TEXT,
        model TEXT,
        vram INTEGER,
        power_consumption INTEGER,
        frequency INTEGER
    )
    ''')

    # Create Storage table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Storage (
        id INTEGER PRIMARY KEY,
        brand TEXT,
        model TEXT,
        storage_type TEXT,
        size INTEGER,
        interface TEXT,
        power_consumption INTEGER
    )
    ''')

    # Create PSU table with power_consumption
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS PSU (
        id INTEGER PRIMARY KEY,
        brand TEXT,
        model TEXT,
        wattage INTEGER,
        certification TEXT,
        power_consumption INTEGER
    )
    ''')

    # Create ComputerCase table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ComputerCase (
        id INTEGER PRIMARY KEY,
        brand TEXT,
        model TEXT,
        form_factor TEXT,
        power_consumption INTEGER
    )
    ''')

    # Create Cooling table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cooling (
        id INTEGER PRIMARY KEY,
        brand TEXT,
        model TEXT,
        cooling_type TEXT,
        size INTEGER,
        power_consumption INTEGER
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
