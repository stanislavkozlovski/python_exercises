from base import ComponentMixin
from constants import (
    EXPRESS_SOFTWARE_MEM_INCREASE_TIMES, LIGHT_SOFTWARE_MEM_DECREASE_PERCENTAGE, LIGHT_SOFTWARE_CAP_INCREASE_PERCENTAGE
)


class SoftwareComponent(ComponentMixin):
    def __init__(self, name: str, type: str, cap_cons: int, mem_cons: int):
        super().__init__(name, type)
        self.capacity_consumption = cap_cons
        self.memory_consumption = mem_cons


class ExpressSoftwareComponent(SoftwareComponent):
    def __init__(self, name: str, cap_cons: int, mem_cons: int):
        # double memory consumption
        mem_cons *= EXPRESS_SOFTWARE_MEM_INCREASE_TIMES
        super().__init__(name, "Express Software", cap_cons, mem_cons)


class LightSoftwareComponent(SoftwareComponent):
    def __init__(self, name: str, cap_cons: int, mem_cons: int):
        # increase capacity consumption by 50%
        cap_cons += int(EXPRESS_SOFTWARE_MEM_INCREASE_TIMES * cap_cons)
        # decrease memory consumption by 50%
        mem_cons -= int(LIGHT_SOFTWARE_MEM_DECREASE_PERCENTAGE * mem_cons)
        super().__init__(name, "Light Software", cap_cons, mem_cons)