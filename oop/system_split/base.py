class ComponentMixin:
    def __init__(self, name: str, type: str):
        self._name = name
        self._type = type

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> str:
        return self._type