



1. Para el siguiente ejercicio, defina una expresión regular para el siguiente lenguaje: [El conjunto de movimientos del ajedrez como p->k4 o kbp X qn].
  Implemente el AFD para esta expresión regular. Use Python.

    Notación Descriptiva del Ajedrez:
    Es una manera de expresar los movimientos de las piezas en un partido de ajedrez, se indica la pieza que se mueve y a las coordenadas a las que llega,
    también se indica si la pieza movida capturó a otra pieza o no.
    Las coordenadas en la notación descriptiva son distintas a como se escribe actualmente, en notación descriptiva las columnas se identifican con la pieza
    que caracteriza esa posición mientras que las filas van del 1 al 8, contándolas desde la perspectiva de cada color.
    
    <img width="392" height="389" alt="image" src="https://github.com/user-attachments/assets/d580c6b6-58e7-48d4-b311-6727dcee89ae" />

    Columnas: QR, QN, QB, Q, K, KB, KN, KR
    Filas: 1, 2, 3, 4, 5, 6, 7, 8
    Piezas: R, N, B, Q, K, P
    Movimiento: -
    Captura: x
    Jaque: +
   Jaque Mate: #
   Enroque del lado del rey: 0-0
   Enroque del lado de la reina: 0-0-0
   1-0: Ganaron las blancas
   0-1: Ganaron las negras
   
