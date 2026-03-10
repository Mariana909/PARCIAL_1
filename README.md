# Parcial 1 — Lenguajes y Procesamiento de Texto

## Requisitos

- Python
- Java
- gcc
- ghc
- flex
- bison
- ANTLR4

---

## Punto 1 — AFD Movimientos de Ajedrez

### Descripción

Definición de una expresión regular para el conjunto de movimientos del ajedrez en notación descriptiva, e implementación de un AFD en Python.

La notación descriptiva es una manera de expresar los movimientos de las piezas en un partido de ajedrez. Se indica la pieza que se mueve y las coordenadas a las que llega, también se indica si la pieza movida capturó a otra pieza o no.

Las coordenadas en la notación descriptiva son distintas a como se escribe actualmente: las columnas se identifican con la pieza que caracteriza esa posición, mientras que las filas van del 1 al 8, contándolas desde la perspectiva de cada color.

<img width="392" height="389" alt="image" src="https://github.com/user-attachments/assets/d580c6b6-58e7-48d4-b311-6727dcee89ae" />

### Elementos del lenguaje

| Elemento | Valores |
|---|---|
| Filas | 1, 2, 3, 4, 5, 6, 7, 8 |
| Pieza con Columnas | QR, QN, QB, Q, K, KB, KN, KR, KRP, KNP, KBP, QBP, QNP, QRP |
| Piezas | R, N, B, Q, K, P |
| Movimiento | `->` |
| Captura | `X` |
| Jaque | `+` |
| Jaque Mate | `#` |
| Enroque lado del rey | `0-0` |
| Enroque lado de la reina | `0-0-0` |
| Ganaron blancas | `1-0` |
| Ganaron negras | `0-1` |

### Estructura de un movimiento

**Sin captura:**
```
[Pieza] -> [Columna][Fila] [+/#]?
```
Ejemplo: `knp->q6` o `p->q6`

**Con captura:**
```
[Pieza] X [Pieza] [Fila?] [+/#]?
```
Ejemplo: `kb X qn` o `b X n`

### Solución

Para el AFD se decidió aceptar las versiones en mayúscula y en minúscula de las jugadas con la estructura descrita en el enunciado. No se tienen en cuenta los casos especiales como `0-0` y `0-0-0`.

### Ejecución

```bash
python afd.py entrada.txt
```

### Salida

<img width="91" height="255" alt="image" src="https://github.com/user-attachments/assets/d2b772d1-918a-4e2d-b2a4-1b93f9f30e69" />

---

## Punto 2 — AFD Identificadores

### Descripción

Implementación de un AFD en Python para la expresión regular:

```
[A-Za-z][A-Za-z0-9]*
```

Esta expresión regular acepta cadenas que empiecen con una letra (mayúscula o minúscula), seguida o no por una combinación de letras y números. No acepta cadenas que empiecen con números o que contengan símbolos diferentes a letras y números.

### Ejecución

```bash
python afd2.py entrada2.txt
```

### Salida

<img width="91" height="202" alt="image" src="https://github.com/user-attachments/assets/ecb00156-0fd0-4641-9ae3-a4b8fbac55ac" />

---

## Punto 3 — Calculadora con Raíz en Flex y Bison

### Descripción

Programa en C que implementa una calculadora capaz de sacar la raíz cuadrada de números reales, usando Flex y Bison. Para el cálculo de la raíz cuadrada se usa el método numérico Newton-Raphson.

La entrada es por archivo de texto y la salida por consola. Tomando como base la calculadora del ejercicio 3 del primer capítulo (quitando las operaciones bitwise), se anexa la operación raíz.

La raíz se expresa como `raiz(9)`, lo que daría como resultado `3`.

### Ejecución

<img width="511" height="284" alt="image" src="https://github.com/user-attachments/assets/e710f3d8-cc24-435e-b0f0-32b85d170381" />

### Salida con entrada3.txt

<img width="373" height="320" alt="image" src="https://github.com/user-attachments/assets/1b7e5031-d7bd-4241-bd85-6aad5a0f6653" />

---

## Punto 4 — Comparación de Rendimiento: C vs Haskell

### Descripción

Comparación de rendimiento del algoritmo recursivo de Euclides entre C (lenguaje imperativo) y Haskell (lenguaje declarativo).

### Algoritmo de Euclides

El algoritmo se usa para hallar el máximo común divisor de dos números mediante el módulo.

**Pseudocódigo:**
```
Funcion mcd(a, b):
    Si b == 0:
        Retornar a
    Si no:
        Retornar mcd(b, a MOD b)
```

### Métrica de comparación

Para comparar el rendimiento se mide el tiempo que tarda cada función en calcular el resultado:
- En **C** se usa `time.h`
- En **Haskell** se usa `System.CPUTime`

### Ejecución

<img width="729" height="94" alt="image" src="https://github.com/user-attachments/assets/e66cabb8-65d8-4a04-bac7-516d917d2579" />

<img width="706" height="153" alt="image" src="https://github.com/user-attachments/assets/00205467-3fd7-4f34-a6a6-1dc56512db37" />

### Resultados con entrada `701408733 433494437`

| Lenguaje | Resultado | Tiempo |
|---|---|---|
| C | 1 | 0.000002 s |
| Haskell | 1 | 0.001954 s |

```
0.001954 s - 0.000002 s = 0.001952 s
Haskell tarda 0.001952 s más que C
```

### Análisis

Con entradas grandes como números de Fibonacci consecutivos `(701408733, 433494437)`, C ejecuta en microsegundos mientras Haskell tarda milisegundos. Esto se debe principalmente al overhead del runtime de Haskell y su evaluación lazy:

- **C** compila directamente a código máquina, sin overhead en tiempo de ejecución y con gestión de memoria directa.
- **Haskell** incluye el costo de inicializar su runtime, el garbage collector y la evaluación lazy, que retrasa el cómputo hasta que el resultado es necesario.

---

## Punto 5 — Serie de Maclaurin para e^x con ANTLR

### Descripción

Programa en ANTLR con lenguaje objetivo Python que calcula los primeros `n` términos de la serie de Maclaurin para `e^x`.

```
e^x = x^0/0! + x^1/1! + x^2/2! + ... + x^n/n!
```

La gramática se define en `maclaurin.g4`, donde se definen los tokens que acepta el lenguaje: números reales y la palabra `exp`.

**Formato de entrada:**
```
EXP(x, n)
```
Donde `x` es el exponente (entero o decimal, puede ser negativo) y `n` es el número de términos (entero positivo).

### Ejecución

<img width="262" height="32" alt="image" src="https://github.com/user-attachments/assets/574979b3-d48c-4adb-9b35-27ed1cfcee78" />

### Ejemplo de salida

<img width="499" height="402" alt="image" src="https://github.com/user-attachments/assets/8712c4ea-d73d-4b51-9988-b66ea66bedfb" />
