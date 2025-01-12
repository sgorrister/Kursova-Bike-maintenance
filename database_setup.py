import sqlite3

def create_database():
    conn = sqlite3.connect('computer_components.db')
    cursor = conn.cursor()

    # Створення таблиці CPU
    cursor.execute('''
        CREATE TABLE CPU (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            series TEXT NOT NULL,
            generation TEXT NOT NULL,
            socket_type TEXT NOT NULL,
            cores INTEGER NOT NULL,
            frequency REAL NOT NULL,
            cache INTEGER NOT NULL,
            power_consumption INTEGER NOT NULL
        )
    ''')

    # Створення таблиці Motherboard
    cursor.execute('''
        CREATE TABLE Motherboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            socket_type TEXT NOT NULL,
            chipset TEXT NOT NULL,
            ram_slots INTEGER NOT NULL,
            ram_type TEXT NOT NULL,
            pcie_version TEXT NOT NULL,
            power_consumption INTEGER NOT NULL
        )
    ''')

    # Створення таблиці RAM
    cursor.execute('''
        CREATE TABLE RAM (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            memory_type TEXT NOT NULL,
            size INTEGER NOT NULL,
            frequency INTEGER NOT NULL,
            power_consumption INTEGER NOT NULL
        )
    ''')

    # Створення таблиці GPU
    cursor.execute('''
        CREATE TABLE GPU (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            vram INTEGER NOT NULL,
            power_consumption INTEGER NOT NULL,
            frequency INTEGER NOT NULL,
            length INTEGER NOT NULL,
            connectors_needed INTEGER NOT NULL
        )
    ''')

    # Створення таблиці Storage
    cursor.execute('''
        CREATE TABLE Storage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            storage_type TEXT NOT NULL,
            size TEXT NOT NULL,
            interface TEXT NOT NULL,
            power_consumption INTEGER NOT NULL
        )
    ''')

    # Створення таблиці ComputerCase
    cursor.execute('''
        CREATE TABLE ComputerCase (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            form_factor TEXT NOT NULL,
            max_gpu_length INTEGER NOT NULL,
            power_consumption INTEGER NOT NULL
        )
    ''')

    # Створення таблиці Cooling
    cursor.execute('''
        CREATE TABLE Cooling (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            cooling_type TEXT NOT NULL,
            size INTEGER NOT NULL,
            power_consumption INTEGER NOT NULL,
            socket_compatibility TEXT NOT NULL,
            max_tdp INTEGER NOT NULL
        )
    ''')

    # Створення таблиці PSU
    cursor.execute('''
        CREATE TABLE PSU (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            wattage INTEGER NOT NULL,
            certification TEXT NOT NULL,
            pcie_connectors INTEGER NOT NULL,
            power_consumption INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print("Database created successfully!")

if __name__ == "__main__":
    create_database()
