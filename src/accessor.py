# get_hoge(), set_hoge(hoge)メソッドを設けるのはPythonicではない
class OldResistor:
    def __init__(self, ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(self, ohms):
        self._ohms = ohms


# @propertyデコレータ使う方法
class Resistor:
    def __init__(self, ohms) -> None:
        self._ohms = ohms
        self.voltage = 0
        self.current = 0


# voltage設定時の特別な振る舞いを@propertyデコレータで設定
class VoltageResistance(Resistor):
    def __init__(self, ohms) -> None:
        super().__init__(ohms)
        self._voltage = 0

    # self._voltageを直接操作しているが, 外部からはself.voltageというインターフェースを提供している
    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self._ohms


if __name__ == "__main__":
    # accessorを使ったPythonicでない例
    r0 = OldResistor(50e3)
    print("Before: ", r0.get_ohms())
    r0.set_ohms(10e3)
    print("After:  ", r0.get_ohms())

    # @propertyを使った例
    r1 = VoltageResistance(1e3)
    print(f"Before: {r1.current:.2f} amps")
    r1.voltage = 10
    print(f"After:  {r1.current:.2f} amps")
