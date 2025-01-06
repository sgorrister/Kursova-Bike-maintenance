import sqlite3

def populate_database():
    conn = sqlite3.connect('computer_components.db')
    cursor = conn.cursor()

    # Insert CPU data
    cursor.execute('''
    INSERT INTO CPU (brand, model, series, generation, socket_type, cores, frequency, cache, power_consumption)
    VALUES ('Intel', 'Core i5', 'Core i5', '13th Gen', 'LGA1700', 6, 3.5, 12, 65)
    ''')

    # Insert Motherboard data
    cursor.execute('''
    INSERT INTO Motherboard (brand, model, socket_type, chipset, ram_slots, pcie_version, power_consumption)
    VALUES ('ASUS', 'ROG Strix Z790', 'LGA1700', 'Z790', 4, '5.0', 0)
    ''')

    # Insert RAM data
    cursor.execute('''
    INSERT INTO RAM (brand, model, memory_type, size, frequency, power_consumption)
    VALUES ('Corsair', 'Vengeance LPX', 'DDR4', 16, 3200, 5)
    ''')

    # Insert GPU data
    cursor.execute('''
    INSERT INTO GPU (brand, model, vram, power_consumption, frequency)
    VALUES ('NVIDIA', 'RTX 4060', 8, 200, 1800)
    ''')

    # Insert Storage data
    cursor.execute('''
    INSERT INTO Storage (brand, model, storage_type, size, interface, power_consumption)
    VALUES ('Samsung', '970 EVO', 'SSD', 1000, 'M.2', 5)
    ''')

    # Insert PSU data
    cursor.execute('''
    INSERT INTO PSU (brand, model, wattage, certification, power_consumption)
    VALUES ('Corsair', 'RMX Series', 750, 'Gold', 10)
    ''')

    # Commit changes
    conn.commit()
    conn.close()
