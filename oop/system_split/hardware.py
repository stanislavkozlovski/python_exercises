from base import ComponentMixin
from constants import (
    POWER_HARDWARE_CAPACITY_PERCENTAGE, POWER_HARDWARE_MEMORY_INCREASE_PERCENTAGE,
    HEAVY_HARDWARE_CAPACITY_INCREASE_TIMES, HEAVY_HARDWARE_MEMORY_PERCENTAGE
)


class HardwareComponent(ComponentMixin):
    def __init__(self, name: str, type: str, max_cap: int, max_mem: int):
        super().__init__(name, type)
        self.software_components = {}
        self.max_capacity = max_cap
        self.max_memory = max_mem
        self.used_capacity, self.used_memory = 0, 0

    def register_software_component(self, soft_component):
        cap_is_overfilled = self.used_capacity + soft_component.capacity_consumption > self.max_capacity
        mem_is_overfilled = self.used_memory + soft_component.memory_consumption > self.max_memory
        if cap_is_overfilled or mem_is_overfilled:
            return False

        self.used_capacity += soft_component.capacity_consumption
        self.used_memory += soft_component.memory_consumption

        self.software_components[soft_component.name] = soft_component
        return True

    def release_software_component(self, soft_component_name):
        """ Remove a software component from this hardware """
        if soft_component_name not in self.software_components:
            return False

        soft_component = self.software_components[soft_component_name]
        self.used_capacity -= soft_component.capacity_consumption
        self.used_memory -= soft_component.memory_consumption
        del self.software_components[soft_component_name]

        return True


class PowerHardware(HardwareComponent):
    def __init__(self, name: str, max_cap: int, max_mem: int):
        # decrease 75% cap
        max_cap = int(POWER_HARDWARE_CAPACITY_PERCENTAGE * max_cap)
        # increase memory 75%
        max_mem += int(POWER_HARDWARE_MEMORY_INCREASE_PERCENTAGE * max_mem)
        super().__init__(name, "Power Hardware", max_cap, max_mem)


class HeavyHardware(HardwareComponent):
    def __init__(self, name: str, max_cap: int, max_mem: int):
        # double cap
        max_cap = max_cap * HEAVY_HARDWARE_CAPACITY_INCREASE_TIMES
        # decrease memory 25%
        max_mem = int(HEAVY_HARDWARE_MEMORY_PERCENTAGE * max_mem)
        super().__init__(name, "Heavy Hardware", max_cap, max_mem)
