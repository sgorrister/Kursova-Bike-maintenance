import unittest
from computer_builder import ComputerBuilder, CPU, Motherboard, RAM, GPU, Storage, PSU, ComputerCase, Cooling

class TestComputerBuilder(unittest.TestCase):

    def setUp(self):
        # Ініціалізація тестового об'єкта для перевірки
        self.builder = ComputerBuilder()
        self.cpu = CPU("Intel", "Core i5-12600K", "Core i5", "12th Gen", "LGA1700", 10, 3.7, 20, 125)
        self.motherboard = Motherboard("ASUS", "TUF Z690", "LGA1700", "Z690", 4, "DDR4", "5.0", 20, 300)
        self.ram = RAM("Kingston", "Fury Beast", "DDR4", 16, 3600, 10)
        self.gpu = GPU("NVIDIA", "RTX 3070", 8, 220, 1500, 250, 2)
        self.storage = Storage("Samsung", "970 Evo", "SSD", "1TB", "NVMe", 5)
        self.psu = PSU("Corsair", "RM750x", 750, "80+ Gold", 4, 15)
        self.case = ComputerCase("NZXT", "H510 Flow", "ATX", 381)
        self.cooling = Cooling("Noctua", "NH-D15", "Air", 165, 5, "LGA1700", 220)

    def test_add_components(self):
        self.builder.add_component("CPU", self.cpu)
        self.builder.add_component("Motherboard", self.motherboard)
        self.builder.add_component("RAM", self.ram)
        self.assertIn("CPU", self.builder.components)
        self.assertIn("Motherboard", self.builder.components)
        self.assertIn("RAM", self.builder.components)

    def test_compatibility_success(self):
        self.builder.add_component("CPU", self.cpu)
        self.builder.add_component("Motherboard", self.motherboard)
        self.builder.add_component("RAM", self.ram)
        self.builder.add_component("GPU", self.gpu)
        self.builder.add_component("Storage", self.storage)
        self.builder.add_component("PSU", self.psu)
        self.builder.add_component("Case", self.case)
        self.builder.add_component("Cooling", self.cooling)
        result = self.builder.check_compatibility()
        self.assertEqual(result, "Success: All components are compatible.")

    def test_incompatible_cpu_motherboard(self):
        incompatible_cpu = CPU("AMD", "Ryzen 5 5600X", "Ryzen 5", "Zen 3", "AM4", 6, 3.7, 32, 65)
        self.builder.add_component("CPU", incompatible_cpu)
        self.builder.add_component("Motherboard", self.motherboard)
        result = self.builder.check_compatibility()
        self.assertIn("CPU and Motherboard socket types are incompatible.", result)

    def test_psu_overload(self):
        high_power_gpu = GPU("NVIDIA", "RTX 4090", 24, 450, 2500, 400, 3)
        self.builder.add_component("CPU", self.cpu)
        self.builder.add_component("GPU", high_power_gpu)
        self.builder.add_component("PSU", PSU("CoolerMaster", "V750", 500, "80+ Bronze", 2, 10))
        result = self.builder.visualize_build()
        self.assertIn("Warning: PSU is overloaded", result)

    def test_case_gpu_size_mismatch(self):
        oversized_gpu = GPU("NVIDIA", "RTX 4080", 16, 320, 2500, 450, 3)
        self.builder.add_component("GPU", oversized_gpu)
        self.builder.add_component("Case", self.case)
        result = self.builder.check_compatibility()
        self.assertIn("GPU is too long for the case.", result)

if __name__ == "__main__":
    unittest.main()