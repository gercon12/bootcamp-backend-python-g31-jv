
# Importamos random para generar números aleatorios
import random

#Parte 1: La clase Tragamonedas — Nace la máquina


#-----------------------------------------------------------------------------
class Tragamonedas:

    def __init__(self, nombre, creditos):

        self.nombre = nombre

        # Atributo privado: protege los créditos.
        self.__creditos = creditos

        # Estadísticas de la máquina.
        self.total_apostado = 0
        self.total_ganado = 0
        self.numero_jugadas = 0

        # Símbolos de la máquina clásica.
        self.simbolos = ["7️⃣", "💎", "🔔", "🍀", "⭐", "🍒"]

    # Método para consultar los créditos.
    def mostrar_creditos(self):
        return self.__creditos

    def mostrar(self):
        print(f"🎰 {self.nombre}")
        print(f"Créditos disponibles: {self.__creditos}")

    def girar(self):

        resultado = []

        for i in range(3):
            indice = random.randint(0, len(self.simbolos) - 1)
            resultado.append(self.simbolos[indice])

        print(resultado)

        return resultado

    def jugar(self, apuesta):

        # Validar que la apuesta sea positiva.
        if apuesta <= 0:
            print("La apuesta debe ser mayor que cero.")
            return

        # Validar que existan suficientes créditos.
        if apuesta > self.__creditos:
            print("No tienes suficientes créditos.")
            return

        # Registrar la apuesta.
        self.__creditos -= apuesta
        self.total_apostado += apuesta
        self.numero_jugadas += 1

        # Girar la máquina.
        resultado = self.girar()

        premio = 0

        # Tres símbolos iguales: premio x10.
        if resultado[0] == resultado[1] == resultado[2]:
            premio = apuesta * 10
            print(f"¡Jackpot! Ganaste {premio} créditos.")

        # Dos símbolos iguales: premio x2.
        elif (
            resultado[0] == resultado[1]
            or resultado[1] == resultado[2]
            or resultado[0] == resultado[2]
        ):
            premio = apuesta * 2
            print(f"¡Ganaste {premio} créditos!")

        else:
            print("Lo siento, perdiste la apuesta.")

        # Actualizar saldo y estadísticas.
        self.__creditos += premio
        self.total_ganado += premio

        self.mostrar()

    # Mostrar las estadísticas de la máquina.
    def mostrar_estadisticas(self):

        print("\n--- ESTADÍSTICAS ---")
        print(f"Total apostado: {self.total_apostado}")
        print(f"Total ganado: {self.total_ganado}")
        print(f"Número de jugadas: {self.numero_jugadas}")
        print(f"Saldo actual: {self.__creditos}")



# 3B — Reto: Bucle de juego

# CREAR UNA INSTANCIA (OBJETO)
# Creamos la máquina una sola vez con 100 créditos.
maquina = Tragamonedas("La Siete", 100)

# BUCLE PRINCIPAL DEL JUEGO
# Se repetirá hasta que el jugador decida salir
# o se quede sin créditos.
def main(maquina):
    while True:

        # Mostrar los créditos disponibles.
        maquina.mostrar()

        # Solicitar la apuesta al jugador.
        try:
            apuesta = int(input("¿Cuánto apuestas? (0 para salir): "))

        except ValueError:
            print("Debes ingresar un número válido.")
            continue

        # SALIR DEL JUEGO
        if apuesta == 0:
            print("Gracias por jugar. ¡Hasta pronto!")
            break

        # VALIDAR APUESTA
        if apuesta < 0:
            print("La apuesta no puede ser negativa.")
            continue

        # EJECUTAR EL JUEGO
        # Utilizamos la cantidad ingresada por el jugador.
        maquina.jugar(apuesta)

        # COMPROBAR SI SE QUEDÓ SIN CRÉDITOS.
        if maquina.creditos <= 0:
            print("Te quedaste sin créditos.")
            break


# Parte 4: Herencia — Diferentes tipos de máquinas
# 4A — Demo: Máquina de Frutas

class FrutasTragamonedas(Tragamonedas):

    def __init__(self, nombre, creditos):

        # Ejecutamos el constructor de la clase padre.
        super().__init__(nombre, creditos)

        # Cambiamos los símbolos por los de frutas.
        self.simbolos = ["🍒", "🍋", "🍊", "🍉", "🍇", "🍓"]


# 4B — Reto: Crea tu propia máquina
class AnimalesTragamonedas(Tragamonedas):

    def __init__(self, nombre, creditos):

        # Ejecutamos el constructor de la clase padre.
        super().__init__(nombre, creditos)

        # Cambiamos los símbolos por los de animales.
        self.simbolos = ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊"]

    # Sobrescribimos el método jugar() de la clase padre.
    def jugar(self, apuesta):

        # Validamos que la apuesta sea válida.
        if apuesta <= 0:
            print("La apuesta debe ser mayor que cero.")
            return

        # Validamos que tenga suficientes créditos.
        if apuesta > self.creditos:
            print(f"No tienes suficientes créditos. Dispones de {self.creditos}")
            return

        # Descontamos la apuesta.
        self.creditos -= apuesta

        # Giramos la máquina. Este método lo heredamos de Tragamonedas.
        resultado = self.girar()

        # Tres animales iguales: premio x15.
        if resultado[0] == resultado[1] == resultado[2]:
            premio = apuesta * 15
            print(f"¡Jackpot! Ganaste {premio} créditos.")

        # Dos animales iguales: premio x2.
        elif (
            resultado[0] == resultado[1]
            or resultado[1] == resultado[2]
            or resultado[0] == resultado[2]
        ):
            premio = apuesta * 2
            print(f"¡Ganaste {premio} créditos!")

        # Ninguna combinación ganadora.
        else:
            premio = 0
            print("Lo siento, perdiste la apuesta.")

        # Sumamos el premio a los créditos.
        self.creditos += premio

        # Mostramos el saldo actualizado.
        self.mostrar()

        
# Crear máquina clásica.
maquina_clasica = Tragamonedas("La Siete", 100)

# Crear máquina de frutas.
maquina_frutas = FrutasTragamonedas("Las Frutas", 100)

# Crear máquina de animales.
maquina_animales = AnimalesTragamonedas("Los Animales", 100)

# Ejecutar el juego con la máquina a tu elección.
main(maquina_clasica)

print("\n--- FIN DEL JUEGO ---")
maquina_clasica.mostrar()