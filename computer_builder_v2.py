import sqlite3
from component_selector import select_component  # Import the component selection function

class CPU:
    def __init__(self, brand, model, series, generation, socket_type, cores, frequency, cache, power_consumption):
        self.brand = brand
        self.model = model
        self.series = series
        self.generation = generation
        self.socket_type = socket_type
        self.cores = cores
        self.frequency = frequency  # in GHz
        self.cache = cache  # in MB
        self.power_consumption = power_consumption  # in Watts

class Motherboard:
    def __init__(self, brand, model, socket_type, chipset, ram_slots, pcie_version, power_consumption):
        self.brand = brand
        self.model = model
        self.socket_type = socket_type
        self.chipset = chipset
        self.ram_slots = ram_slots
        self.pcie_version = pcie_version
        self.power_consumption = power_consumption  # in Watts

class RAM:
    def __init__(self, brand, model, memory_type, size, frequency, power_consumption):
        self.brand = brand
        self.model = model
        self.memory_type = memory_type
        self.size = size  # in GB
        self.frequency = frequency  # in MHz
        self.power_consumption = power_consumption  # in Watts

class GPU:
    def __init__(self, brand, model, vram, power_consumption, frequency):
        self.brand = brand
        self.model = model
        self.vram = vram  # in GB
        self.power_consumption = power_consumption  # in Watts
        self.frequency = frequency  # in MHz

class Storage:
    def __init__(self, brand, model, storage_type, size, interface, power_consumption):
        self.brand = brand
        self.model = model
        self.storage_type = storage_type
        self.size = size  # in GB or TB
        self.interface = interface
        self.power_consumption = power_consumption  # in Watts

class PSU:
    def __init__(self, brand, model, wattage, certification, power_consumption):
        self.brand = brand
        self.model = model
        self.wattage = wattage  # in Watts
        self.certification = certification
        self.power_consumption = power_consumption  # in Watts

class ComputerCase:
    def __init__(self, brand, model, form_factor, power_consumption):
        self.brand = brand
        self.model = model
        self.form_factor = form_factor
        self.power_consumption = power_consumption  # in Watts

class Cooling:
    def __init__(self, brand, model, cooling_type, size, power_consumption):
        self.brand = brand
        self.model = model
        self.cooling_type = cooling_type
        self.size = size  # in mm
        self.power_consumption = power_consumption  # in Watts

class ComponentDatabase:
    def __init__(self, db_file):
        self.components = {
            'CPU': [],
            'Motherboard': [],
            'RAM': [],
            'GPU': [],
            'Storage': [],
            'PSU': [],
            'Case': [],
            'Cooling': []
        }
        self.populate_database(db_file)

    def populate_database(self, db_file):
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Load CPU data
        cursor.execute("SELECT * FROM CPU")
        for row in cursor.fetchall():
            self.components['CPU'].append(CPU(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

        # Load Motherboard data
        cursor.execute("SELECT * FROM Motherboard")
        for row in cursor.fetchall():
            self.components['Motherboard'].append(Motherboard(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

        # Load RAM data
        cursor.execute("SELECT * FROM RAM")
        for row in cursor.fetchall():
            self.components['RAM'].append(RAM(row[1], row[2], row[3], row[4], row[5], row[6]))

        # Load GPU data
        cursor.execute("SELECT * FROM GPU")
        for row in cursor.fetchall():
            self.components['GPU'].append(GPU(row[1], row[2], row[3], row[4], row[5]))

        # Load Storage data
        cursor.execute("SELECT * FROM Storage")
        for row in cursor.fetchall():
            self.components['Storage'].append(Storage(row[1], row[2], row[3], row[4], row[5], row[6]))

       # Load PSU data
        cursor.execute("SELECT * FROM PSU")
        for row in cursor.fetchall():
            try:
                brand = row[1]
                model = row[2]
                wattage = int(row[3]) if len(row) > 3 and row[3] else 0
                certification = row[4] if len(row) > 4 else "Unknown"
                power_consumption = int(row[5]) if len(row) > 5 and row[5] else 0
                self.components['PSU'].append(PSU(brand, model, wattage, certification, power_consumption))
            except IndexError as e:
                print(f"Error processing row {row}: {e}")

        # Load Case data
        cursor.execute("SELECT * FROM ComputerCase")
        for row in cursor.fetchall():
            self.components['Case'].append(ComputerCase(row[1], row[2], row[3], row[4]))

        # Load Cooling data
        cursor.execute("SELECT * FROM Cooling")
        for row in cursor.fetchall():
            self.components['Cooling'].append(Cooling(row[1], row[2], row[3], row[4], row[5]))

        conn.close()

    def get_components(self, component_type):
        return self.components.get(component_type, [])

class ComputerBuilder:
    def __init__(self):
        self.components = {}
        self.database = ComponentDatabase('computer_components.db')

    def add_component(self, component_type, component):
        self.components[component_type] = component

    def check_compatibility(self):
        cpu = self.components.get('CPU')
        motherboard = self.components.get('Motherboard')
        ram = self.components.get('RAM')
        gpu = self.components.get('GPU')
        storage = self.components.get('Storage')
        psu = self.components.get('PSU')

        if cpu and motherboard:
            if cpu.socket_type != motherboard.socket_type:
                return "CPU and Motherboard socket types are incompatible."

        if motherboard and ram:
            if ram.memory_type not in ['DDR4', 'DDR5']:
                return "RAM type is incompatible with the Motherboard."

        if gpu and psu:
            if gpu.power_consumption > psu.wattage:
                return "PSU wattage is insufficient for the GPU."

        return "All components are compatible."

    def calculate_power(self):
        total_power = 0
        for component in self.components.values():
            total_power += component.power_consumption
        return total_power  # Total power consumption of all components

    def visualize_build(self):
        return self.components

# Example usage
if __name__ == "__main__":
    builder = ComputerBuilder()
    
    # Integrate component selection
    cpu = select_component("CPU")
    motherboard = select_component("Motherboard")
    ram = select_component("RAM")
    gpu = select_component("GPU")
    storage = select_component("Storage")
    psu = select_component("PSU")
    case = select_component("ComputerCase")
    cooling = select_component("Cooling")

    # Wrap the tuples into their corresponding class objects
    cpu_object = CPU(*cpu[1:])
    motherboard_object = Motherboard(*motherboard[1:])
    ram_object = RAM(*ram[1:])
    gpu_object = GPU(*gpu[1:])
    storage_object = Storage(*storage[1:])
    psu_object = PSU(*psu[1:])
    case_object = ComputerCase(*case[1:])
    cooling_object = Cooling(*cooling[1:])

    # Add components to the builder
    builder.add_component('CPU', cpu_object)
    builder.add_component('Motherboard', motherboard_object)
    builder.add_component('RAM', ram_object)
    builder.add_component('GPU', gpu_object)
    builder.add_component('Storage', storage_object)
    builder.add_component('PSU', psu_object)
    builder.add_component('Case', case_object)
    builder.add_component('Cooling', cooling_object)

    # Visualize the build and check compatibility
    print(builder.visualize_build())
    print(builder.check_compatibility())
