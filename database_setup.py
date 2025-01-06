import sqlite3

def create_tables():
    conn = sqlite3.connect('computer_components.db')
    cursor = conn.cursor()

    # Create CPU table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS CPU (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT,
        model TEXT,
        storage_type TEXT,
        size INTEGER,
        interface TEXT,
        power_consumption INTEGER
    )
    ''')

    # Create PSU table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS PSU (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT,
        model TEXT,
        form_factor TEXT,
        power_consumption INTEGER
    )
    ''')

    # Create Cooling table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cooling (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT,
        model TEXT,
        cooling_type TEXT,
        size INTEGER,
        power_consumption INTEGER
    )
    ''')

    conn.commit()
    conn.close()

def populate_database():
    conn = sqlite3.connect('computer_components.db')
    cursor = conn.cursor()

    # Insert multiple CPU data
    cpus = [
        ('Intel', 'Core i5-12400', 'Core i5', '12th Gen', 'LGA1700', 6, 2.5, 12, 65),
        ('Intel', 'Core i7-12700K', 'Core i7', '12th Gen', 'LGA1700', 12, 3.6, 25, 125),
        ('AMD', 'Ryzen 5 5600X', 'Ryzen 5', 'Zen 3', 'AM4', 6, 3.7, 32, 65),
        ('AMD', 'Ryzen 7 5800X', 'Ryzen 7', 'Zen 3', 'AM4', 8, 3.8, 32, 105),
        ('Intel', 'Core i9-12900K', 'Core i9', '12th Gen', 'LGA1700', 16, 3.2, 30, 125)
    ]
    cursor.executemany('''
    INSERT INTO CPU (brand, model, series, generation, socket_type, cores, frequency, cache, power_consumption)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', cpus)
    print("CPU data inserted.")

    # Insert multiple Motherboard data
    motherboards = [
        ('ASUS', 'ROG Strix Z690-E', 'LGA1700', 'Z690', 4, '5.0', 0),
        ('MSI', 'MAG B660M Mortar', 'LGA1700', 'B660', 4, '4.0', 0),
        ('Gigabyte', 'AORUS X570 Elite', 'AM4', 'X570', 4, '4.0', 0),
        ('ASRock', 'B550 Steel Legend', 'AM4', 'B550', 4, '4.0', 0),
        ('ASUS', 'TUF Gaming B550-PLUS', 'AM4', 'B550', 4, '4.0', 0)
    ]
    cursor.executemany('''
    INSERT INTO Motherboard (brand, model, socket_type, chipset, ram_slots, pcie_version, power_consumption)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', motherboards)
    print("Motherboard data inserted.")

    # Insert multiple RAM data
    rams = [
        ('Corsair', 'Vengeance LPX', 'DDR4', 16, 3200, 5),
        ('G.Skill', 'Ripjaws V', 'DDR4', 16, 3600, 5),
        ('Crucial', 'Ballistix', 'DDR4', 16, 3200, 5),
        ('Kingston', 'Fury Beast', 'DDR4', 16, 3200, 5),
        ('Corsair', 'Vengeance LPX', 'DDR4', 32, 3200, 10)
    ]
    cursor.executemany('''
    INSERT INTO RAM (brand, model, memory_type, size, frequency, power_consumption)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', rams)
    print("RAM data inserted.")

    # Insert multiple GPU data
    gpus = [
        ('NVIDIA', 'RTX 3060', 12, 200, 1800),
        ('NVIDIA', 'RTX 3070', 8, 220, 1800),
        ('AMD', 'RX 6700 XT', 12, 230, 2321),
        ('NVIDIA', 'RTX 3080', 10, 320, 1800),
        ('NVIDIA', 'RTX 3090', 24, 350, 1800)
    ]
    cursor.executemany('''
    INSERT INTO GPU (brand, model, vram, power_consumption, frequency)
    VALUES (?, ?, ?, ?, ?)
    ''', gpus)
    print("GPU data inserted.")

    # Insert multiple Storage data
    storages = [
        ('Samsung', '970 EVO', 'SSD', 1000, 'M.2', 5),
        ('Western Digital', 'Blue SN550', 'SSD', 500, 'M.2', 5),
        ('Crucial', 'MX500', 'SSD', 1000, 'SATA', 5),
        ('Seagate', 'Barracuda', 'HDD', 2000, 'SATA', 6),
        ('Samsung', '870 QVO', 'SSD', 2000, 'SATA', 5)
    ]
    cursor.executemany('''
    INSERT INTO Storage (brand, model, storage_type, size, interface, power_consumption)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', storages)
    print("Storage data inserted.")

    # Insert multiple PSU data
    psus = [
        ('Corsair', 'RMX Series', 750, 'Gold'),
        ('EVGA', 'SuperNOVA 750 G5', 750, 'Gold'),
        ('Seasonic', 'Focus GX-750', 750, 'Gold'),
        ('Thermaltake', 'Toughpower GF1', 750, 'Gold'),
        ('Cooler Master', 'V750 Gold', 750, 'Gold')
    ]
    cursor.executemany('''
    INSERT INTO PSU (brand, model, wattage, certification)
    VALUES (?, ?, ?, ?)
    ''', psus)
    print("PSU data inserted.")

    # Insert multiple Case data
    cases = [
        ('Fractal Design', 'Meshify C', 'ATX', 5),
        ('NZXT', 'H510', 'ATX', 5),
        ('Corsair', '4000D Airflow', 'ATX', 5),
        ('Cooler Master', 'MasterBox Q300L', 'Micro-ATX', 5),
        ('Thermaltake', 'V200', 'ATX', 5)
    ]
    cursor.executemany('''
    INSERT INTO ComputerCase (brand, model, form_factor, power_consumption)
    VALUES (?, ?, ?, ?)
    ''', cases)
    print("Case data inserted.")

    # Insert multiple Cooling data
    coolings = [
        ('Cooler Master', 'Hyper 212', 'Air', 120, 5),
        ('NZXT', 'Kraken X63', 'Liquid', 280, 10),
        ('Corsair', 'H100i RGB Platinum', 'Liquid', 240, 10),
        ('be quiet!', 'Dark Rock 4', 'Air', 120, 5),
        ('Thermaltake', 'Water 3.0', 'Liquid', 240, 10)
    ]
    cursor.executemany('''
    INSERT INTO Cooling (brand, model, cooling_type, size, power_consumption)
    VALUES (?, ?, ?, ?, ?)
    ''', coolings)
    print("Cooling data inserted.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()  # Create the tables first
    populate_database()  # Then populate the database
