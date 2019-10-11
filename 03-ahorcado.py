IMAGES=[
"""

   +---+
   |   |
       |
       |
       |
       |
=========
""",
"""

   +---+
   |   |
   O   |
       |
       |
       |
=========
""",
"""

   +---+
   |   |
   O   |
   |   |
       |
       |
=========
""",
"""

   +---+
   |   |
   O   |
  /|   |
       |
       |
=========
""",
"""

   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========
""",
"""

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========
""",
"""

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========
"""]

def seleccionPalabra():
    while (True):
        try:
            palabra= str(input("Seleccione la palabra que el otro jugador debera adivinar:"))
        except ValueError:
            print("Ingrese una palabra valida por favor.")
        assert (palabra.find(" ") != (-1)), "Ingrese una palabra sin espacios, por favor"
        


if __name__ == "__main__":
    seleccionPalabra()