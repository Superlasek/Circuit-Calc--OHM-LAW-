"""References
    Power / Potencia V*i, V^2 / R, R*i^2
    Current / Intensidad  V/R, P/V, 
    Resistor / Resistencia V/I, 
    Voltage / Voltaje R*I, P/I
"""

def _C_(v,r):
    print("The current is of ", v / r)

def _V_(i,r):
    print("The voltage is of ", i* r)

def _R_(v, i):
    print("The resistance is of ", v / i)


class Serie():
    def __init__(self):
        self._Resistor = []
        self._Sum = 0
    def __add__(self, resistor):
        self._Resistor.append(resistor)

    def __RT__(self):
        for i in self._Resistor:
            self._Sum += i
        #Total resistance
        print(f"The total resistance is {self._Sum}")
