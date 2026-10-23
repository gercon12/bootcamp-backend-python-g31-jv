import random

class Tragamonedas:

    # Constructor
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos

    # Mostrar información
    def mostrar(self):
        print(f"🎰 {self.nombre} - Créditos: S/ {self.creditos}")

    # Girar tragamonedas
    def girar(self):

        simbolos = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"]

        resultado = []

        # Generar 3 símbolos aleatorios
        for i in range(3):
            resultado.append(random.choice(simbolos))

        print(resultado)

        return resultado


# Crear objeto
maquina = Tragamonedas("La Siete", 100)

# Mostrar información
maquina.mostrar()

# Girar tragamonedas
maquina.girar()