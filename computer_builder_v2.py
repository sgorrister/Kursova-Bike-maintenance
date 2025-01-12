import sqlite3
from component_selector import select_component


class CPU:
    def __init__(self, brand, model, series, generation, socket_type, cores, frequency, cache, power_consumption):
        self.brand = brand
        self.model = model
        self.series = series
        self.generation = generation
        self.socket_type = socket_type
        self.cores = cores
        self.frequency = frequency  # GHz
        self.cache = cache  # MB
        self.power_consumption = power_consumption  # Watts


class Motherboard:
    def __init__(self, brand, model, socket_type, chipset, ram_slots, ram_type, pcie_version, power_consumption):
        self.brand = brand
        self.model = model
        self.socket_type = socket_type
        self.chipset = chipset
        self.ram_slots = ram_slots
        self.ram_type = ram_type
        self.pcie_version = pcie_version
        self.power_consumption = power_consumption  # Watts

class RAM:
    def __init__(self, brand, model, memory_type, size, frequency, power_consumption):
        self.brand = brand
        self.model = model
        self.memory_type = memory_type
        self.size = size  # GB
        self.frequency = frequency  # MHz
        self.power_consumption = power_consumption  # Watts


class GPU:
    def __init__(self, brand, model, vram, power_consumption, frequency, length, connectors_needed):
        self.brand = brand
        self.model = model
        self.vram = vram  # GB
        self.power_consumption = power_consumption  # Watts
        self.frequency = frequency  # MHz
        self.length = length  # mm
        self.connectors_needed = connectors_needed  # Number of PCIe connectors


class Storage:
    def __init__(self, brand, model, storage_type, size, interface, power_consumption):
        self.brand = brand
        self.model = model
        self.storage_type = storage_type
        self.size = size  # GB or TB
        self.interface = interface
        self.power_consumption = power_consumption  # Watts


class PSU:
    def __init__(self, brand, model, wattage, certification, pcie_connectors, power_consumption=0):
        self.brand = brand
        self.model = model
        self.wattage = wattage  # Watts
        self.certification = certification
        self.pcie_connectors = pcie_connectors  # Number of PCIe connectors available
        self.power_consumption = power_consumption  # Watts


class ComputerCase:
    def __init__(self, brand, model, form_factor, max_gpu_length, power_consumption=0):
        self.brand = brand
        self.model = model
        self.form_factor = form_factor
        self.max_gpu_length = max_gpu_length  # mm
        self.power_consumption = power_consumption  # Watts


class Cooling:
    def __init__(self, brand, model, cooling_type, size, power_consumption, socket_compatibility, max_tdp):
        self.brand = brand
        self.model = model
        self.cooling_type = cooling_type
        self.size = size  # mm
        self.power_consumption = power_consumption  # Watts
        self.socket_compatibility = socket_compatibility  # List of supported sockets
        self.max_tdp = max_tdp  # Maximum cooling capacity in Watts


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
            self.components['CPU'].append(CPU(*row[1:]))

        # Load Motherboard data
        cursor.execute("SELECT * FROM Motherboard")
        for row in cursor.fetchall():
            self.components['Motherboard'].append(Motherboard(*row[1:]))

        # Load RAM data
        cursor.execute("SELECT * FROM RAM")
        for row in cursor.fetchall():
            self.components['RAM'].append(RAM(*row[1:]))

        # Load GPU data
        cursor.execute("SELECT * FROM GPU")
        for row in cursor.fetchall():
            self.components['GPU'].append(GPU(*row[1:]))

        # Load Storage data
        cursor.execute("SELECT * FROM Storage")
        for row in cursor.fetchall():
            self.components['Storage'].append(Storage(*row[1:]))

        # Load PSU data
        cursor.execute("SELECT * FROM PSU")
        for row in cursor.fetchall():
            self.components['PSU'].append(PSU(*row[1:]))

        # Load Case data
        cursor.execute("SELECT * FROM ComputerCase")
        for row in cursor.fetchall():
            self.components['Case'].append(ComputerCase(*row[1:]))

        # Load Cooling data
        cursor.execute("SELECT * FROM Cooling")
        for row in cursor.fetchall():
            self.components['Cooling'].append(Cooling(*row[1:]))

        conn.close()

    def get_components(self, component_type):
        return self.components.get(component_type, [])


class ComputerBuilder:
    def __init__(self):
        self.components = {}
        self.database = ComponentDatabase('computer_components.db')

    def add_component(self, component_type, component):
        self.components[component_type] = component
        return self

    def check_compatibility(self):
        issues = []

        cpu = self.components.get('CPU')
        motherboard = self.components.get('Motherboard')
        ram = self.components.get('RAM')
        gpu = self.components.get('GPU')
        storage = self.components.get('Storage')
        psu = self.components.get('PSU')
        case = self.components.get('Case')
        cooling = self.components.get('Cooling')

        total_power = self.calculate_power()  # Add this line to calculate total power consumption
        load_percentage = (total_power / psu.wattage) * 100  # Add this line to calculate load percentage

        if cpu and motherboard:
            if cpu.socket_type != motherboard.socket_type:
                issues.append("Error: CPU and Motherboard socket types are incompatible.")
            if cooling and cpu.power_consumption > cooling.max_tdp:
                issues.append("Error: Cooling system is insufficient for the CPU.")

        if motherboard and ram:
            if ram.memory_type != motherboard.ram_type:
                issues.append("Error: RAM type is incompatible with the Motherboard.")

        if gpu and psu:
            if gpu.connectors_needed > psu.pcie_connectors:
                issues.append("Error: PSU does not have enough PCIe connectors for the GPU.")

        if case and gpu:
            if gpu.length > case.max_gpu_length:
                issues.append("Error: GPU is too long for the case.")
    
        if load_percentage > 100:  # Corrected condition
            issues.append("Error: Total power consumption exceeds PSU wattage.")
        
        if load_percentage > 80:
            issues.append("Warning: PSU is overloaded (more than 80% capacity).")

        return issues

    def calculate_power(self):
        total_power = 0
        for component in self.components.values():
            if hasattr(component, 'power_consumption') and component.power_consumption is not None:
                total_power += component.power_consumption
        return total_power

    def visualize_build(self):
        build_info = ""
        total_power = 0
        psu = None

        for component_type, component in self.components.items():
            if isinstance(component, PSU):
                psu = component
                continue

            build_info += f"{component_type}:\n"
            build_info += f"  Brand: {component.brand}\n"
            build_info += f"  Model: {component.model}\n"

            if hasattr(component, 'power_consumption'):
                build_info += f"  Power Consumption: {component.power_consumption} Watts\n"
                total_power += component.power_consumption

        if psu:
            load_percentage = (total_power / psu.wattage) * 100
            build_info += f"\nPSU Loading: {load_percentage:.2f}%\n"

        return build_info


if __name__ == "__main__":
    builder = ComputerBuilder()

    cpu = select_component("CPU")
    motherboard = select_component("Motherboard")
    ram = select_component("RAM")
    gpu = select_component("GPU")
    storage = select_component("Storage")
    psu = select_component("PSU")
    case = select_component("ComputerCase")
    cooling = select_component("Cooling")

    cpu_object = CPU(*cpu[1:])
    motherboard_object = Motherboard(*motherboard[1:])
    ram_object = RAM(*ram[1:])
    gpu_object = GPU(*gpu[1:])
    storage_object = Storage(*storage[1:])
    psu_object = PSU(*psu[1:])
    case_object = ComputerCase(*case[1:])
    cooling_object = Cooling(*cooling[1:])

    builder.add_component('CPU', cpu_object)\
    .add_component('Motherboard', motherboard_object)\
    .add_component('RAM', ram_object)\
    .add_component('GPU', gpu_object)\
    .add_component('Storage', storage_object)\
    .add_component('PSU', psu_object)\
    .add_component('Case', case_object)\
    .add_component('Cooling', cooling_object)\

    build_info = builder.visualize_build()
    compatibility_issues = builder.check_compatibility()

    print(build_info)
    if compatibility_issues:
        print("\nCompatibility Issues:")
        print("\n".join(compatibility_issues))
    else:
        print("All components are compatible with each other")

