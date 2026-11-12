# 🎰 Casino Royale

Proyecto de consola desarrollado en Python para practicar los
fundamentos de la **programación orientada a objetos (POO)**. El
programa administra varias máquinas tragamonedas, cada una con sus
propios símbolos, créditos y estadísticas.

## 1. Objetivo del proyecto

Construir un casino sencillo que permita:

-   Crear y administrar varias máquinas tragamonedas.
-   Seleccionar una máquina desde un menú principal.
-   Realizar apuestas y generar resultados aleatorios.
-   Aplicar diferentes reglas de premios según el tipo de máquina.
-   Proteger el saldo de créditos mediante encapsulación.
-   Registrar estadísticas individuales y generales.
-   Conservar el saldo y las estadísticas mientras el programa está en
    ejecución.

## 2. Requisitos

-   Python 3 instalado.
-   Una terminal que permita ejecutar programas Python.
-   No se necesitan librerías externas: `random` forma parte de la
    biblioteca estándar de Python.

## 3. Cómo ejecutar el programa

Guarda el código en un archivo, por ejemplo `03_tragamonedas.py`.

Desde la terminal, ubícate en la carpeta donde guardaste el archivo y
ejecuta:

``` bash
py 03_tragamonedas.py
```

En algunos sistemas también puedes utilizar:

``` bash
python 03_tragamonedas.py
```

## 4. Estructura general del programa

El programa está organizado en ocho partes:

  --------------------------------------------------------------------------------
  Parte                   Elemento                         Responsabilidad
  ----------------------- -------------------------------- -----------------------
  1                       `Tragamonedas`                   Clase padre con los
                                                           atributos y operaciones
                                                           comunes.

  2                       `TragamonedasFrutas`             Máquina con símbolos de
                                                           frutas.

  3                       `TragamonedasClasico`            Máquina con símbolos
                                                           clásicos.

  4                       `Mundial2026Tragamonedas`        Máquina temática de
                                                           fútbol con reglas de
                                                           premio propias.

  5                       `jugar_maquina()`                Controla el bucle de
                                                           juego de una máquina
                                                           seleccionada.

  6                       `mostrar_menu()`                 Presenta las máquinas y
                                                           sus saldos disponibles.

  7                       `mostrar_estadisticas_todas()`   Presenta estadísticas
                                                           individuales y totales
                                                           del casino.

  8                       `main()`                         Crea las máquinas y
                                                           controla el menú
                                                           principal.
  --------------------------------------------------------------------------------

### Relación entre las clases

Las tres máquinas especializadas heredan de la clase padre
`Tragamonedas`:

``` text
                 Tragamonedas
                      |
          +-----------+------------+
          |           |            |
   Tragamonedas   Tragamonedas   Mundial2026
      Frutas        Clasico     Tragamonedas
```

La herencia permite reutilizar los métodos y atributos comunes sin
escribir de nuevo toda la lógica del juego.

## 5. Clase padre: `Tragamonedas`

Es la clase principal del programa. Define el comportamiento que
comparten todas las máquinas.

### Atributos

  -----------------------------------------------------------------------
  Atributo                            Descripción
  ----------------------------------- -----------------------------------
  `nombre`                            Nombre de la máquina.

  `__creditos`                        Saldo de créditos. Es privado
                                      mediante la convención de doble
                                      guion bajo de Python.

  `total_apostado`                    Acumulado de todas las apuestas
                                      aceptadas.

  `total_ganado`                      Acumulado de los premios
                                      entregados.

  `numero_jugadas`                    Cantidad de apuestas aceptadas y
                                      jugadas ejecutadas.

  `simbolos`                          Lista de símbolos que utiliza la
                                      máquina.
  -----------------------------------------------------------------------

El constructor recibe el nombre, los créditos iniciales y,
opcionalmente, una lista de símbolos. Si no recibe símbolos, utiliza los
símbolos clásicos predeterminados.

### Métodos principales

-   `mostrar_creditos()`: devuelve el saldo actual.
-   `_descontar_creditos(cantidad)`: descuenta una apuesta del saldo.
-   `_agregar_creditos(cantidad)`: agrega el premio al saldo.
-   `mostrar()`: muestra el nombre y los créditos disponibles.
-   `girar()`: selecciona aleatoriamente tres símbolos y muestra el
    resultado.
-   `jugar(apuesta)`: ejecuta una jugada con las reglas generales.
-   `_jugar_con_reglas(apuesta, premio_tres, premio_dos)`: concentra las
    validaciones, el giro, el cálculo del premio y la actualización de
    las estadísticas.
-   `mostrar_estadisticas()`: muestra las estadísticas de una máquina.

Los métodos que comienzan con un guion bajo, como `_jugar_con_reglas()`,
se consideran internos por convención: están pensados para ser
utilizados dentro de la clase y sus clases hijas.

## 6. Encapsulación de los créditos

El saldo se declara así:

``` python
self.__creditos = creditos
```

El doble guion bajo activa el mecanismo de *name mangling* de Python.
Esto dificulta el acceso accidental al atributo desde fuera de la clase.

Para consultar el saldo se utiliza:

``` python
maquina.mostrar_creditos()
```

Para modificarlo, la lógica interna utiliza:

``` python
self._descontar_creditos(apuesta)
self._agregar_creditos(premio)
```

De esta manera, las jugadas actualizan el saldo a través de los métodos
definidos en la clase, en lugar de modificarlo directamente desde el
menú.

**Nota:** en Python, el doble guion bajo no proporciona privacidad
absoluta ni seguridad criptográfica. Es un mecanismo para evitar accesos
accidentales y organizar el código.

## 7. Herencia y tipos de máquinas

### Máquina de frutas

Clase: `TragamonedasFrutas`

Utiliza los símbolos:

``` python
["🍒", "🍋", "🍊", "🍉", "🍇", "🍓"]
```

Hereda las reglas generales de la clase padre.

### Máquina clásica

Clase: `TragamonedasClasico`

Utiliza los símbolos:

``` python
["7️⃣", "💎", "🔔", "🍀", "⭐", "🍒"]
```

También utiliza las reglas generales de la clase padre.

### Máquina Mundial 2026

Clase: `Mundial2026Tragamonedas`

Utiliza símbolos relacionados con el fútbol:

``` python
["⚽", "🏆", "🥅", "👟", "🏟️", "🎽"]
```

Esta clase sobrescribe el método `jugar()` para utilizar reglas
diferentes. En particular, tres símbolos iguales entregan un premio de
quince veces la apuesta.

## 8. Reglas de las apuestas y premios

Las máquinas utilizan las siguientes reglas:

  Resultado                 Máquina clásica y frutas   Mundial 2026
  ----------------------- -------------------------- --------------
  Tres símbolos iguales                 Apuesta × 10   Apuesta × 15
  Dos símbolos iguales                   Apuesta × 2    Apuesta × 2
  Ninguna combinación                     Sin premio     Sin premio

Antes de ejecutar una jugada, el programa valida que:

1.  La apuesta sea mayor que cero.
2.  La apuesta no supere los créditos disponibles.

Cuando la apuesta es válida:

1.  Se descuentan los créditos apostados.
2.  Se incrementa `total_apostado`.
3.  Se incrementa `numero_jugadas`.
4.  Se generan tres símbolos aleatorios.
5.  Se calcula el premio según la combinación.
6.  Se agrega el premio al saldo.
7.  Se incrementa `total_ganado` con el premio entregado.

**Importante sobre las estadísticas:** `total_ganado` representa la suma
de los premios pagados, no la ganancia neta. La diferencia entre
`total_ganado` y `total_apostado` permite calcular el resultado
acumulado de las jugadas.

## 9. Flujo del programa

Al iniciar `main()` se crean tres objetos:

  Máquina          Créditos iniciales
  -------------- --------------------
  La Frutal                    S/ 200
  La Clásica                   S/ 300
  Mundial 2026                 S/ 150

Los objetos se guardan en una lista:

``` python
maquinas = [
    maquina_frutas,
    maquina_clasica,
    maquina_mundial
]
```

El menú principal se ejecuta dentro de un bucle `while`. El usuario
puede:

1.  Seleccionar una de las tres máquinas.
2.  Consultar las estadísticas de todas.
3.  Salir del casino.

Cuando se selecciona una máquina, `jugar_maquina(maquina)` inicia un
segundo bucle. En ese bucle se pueden realizar varias apuestas. Al
ingresar `0`, se regresa al menú principal.

Los objetos se crean una sola vez al iniciar el programa. Por eso, al
salir de una máquina y volver a seleccionarla, conserva sus créditos y
estadísticas durante esa ejecución.

Si una máquina llega a cero créditos, el menú muestra el estado
`SIN CRÉDITOS` y no permite iniciar otra jugada en ella.

## 10. Estadísticas del casino

La función `mostrar_estadisticas_todas(maquinas)` recorre la lista de
máquinas y muestra las estadísticas de cada una.

Después calcula los totales generales utilizando `sum()` y expresiones
generadoras:

-   **Total apostado:** suma de las apuestas aceptadas de todas las
    máquinas.
-   **Total ganado:** suma de los premios entregados por todas las
    máquinas.
-   **Total de jugadas:** suma de las jugadas ejecutadas.
-   **Créditos restantes:** suma de los saldos actuales.

El resumen general se muestra al seleccionar la opción 4 y también al
salir del casino.

## 11. Conceptos de Python practicados

Este proyecto reúne los siguientes conceptos:

-   **Clases y objetos:** definición de máquinas y creación de
    instancias.
-   **Constructor `__init__`:** inicialización de atributos.
-   **`self`:** acceso a los atributos y métodos del objeto actual.
-   **Herencia:** reutilización de la clase `Tragamonedas`.
-   **`super()`:** llamada al constructor de la clase padre.
-   **Sobrescritura de métodos:** modificación de `jugar()` en la
    máquina Mundial 2026.
-   **Encapsulación:** protección del saldo mediante `__creditos`.
-   **Métodos internos:** organización de operaciones compartidas.
-   **Listas:** administración de varias máquinas.
-   **Bucles `while` y `for`:** control del menú y de las jugadas.
-   **Condicionales `if`, `elif` y `else`:** validación de opciones y
    resultados.
-   **Manejo de excepciones `try/except`:** control de entradas que no
    son números.
-   **Módulo `random`:** selección aleatoria de símbolos.
-   **Funciones `sum()` y `enumerate()`:** cálculo de totales y
    recorrido numerado de máquinas.

## 12. Consideraciones y limitaciones

-   Los créditos y las estadísticas existen únicamente mientras el
    programa está ejecutándose. Al cerrar el programa, los datos vuelven
    a sus valores iniciales.
-   No existe una base de datos ni almacenamiento permanente.
-   Los resultados se generan aleatoriamente; no se garantiza una
    frecuencia específica de premios.
-   La visualización de emojis depende de la fuente y de la
    compatibilidad de la terminal utilizada.
-   Es un ejercicio educativo de Python y POO, no un sistema de apuestas
    con dinero real.

## 13. Posibles mejoras futuras

-   Guardar saldos y estadísticas en un archivo JSON o en una base de
    datos.
-   Incorporar una opción para reiniciar una máquina.
-   Permitir agregar nuevas máquinas desde el menú.
-   Crear una clase `Casino` que centralice la administración de las
    máquinas.
-   Agregar pruebas automatizadas para validar las reglas de premios.

------------------------------------------------------------------------

**Proyecto:** Casino Royale\
**Lenguaje:** Python\
**Enfoque:** Programación orientada a objetos (POO)\
**Versión:** 1.0
