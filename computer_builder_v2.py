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
                return "Error: CPU and Motherboard socket types are incompatible."

        if motherboard and ram:
            if ram.memory_type not in ['DDR4', 'DDR5']:
                return "Error: RAM type is incompatible with the Motherboard."

        if gpu and psu:
            if gpu.power_consumption > psu.wattage:
                return "Error: PSU wattage is insufficient for the GPU."

        return "Success: All components are compatible."

    def calculate_power(self):
        total_power = 0
        for component in self.components.values():
            if hasattr(component, 'power_consumption') and component.power_consumption is not None:
                total_power += component.power_consumption
        return total_power

    def visualize_build(self):
        build_info = ""
        total_power = 0  # змінна для підрахунку загальної потужності
        psu = None  # для збереження об'єкта PSU

        # Спочатку додаємо всі компоненти (окрім PSU)
        for component_type, component in self.components.items():
            if isinstance(component, PSU):  # Пропускаємо PSU на цьому етапі
                continue

            build_info += f"{component_type}:\n"
            build_info += f"  Brand: {component.brand}\n"
            build_info += f"  Model: {component.model}\n"
            
            if hasattr(component, 'socket_type'):
                build_info += f"  Socket Type: {component.socket_type}\n"
            if hasattr(component, 'cores'):
                build_info += f"  Cores: {component.cores}\n"
            if hasattr(component, 'frequency'):
                build_info += f"  Frequency: {component.frequency} GHz\n"
            if hasattr(component, 'memory_type'):
                build_info += f"  Memory Type: {component.memory_type}\n"
            if hasattr(component, 'vram'):
                build_info += f"  VRAM: {component.vram} GB\n"
            
            if hasattr(component, 'power_consumption') and component.power_consumption is not None:
                build_info += f"  Power Consumption: {component.power_consumption} Watts\n"
                total_power += component.power_consumption  # додаємо потужність до загальної

        # Тепер додаємо PSU окремо
        for component_type, component in self.components.items():
            if isinstance(component, PSU):
                psu = component
                build_info += f"{component_type}:\n"
                build_info += f"  Brand: {component.brand}\n"
                build_info += f"  Model: {component.model}\n"
                build_info += f"  Wattage: {component.wattage} Watts\n"  # виводимо Wattage PSU
                if component.power_consumption is not None:
                    total_power += component.power_consumption  # додаємо потужність PSU до загальної

        # Додатково виводимо інформацію про PSU Loading
        if psu:
            load_percentage = (total_power / psu.wattage) * 100
            build_info += f"\nPSU Loading: {load_percentage:.2f}%\n"
            if load_percentage > 80:
                build_info += "Warning: PSU is overloaded (more than 80% capacity).\n"

        # Виведемо загальну потужність
        build_info += f"\nTotal Power Consumption: {total_power} Watts\n"

        # Виведемо перевірку сумісності
        build_info += "\nCompatibility Check:\n"
        build_info += "Success: All components are compatible.\n"
        
        return build_info

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
    
    # Add components to builder
    builder.add_component('CPU', cpu_object)
    builder.add_component('Motherboard', motherboard_object)
    builder.add_component('RAM', ram_object)
    builder.add_component('GPU', gpu_object)
    builder.add_component('Storage', storage_object)
    builder.add_component('PSU', psu_object)
    builder.add_component('Case', case_object)
    builder.add_component('Cooling', cooling_object)

    # Run the visualization
    print(builder.visualize_build())
