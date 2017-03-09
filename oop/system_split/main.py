import re

from hardware import PowerHardware, HeavyHardware
from software import ExpressSoftwareComponent, LightSoftwareComponent


class TheSystem:
    def __init__(self):
        self.hardwares = {}

    def register_power_hardware(self, name, capacity, memory):
        self.hardwares[name] = PowerHardware(name, capacity, memory)

    def register_heavy_hardware(self, name, capacity, memory):
        self.hardwares[name] = HeavyHardware(name, capacity, memory)

    def register_express_software(self, hardware_component_name, name, capacity, memory):
        if hardware_component_name not in self.hardwares:
            return
        soft_comp = ExpressSoftwareComponent(name, capacity, memory)

        self.hardwares[hardware_component_name].register_software_component(soft_comp)

    def register_light_software(self, hardware_component_name, name, capacity, memory):
        if hardware_component_name not in self.hardwares:
            return

        soft_comp = LightSoftwareComponent(name, capacity, memory)
        self.hardwares[hardware_component_name].register_software_component(soft_comp)

    def release_software_component(self, hardware_component_name, software_component_name):
        if hardware_component_name not in self.hardwares:
            return False

        self.hardwares[hardware_component_name].release_software_component(software_component_name)

        return True

    def analyze(self):
        print(f"""Software Components
Hardware Components: {len(self.hardwares)}
Software Components: {sum(len(hardware.software_components) for hardware in self.hardwares.values())}
Total Operational Memory: {sum(hardware.used_memory for hardware in self.hardwares.values())} / {sum(hardware.max_memory for hardware in self.hardwares.values())}
Total Capacity Taken: {sum(hardware.used_capacity for hardware in self.hardwares.values())} / {sum(hardware.max_capacity for hardware in self.hardwares.values())}""")

    def split(self):
        ordered_hardware_components = ([pow_comp for pow_comp in self.hardwares.values()
                                        if isinstance(pow_comp, PowerHardware)]
                                      + [heavy_comp for heavy_comp in self.hardwares.values()
                                         if isinstance(heavy_comp, HeavyHardware)])
        for comp in ordered_hardware_components:
            express_soft_count = len([None for soft_comp in comp.software_components.values()
                                      if isinstance(soft_comp, ExpressSoftwareComponent)])
            light_soft_count = len([None for light_comp in comp.software_components.values()
                                      if isinstance(light_comp, LightSoftwareComponent)])
            print(f'Hardware Component - {comp.name}')
            print(f'Express Software Components: {express_soft_count}')
            print(f'Light Software Components: {light_soft_count}')
            print(f'Memory Usage: {comp.used_memory} / {comp.max_memory}')
            print(f'Capacity Usage: {comp.used_capacity} / {comp.max_capacity}')
            print(f'Type: {"Power" if isinstance(comp, PowerHardware) else "Heavy"}')
            print(f'Software Components {{{", ".join([s_comp.name for s_comp in comp.software_components.values()]) or "None"}}}')


def main():
    re_pattern = r'.+\((?P<args>.+)\)'
    command = input()
    system = TheSystem()
    while command != 'System Split':
        if command.startswith('RegisterPowerHardware') or command.startswith('RegisterHeavyHardware'):
            args = re.match(re_pattern, command).group('args').split(', ')
            name = args[0]
            capacity = int(args[1])
            memory = int(args[2])
            if command.startswith('RegisterPowerHardware'):
                system.register_power_hardware(name, capacity, memory)
            else:
                system.register_heavy_hardware(name, capacity, memory)
        elif command.startswith('RegisterLightSoftware') or command.startswith('RegisterExpressSoftware'):
            args = re.match(re_pattern, command).group('args').split(', ')
            hardware_name = args[0]
            name = args[1]
            capacity = int(args[2])
            memory = int(args[3])
            if command.startswith('RegisterLightSoftware'):
                system.register_light_software(hardware_name, name, capacity, memory)
            else:
                system.register_express_software(hardware_name, name, capacity, memory)
        elif command.startswith('Analyze'):
            system.analyze()
        elif command.startswith('ReleaseSoftwareComponent'):
            args = re.match(re_pattern, command).group('args').split(', ')
            hardware_name = args[0]
            software_name = args[1]
            system.release_software_component(hardware_name, software_name)
        command = input()
    system.split()


if __name__ == '__main__':
    main()
