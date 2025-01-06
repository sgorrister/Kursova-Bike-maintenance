import sqlite3

def populate_database():
    conn = sqlite3.connect('computer_components.db')
    cursor = conn.cursor()

    # Insert CPU data
    cursor.execute('''
    INSERT INTO CPU (brand, model, series, generation, socket_type, cores, frequency, cache, power_consumption)
    VALUES ('Intel', 'Core i5', 'Core i5', '13th Gen', 'LGA1700', 6, 3.5, 12, 65)
    ''')
    print("CPU data inserted.")

    # Insert Motherboard data
    cursor.execute('''
    INSERT INTO Motherboard (brand, model, socket_type, chipset, ram_slots, pcie_version, power_consumption)
    VALUES ('ASUS', 'ROG Strix Z790', 'LGA1700', 'Z790', 4, '5.0', 0)
    ''')
    print("Motherboard data inserted.")

    # Insert RAM data
    cursor.execute('''
    INSERT INTO RAM (brand, model, memory_type, size, frequency, power_consumption)
    VALUES ('Corsair', 'Vengeance LPX', 'DDR4', 16, 3200, 5)
    ''')
    print("RAM data inserted.")

    # Insert GPU data
    cursor.execute('''
    INSERT INTO GPU (brand, model, vram, power_consumption, frequency)
    VALUES ('NVIDIA', 'RTX 4060', 8, 200, 1800)
    ''')
    print("GPU data inserted.")

    # Insert Storage data
    cursor.execute('''
    INSERT INTO Storage (brand, model, storage_type, size, interface, power_consumption)
    VALUES ('Samsung', '970 EVO', 'SSD', 1000, 'M.2', 5)
    ''')
    print("Storage data inserted.")

    # Insert PSU data
    cursor.execute('''
    INSERT INTO PSU (brand, model, wattage, certification)
    VALUES ('Corsair', 'RMX Series', 750, 'Gold')
    ''')
    print("PSU data inserted.")

    # Insert Case data
    cursor.execute('''
    INSERT INTO ComputerCase (brand, model, form_factor, power_consumption)
    VALUES ('Fractal Design', 'Meshify C', 'ATX', 5)
    ''')
    print("Case data inserted.")

    # Insert Cooling data
    cursor.execute('''
    INSERT INTO Cooling (brand, model, cooling_type, size, power_consumption)
    VALUES ('Cooler Master', 'Hyper 212', 'Air', 120, 5)
    ''')
    print("Cooling data inserted.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    populate_database()
