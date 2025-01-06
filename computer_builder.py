import csv

class CPU:
    def __init__(self, brand, model, series, generation, socket_type, cores, frequency, cache):
        self.brand = brand
        self.model = model
        self.series = series
        self.generation = generation
        self.socket_type = socket_type
        self.cores = cores
        self.frequency = frequency  # in GHz
        self.cache = cache  # in MB

class Motherboard:
    def __init__(self, brand, model, socket_type, chipset, ram_slots, pcie_version):
        self.brand = brand
        self.model = model
        self.socket_type = socket_type
        self.chipset = chipset
        self.ram_slots = ram_slots
        self.pcie_version = pcie_version

class RAM:
    def __init__(self, brand, model, memory_type, size, frequency):
        self.brand = brand
        self.model = model
        self.memory_type = memory_type
        self.size = size  # in GB
        self.frequency = frequency  # in MHz

class GPU:
    def __init__(self, brand, model, vram, power_consumption, frequency):
        self.brand = brand
        self.model = model
        self.vram = vram  # in GB
        self.power_consumption = power_consumption  # in Watts
        self.frequency = frequency  # in MHz

class Storage:
    def __init__(self, brand, model, storage_type, size, interface):
        self.brand = brand
        self.model = model
        self.storage_type = storage_type
        self.size = size  # in GB or TB
        self.interface = interface

class PSU:
    def __init__(self, brand, model, wattage, certification):
        self.brand = brand
        self.model = model
        self.wattage = wattage  # in Watts
        self.certification = certification

class Case:
    def __init__(self, brand, model, form_factor):
        self.brand = brand
        self.model = model
        self.form_factor = form_factor

class Cooling:
    def __init__(self, brand, model, cooling_type, size):
        self.brand = brand
        self.model = model
        self.cooling_type = cooling_type
        self.size = size  # in mm

class ComponentDatabase:
    def __init__(self, csv_file):
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
        self.populate_database(csv_file)

    def populate_database(self, csv_file):
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Type'] == 'CPU':
                    self.components['CPU'].append(CPU(row['Brand'], row['Model'], row['Series'], row['Generation'], row['Socket'], int(row['Cores']), float(row['Frequency']), int(row['Cache'])))
                elif row['Type'] == 'Motherboard':
                    self.components['Motherboard'].append(Motherboard(row['Brand'], row['Model'], row['Socket'], row.get('Chipset', 'N/A'), int(row.get('RAMSlots', 0)), row.get('PCIeVersion', 'N/A')))
                elif row['Type'] == 'RAM':
                    self.components['RAM'].append(RAM(row['Brand'], row['Model'], row.get('MemoryType', 'N/A'), int(row['Size']), int(row['Frequency'])))
                elif row['Type'] == 'GPU':
                    self.components['GPU'].append(GPU(row['Brand'], row['Model'], int(row['VRAM']), int(row['PowerConsumption']), int(row['Frequency'])))
                elif row['Type'] == 'Storage':
                    self.components['Storage'].append(Storage(row['Brand'], row['Model'], row.get('StorageType', 'N/A'), int(row['Size']) if row['Size'].isdigit() else 0, row['Interface']))
                elif row['Type'] == 'PSU':
                    self.components['PSU'].append(PSU(row['Brand'], row['Model'], int(row.get('Wattage', 0)), row.get('Certification', 'N/A')))
                elif row['Type'] == 'Case':
                    self.components['Case'].append(Case(row['Brand'], row['Model'], row.get('FormFactor', 'N/A')))
                elif row['Type'] == 'Cooling':
                    self.components['Cooling'].append(Cooling(row['Brand'], row['Model'], row.get('CoolingType', 'N/A'), int(row['Size'])))

    def get_components(self, component_type):
        return self.components.get(component_type, [])

    def print_components(self):
        for component_type, components in self.components.items():
            print(f"{component_type}:")
            for component in components:
                print(f"  - {component.__dict__}")

class ComputerBuilder:
    def __init__(self):
        self.components = {}
        self.database = ComponentDatabase('components.csv')

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

        if gpu and motherboard:
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
    cpu = builder.database.get_components('CPU')[0]  # Get first CPU from database
    motherboard = builder.database.get_components('Motherboard')[0]  # Get first Motherboard from database
    ram = builder.database.get_components('RAM')[0]  # Get first RAM from database
    gpu = builder.database.get_components('GPU')[0]  # Get first GPU from database
    storage = builder.database.get_components('Storage')[0]  # Get first Storage from database
    psu = builder.database.get_components('PSU')[0]  # Get first PSU from database
    case = builder.database.get_components('Case')[0]  # Get first Case from database
    cooling = builder.database.get_components('Cooling')[0]  # Get first Cooling from database

    builder.add_component('CPU', cpu)
    builder.add_component('Motherboard', motherboard)
    builder.add_component('RAM', ram)
    builder.add_component('GPU', gpu)
    builder.add_component('Storage', storage)
    builder.add_component('PSU', psu)
    builder.add_component('Case', case)
    builder.add_component('Cooling', cooling)

    builder.database.print_components()  # Print all components for debugging
    print(builder.visualize_build())
    print(builder.check_compatibility())
    print(f"Total Power Requirement: {builder.calculate_power()}W")
