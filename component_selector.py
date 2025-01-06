import sqlite3

def get_components(component_type):
    conn = sqlite3.connect('computer_components.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {component_type}")
    components = cursor.fetchall()

    conn.close()
    return components

def display_components(components):
    for index, component in enumerate(components):
        print(f"{index + 1}: {component}")

def select_component(component_type):
    print(f"\nВиберіть {component_type}:")
    components = get_components(component_type)
    display_components(components)

    selected_index = int(input(f"\nВведіть номер {component_type} компонента: ")) - 1
    if 0 <= selected_index < len(components):
        selected_component = components[selected_index]
        print(f"\nВи вибрали: {selected_component}")
        return selected_component
    else:
        print("Неправильний вибір.")
        return None

def main():
    component_types = ["CPU", "Motherboard", "RAM", "GPU", "Storage", "PSU", "ComputerCase", "Cooling"]

    for component_type in component_types:
        select_component(component_type)

if __name__ == "__main__":
    main()
