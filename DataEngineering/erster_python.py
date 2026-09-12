# Globale Variablen vermeiden
# Globale Variablen -> Konstanten (ok)
# Datenbanken Pfad
DATENBANK_URI = "Pfad"

variable_eins: int = 33


def erste_function() -> None:
    # lokale Variablen
    variable_eins = 20
    print(variable_eins)
    # Globale Variablen
    print(DATENBANK_URI)


erste_function()

# Module
# import mathematik as math
# from mathematik import addieren as addi, subtrahieren as subbi
from mathematik import addieren as addi
from mathematik import subtrahieren as subbi

erg1 = addi(0, 1)
erg2 = subbi(5, 6)


# Bedingungen

if erg1 < 0:
    print(f"{erg1} ist negativ.")
elif erg1 == 1:
    print(f"{erg1} ist 1.")
else:
    print(f"{erg1} ist positiv.")

# Schleifen
for element in [2, 3, 4, 5]:
    print(element)

for element in range(5):
    print(element)

element: int = 0
while element < 5:
    print(element)
    element += 1

# tip 1
wert_tuple: tuple = (1, 2, 3, 4, 5)

a = wert_tuple[0]
b = wert_tuple[1]
c = wert_tuple[2]
d = wert_tuple[3]
e = wert_tuple[4]

a, b, c, d, e = wert_tuple
print(a, b, c, d, e)

f, g, _, _, j = wert_tuple
print(f, g, j)


width, height = 200, 400
print(width, height)
print(f"height {width}. width {height}")

width, height = height, width
print(f"height {width}. width {height}")

wert_list: list = []
for i in range(10):
    wert_list.append(i)

print(wert_list)

wert_list2: list = [i for i in range(10)]
print(wert_list2)

# tip 5
name_list = ["tipi", "alex", "suse"]
alter_list = [35, 30, 20, 40]  # 40 fällt weg

personen = list(zip(name_list, alter_list))
print(personen)


# name_list, alter_list = personen.zip*


# Klassen
class Auto:  # First letter is uppercase
    def __init__(
        self, motor: str = "elektro", anzahl_raeder: int = 4, status: str = "stop"
    ):
        self.motor: str = motor
        self.anzahl_raeder: int = anzahl_raeder
        self.status: str = status

    def __str__(self):
        return f"motor: {self.motor} raeder_anzahl: {self.anzahl_raeder} status: {self.status}"

    def motorstart(self):
        self.status = "Motor an"

    def motorabschalten(self):
        self.status = "Motor aus"


auto1: Auto = Auto()  # wie java Constructor
print(auto1)
print(auto1.status)
auto1.motorstart()
print(auto1.status)
Auto.motorabschalten(auto1)
print(auto1.status)

auto2: Auto = Auto()
auto2.status = "fahren"
print(auto2.status)
