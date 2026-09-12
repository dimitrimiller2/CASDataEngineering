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
