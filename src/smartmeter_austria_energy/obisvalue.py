from .constants import PhysicalUnits


class ObisValue():
    def __init__(self, raw_value: float, unit: PhysicalUnits = PhysicalUnits(0), scale: int = 1) -> None:
        self._raw_value = raw_value
        self._scale = scale
        self._unit = unit

    @property
    def RawValue(self) -> float:
        return self._raw_value

    @RawValue.setter
    def RawValue(self, value):
        self._raw_value = value

    @property
    def Scale(self) -> float:
        return self._scale

    @Scale.setter
    def Scale(self, scale):
        self._scale = scale

    @property
    def Unit(self) -> PhysicalUnits:
        return self._unit

    @Unit.setter
    def Unit(self, unit):
        self._unit = unit

    @property
    def Value(self) -> float:
        return self._raw_value * 10**self._scale

    @property
    def ValueString(self) -> str:
        return "{} {}".format(self.Value, self.Unit.name)
