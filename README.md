Requisitos
  * Python
  * Antlr4


1. Para el siguiente ejercicio, defina una expresión regular para el siguiente lenguaje: [El conjunto de movimientos del ajedrez como p->k4 o kbp X qn].
  Implemente el AFD para esta expresión regular. Use Python.

    Notación Descriptiva del Ajedrez:
    Es una manera de expresar los movimientos de las piezas en un partido de ajedrez, se indica la pieza que se mueve y a las coordenadas a las que llega,
    también se indica si la pieza movida capturó a otra pieza o no.
    Las coordenadas en la notación descriptiva son distintas a como se escribe actualmente, en notación descriptiva las columnas se identifican con la pieza
    que caracteriza esa posición mientras que las filas van del 1 al 8, contándolas desde la perspectiva de cada color.
    
    <img width="392" height="389" alt="image" src="https://github.com/user-attachments/assets/d580c6b6-58e7-48d4-b311-6727dcee89ae" />

    Filas: 1, 2, 3, 4, 5, 6, 7, 8
    Pieza con Columnas: QR, QN, QB, Q, K, KB, KN, KR, KRP, KNP, KBP, QBP, QNP, QRP
    Piezas: R, N, B, Q, K, P
    Movimiento: -
    Captura: x
    Jaque: +
    Jaque Mate: #
    Enroque del lado del rey: 0-0
    Enroque del lado de la reina: 0-0-0
    1-0: Ganaron las blancas
    0-1: Ganaron las negras

    Descripción de un Movimiento sin captura
   
    [Pieza] - [Columna][Fila] [+/#]?
   
    Ej: KNP-Q6 o P-Q6
   
    Pero en el enunciado:
    [Pieza] -> [Columna][Fila] [+/#]?

    Ej: knp->q6 o p->q6
   
    Descripción de un Movimiento con captura
    [Pieza] x [Pieza] [Fila?] [+/#]?

    Ej: KBxQN o BxN
   
    Pero en el enunciado:
    [Pieza]  X  [Pieza] [Fila?] [+/#]?

    Ej: kb X qn o b X n

    Solución:
    Para el AFD se decidió aceptar las versiones en mayúscula y en minúscula de las jugadas con la estructura descrita en el enunciado.
    [Pieza] -> [Columna][Fila] [+/#]?    y      [Pieza] X [Pieza] [Fila?] [+/#]?
    No se tendrán en cuenta los casos especíales como 0-0 y 0-0-0

    Para ejecutar: python afd.py entrada.txt
    
3. [𝐴 − 𝑍𝑎 − 𝑍][𝐴 − 𝑍𝑎 − 𝑧0 − 9] *. Implemente un AFD en Python. Realice mínimo 5 pruebas, tres donde “ACEPTE” y dos donde “NO ACEPTE”
   
  Esta expresión regular nos dice que solo acepta cadenas que empiecen con una letra (ya sea mayúscula o minúscula), esta podría estar seguida o no
  por una combinación de letras (ya sean mayúsculas o minúsculas) y de números, la expresión regular no acepta cadenas que empiezan con números o
  cadenas que contengan símbolos diferentes a letras y números.

  Para ejecutar: python afd2.py entrada2.txt
  
3. Escriba un programa en C que implementa una calculadora que pueda sacar raíz cuadrada de números reales. Use flex y Bison. Para el cálculo de la raíz cuadrada use el método numérico Newton-Raphson [ver enlace]. La entrada debe ser por un archivo de texto y la salida debe ser por consola.
