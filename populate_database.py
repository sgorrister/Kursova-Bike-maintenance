import sqlite3

def populate_database():
    conn = sqlite3.connect('computer_components.db')
    cursor = conn.cursor()

    # Наповнення таблиці CPU
    cpus = [
        ("Intel", "Core i9-12900K", "Core i9", "12th Gen", "LGA1700", 16, 3.2, 30, 125),
        ("AMD", "Ryzen 9 5900X", "Ryzen 9", "Zen 3", "AM4", 12, 3.7, 64, 105),
        ("Intel", "Core i7-12700F", "Core i7", "12th Gen", "LGA1700", 12, 2.1, 25, 65),
        ("AMD", "Ryzen 5 5600X", "Ryzen 5", "Zen 3", "AM4", 6, 3.7, 32, 65),
        ("Intel", "Core i5-11600K", "Core i5", "11th Gen", "LGA1200", 6, 3.9, 12, 125),
    ]
    cursor.executemany('''
        INSERT INTO CPU (brand, model, series, generation, socket_type, cores, frequency, cache, power_consumption)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', cpus)

    # Наповнення таблиці Motherboard
    motherboards = [
        ("MSI", "MAG Z690 TOMAHAWK", "LGA1700", "Z690", 4, "DDR5", "5.0", 15),
        ("ASUS", "ROG STRIX B550-F", "AM4", "B550", 4, "DDR4", "4.0", 13),
        ("Gigabyte", "B660M DS3H", "LGA1700", "B660", 2, "DDR4", "4.0", 10),
        ("ASRock", "X570 Steel Legend", "AM4", "X570", 4, "DDR4", "4.0", 17),
        ("MSI", "B450 TOMAHAWK MAX", "AM4", "B450", 4, "DDR4", "3.0", 12),
    ]
    cursor.executemany('''
        INSERT INTO Motherboard (brand, model, socket_type, chipset, ram_slots, ram_type, pcie_version, power_consumption)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', motherboards)

    # Наповнення таблиці RAM
    rams = [
        ("Corsair", "Vengeance LPX", "DDR4", 16, 3200, 6),
        ("G.Skill", "Trident Z", "DDR4", 32, 3600, 8),
        ("Kingston", "HyperX Fury", "DDR4", 8, 2666, 5),
        ("TeamGroup", "T-Force Delta", "DDR5", 16, 5200, 7),
        ("Crucial", "Ballistix", "DDR4", 16, 3000, 6),
    ]
    cursor.executemany('''
        INSERT INTO RAM (brand, model, memory_type, size, frequency, power_consumption)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', rams)

    # Наповнення таблиці GPU
    gpus = [
        ("NVIDIA", "RTX 3080", 10, 320, 1440, 300, 2),
        ("AMD", "Radeon RX 6800 XT", 16, 300, 2015, 267, 2),
        ("NVIDIA", "RTX 3060 Ti", 8, 200, 1665, 242, 1),
        ("AMD", "Radeon RX 6700 XT", 12, 230, 2321, 267, 2),
        ("NVIDIA", "GTX 1660 Super", 6, 125, 1785, 223, 1),
        ("NVIDIA", "RTX 4090", 24, 450, 2520, 400, 3),
    ]
    cursor.executemany('''
        INSERT INTO GPU (brand, model, vram, power_consumption, frequency, length, connectors_needed)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', gpus)

    # Наповнення таблиці Storage
    storages = [
        ("Samsung", "970 Evo Plus", "SSD", "1TB", "NVMe", 5),
        ("Seagate", "Barracuda", "HDD", "2TB", "SATA", 8),
        ("Western Digital", "Blue SN570", "SSD", "500GB", "NVMe", 4),
        ("Crucial", "MX500", "SSD", "1TB", "SATA", 6),
        ("Toshiba", "P300", "HDD", "1TB", "SATA", 7),
    ]
    cursor.executemany('''
        INSERT INTO Storage (brand, model, storage_type, size, interface, power_consumption)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', storages)

    # Наповнення таблиці ComputerCase
    cases = [
        ("NZXT", "H510", "ATX", 381, 0),
        ("Cooler Master", "MasterBox Q300L", "mATX", 360, 0),
        ("Corsair", "4000D Airflow", "ATX", 360, 0),
        ("Fractal Design", "Meshify C", "ATX", 315, 0),
        ("Thermaltake", "V200", "ATX", 320, 0),
    ]
    cursor.executemany('''
        INSERT INTO ComputerCase (brand, model, form_factor, max_gpu_length, power_consumption)
        VALUES (?, ?, ?, ?, ?)
    ''', cases)

    # Наповнення таблиці Cooling
    coolings = [
        ("Noctua", "NH-D15", "Air", 165, 6, "LGA1700,AM4", 220),
        ("Corsair", "iCUE H150i", "Liquid", 360, 7, "LGA1700,AM4", 300),
        ("Cooler Master", "Hyper 212", "Air", 160, 4, "LGA1200,AM4", 150),
        ("NZXT", "Kraken X63", "Liquid", 280, 5, "LGA1700,AM4", 280),
        ("Be Quiet!", "Dark Rock Pro 4", "Air", 135, 6, "LGA1200,AM4", 250),
        ("Intel", "Box", "Air", 100, 6, "LGA1200,AM4", 100),
    ]
    cursor.executemany('''
        INSERT INTO Cooling (brand, model, cooling_type, size, power_consumption, socket_compatibility, max_tdp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', coolings)

    # Наповнення таблиці PSU
    psus = [
        ("Corsair", "RM750x", 750, "80+ Gold", 4, 10),
        ("EVGA", "SuperNOVA 650 G5", 650, "80+ Gold", 4, 8),
        ("Seasonic", "Focus GX-550", 550, "80+ Gold", 3, 7),
        ("Cooler Master", "MWE 500", 500, "80+ Bronze", 2, 6),
        ("Thermaltake", "Toughpower GF1 850W", 850, "80+ Gold", 6, 12),
        ("GameMax", "ATX-300 SFX 300W", 300, "80+", 2, 10),


    ]
    cursor.executemany('''
        INSERT INTO PSU (brand, model, wattage, certification, pcie_connectors, power_consumption)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', psus)

    conn.commit()
    conn.close()
    print("Database populated successfully!")

if __name__ == "__main__":
    populate_database()