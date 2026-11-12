
# ============================================================
# CASINO ROYALE

# ============================================================

import random

# ============================================================
# PARTE 1: CLASE PADRE

class Tragamonedas:

    def __init__(self, nombre, creditos, simbolos=None):

        self.nombre = nombre

        # Atributo privado: no se debe modificar directamente.
        self.__creditos = creditos

        # Estadísticas de la máquina.
        self.total_apostado = 0
        self.total_ganado = 0
        self.numero_jugadas = 0

        # Símbolos de la máquina.
        if simbolos is None:
            self.simbolos = ["7️⃣", "💎", "🔔", "🍀", "⭐", "🍒"]
        else:
            self.simbolos = simbolos

    # --------------------------------------------------------
    # CONSULTAR CRÉDITOS
    # --------------------------------------------------------

    def mostrar_creditos(self):
        return self.__creditos

    # --------------------------------------------------------
    # MODIFICAR CRÉDITOS INTERNAMENTE
    # --------------------------------------------------------

    def _descontar_creditos(self, cantidad):
        self.__creditos -= cantidad

    def _agregar_creditos(self, cantidad):
        self.__creditos += cantidad

    # --------------------------------------------------------
    # MOSTRAR INFORMACIÓN DE LA MÁQUINA
    # --------------------------------------------------------

    def mostrar(self):
        print(f"\n🎰 {self.nombre}")
        print(f"Créditos disponibles: S/ {self.__creditos}")

    # --------------------------------------------------------
    # GIRAR LA MÁQUINA
    # --------------------------------------------------------


    def girar(self):

        resultado = []

        # Generamos tres símbolos aleatorios.
        for i in range(3):
            indice = random.randint(0, len(self.simbolos) - 1)
            resultado.append(self.simbolos[indice])

        # Mostrar los símbolos obtenidos.
        #print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        print("\n🎰 RESULTADO DE LA JUGADA")
        print("-" * 30)
        print(" | ".join(resultado))
        print("-" * 30)

        return resultado


    # --------------------------------------------------------
    # JUGAR CON REGLAS GENERALES
    # --------------------------------------------------------

    def jugar(self, apuesta):
        # premio 1 = *10, premio 2 = *2
        self._jugar_con_reglas(apuesta, 10, 2)

    # --------------------------------------------------------
    # MÉTODO INTERNO PARA EJECUTAR UNA JUGADA
    # --------------------------------------------------------

    def _jugar_con_reglas(self, apuesta, premio_tres, premio_dos):

        # Validar que la apuesta sea positiva.
        if apuesta <= 0:
            print("La apuesta debe ser mayor que cero.")
            return

        # Validar que existan suficientes créditos.
        if apuesta > self.__creditos:
            print("No tienes suficientes créditos.")
            return

        # Registrar la apuesta.
        self._descontar_creditos(apuesta)
        self.total_apostado += apuesta
        self.numero_jugadas += 1

        # Girar la máquina.
        resultado = self.girar()

        premio = 0

        
        # Tres símbolos iguales.
        if resultado[0] == resultado[1] == resultado[2]:

            premio = apuesta * premio_tres

            print("\n🏆 ¡JACKPOT!")
            print(f"Los tres símbolos son iguales.")
            print(f"Premio: S/ {premio}")

        # Dos símbolos iguales.
        elif (
            resultado[0] == resultado[1]
            or resultado[1] == resultado[2]
            or resultado[0] == resultado[2]
        ):

            premio = apuesta * premio_dos

            print("\n🎉 ¡GANASTE!")
            print("Obtuviste dos símbolos iguales.")
            print(f"Premio: S/ {premio}")

        # Ninguna combinación ganadora.
        else:

            premio = 0

            print("\n😢 LO SENTIMOS")
            print("No obtuviste ninguna combinación ganadora.")

        # Actualizar créditos y estadísticas.
        self._agregar_creditos(premio)
        self.total_ganado += premio

        # self.mostrar()

    # --------------------------------------------------------
    # MOSTRAR ESTADÍSTICAS
    # --------------------------------------------------------

    def mostrar_estadisticas(self):

        print(f"\n--- {self.nombre} ---")
        print(f"Total apostado: S/ {self.total_apostado}")
        print(f"Total ganado: S/ {self.total_ganado}")
        print(f"Número de jugadas: {self.numero_jugadas}")
        print(f"Saldo actual: S/ {self.mostrar_creditos()}")


# ============================================================
# PARTE 2: MÁQUINA DE FRUTAS

class TragamonedasFrutas(Tragamonedas):

    def __init__(self, nombre, creditos):

        # Inicializar la clase padre.
        super().__init__(
            nombre,
            creditos,
            ["🍒", "🍋", "🍊", "🍉", "🍇", "🍓"]
        )


# ============================================================
# PARTE 3: MÁQUINA CLÁSICA

class TragamonedasClasico(Tragamonedas):

    def __init__(self, nombre, creditos):

        # Inicializar la clase padre.
        super().__init__(
            nombre,
            creditos,
            ["7️⃣", "💎", "🔔", "🍀", "⭐", "🍒"]
        )


# ============================================================
# PARTE 4: MÁQUINA - MUNDIAL 2026

class Mundial2026Tragamonedas(Tragamonedas):

    def __init__(self, nombre, creditos):

        # Inicializar la clase padre.
        super().__init__(
            nombre,
            creditos,
            ["⚽", "🏆", "🥅", "👟", "🇲🇽", "🇺🇸", "🇨🇦"]
        )

    # Sobrescribir jugar() con reglas diferentes.
    def jugar(self, apuesta):

        # Tres símbolos iguales: premio x15.
        # Dos símbolos iguales: premio x2.
        self._jugar_con_reglas(apuesta, 15, 2)


# ============================================================
# PARTE 5: BUCLE DE JUEGO DE CADA MÁQUINA

def jugar_maquina(maquina):

    print(f"\n🎰 Bienvenido a {maquina.nombre}")

    while True:

        # Si no hay créditos, regresar al menú.
        if maquina.mostrar_creditos() <= 0:

            print("\n¡Esta máquina se quedó SIN CRÉDITOS!")
            break

        maquina.mostrar()

        try:
            apuesta = int(input("\n¿Cuánto deseas apostar? (0 para volver): "))

        except ValueError:
            print("Debes ingresar un número válido.")
            continue

        # Regresar al menú principal.
        if apuesta == 0:
            print("Regresando al menú principal...")
            break

        # Validar apuesta negativa.
        if apuesta < 0:
            print("La apuesta no puede ser negativa.")
            continue

        # Ejecutar una jugada.
        maquina.jugar(apuesta)


# ============================================================
# PARTE 6: MENÚ PRINCIPAL DEL CASINO

def mostrar_menu(maquinas):

    print("\n" + "=" * 45)
    print("          🎰 CASINO ROYALE 🎰")
    print("=" * 45)

    for numero, maquina in enumerate(maquinas, start=1):

        creditos = maquina.mostrar_creditos()

        if creditos <= 0:
            estado = "SIN CRÉDITOS"
        else:
            estado = f"S/ {creditos}"

        print(f"{numero}. {maquina.nombre} ({estado})")

    print("4. Mostrar estadísticas de todas")
    print("5. Salir")

    print("=" * 45)


# ============================================================
# PARTE 7: ESTADÍSTICAS GENERALES

def mostrar_estadisticas_todas(maquinas):

    print("\n" + "=" * 45)
    print("       📊 ESTADÍSTICAS DEL CASINO")
    print("=" * 45)

    for maquina in maquinas:
        maquina.mostrar_estadisticas()

    # Calcular totales generales.
    total_apostado = sum(
        maquina.total_apostado for maquina in maquinas
    )

    total_ganado = sum(
        maquina.total_ganado for maquina in maquinas
    )

    total_jugadas = sum(
        maquina.numero_jugadas for maquina in maquinas
    )

    total_creditos = sum(
        maquina.mostrar_creditos() for maquina in maquinas
    )

    print("\n" + "-" * 45)
    print("          RESUMEN GENERAL")
    print("-" * 45)

    print(f"Total apostado: S/ {total_apostado}")
    print(f"Total ganado: S/ {total_ganado}")
    print(f"Total de jugadas: {total_jugadas}")
    print(f"Créditos restantes: S/ {total_creditos}")

    print("-" * 45)


# ============================================================
# PARTE 8: PROGRAMA PRINCIPAL

def main():

    # Crear las tres máquinas.
    # Cada objeto conserva sus propios créditos y estadísticas.

    maquina_frutas = TragamonedasFrutas("La Frutal", 200)

    maquina_clasica = TragamonedasClasico("La Clásica", 300)

    maquina_mundial = Mundial2026Tragamonedas("Mundial 2026", 150)

    # Guardar las máquinas en una lista.
    maquinas = [
        maquina_frutas,
        maquina_clasica,
        maquina_mundial
    ]

    # Menú principal del casino.
    while True:

        mostrar_menu(maquinas)

        try:
            opcion = int(input("\nElige una máquina: "))

        except ValueError:
            print("Debes ingresar una opción válida.")
            continue

        # Seleccionar una máquina.
        if 1 <= opcion <= 3:

            maquina_seleccionada = maquinas[opcion - 1]

            # No permitir jugar si no tiene créditos.
            if maquina_seleccionada.mostrar_creditos() <= 0:

                print("\nEsta máquina está SIN CRÉDITOS.")

            else:

                jugar_maquina(maquina_seleccionada)

        # Mostrar estadísticas de todas las máquinas.
        elif opcion == 4:

            mostrar_estadisticas_todas(maquinas)

        # Salir del casino.
        elif opcion == 5:

            print("\nGracias por visitar CASINO ROYALE.")

            mostrar_estadisticas_todas(maquinas)

            print("\n🎰 ¡Hasta la próxima! 🎰")
            break

        else:

            print("Opción incorrecta. Intenta nuevamente.")


# ============================================================
# EJECUTAR EL PROGRAMA


if __name__ == "__main__":
    main()
