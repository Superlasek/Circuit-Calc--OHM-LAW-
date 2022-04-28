"""References
    Power / Potencia V*i, V^2 / R, R*i^2
    Current / Intensidad  V/R, P/V, 
    Resistor / Resistencia V/I, 
    Voltage / Voltaje R*I, P/I
"""

def _P_(v, i):
    print("The power is of ", v * i)

def _C_(v,r):
    print("The current is of ", v / r)

def _R_(v, i):
    print("The resistance is of ", v / i)

def _V_(i,r):
    print("The voltage is of ", i* r)


class Power:
    def __clear__(self):
        self.v = 0
        self.i = 0

    def __init__(self, v, i):
        self.v = v
        self.i = i

    def __P_(self):
        for i in range(len(self.v)):
            _P_(self.v[i], self.i[i])
        print("The power is of ", self.v * self.i)


class Serie():
    def __clear__(self):
        self._Resistor.clear()
        self._Sum = 0

    def __init__(self):
        self._Resistor = []
        self._Sum = 0
    def __add__(self, resistor):
        self._Resistor.append(resistor)

    def __RT__(self):
        for i in self._Resistor:
            self._Sum += i
        #Total resistance
        print(f"The total resistance is:\n{self._Sum}Ω")


class Parallel():
    def __clear__(self):
        self._Resistor.clear()
        self._Sum = 0

    def __init__(self):
        self._Resistor = []
        self._Sum = 0

    def __add__(self, resistor):
        self._Resistor.append(resistor)

    def __RT__(self):
        for i in self._Resistor:
            self._Sum += 1/i
            total_sum = 1/self._Sum
        #Total resistance
        print(f"The total resistance is {total_sum}")