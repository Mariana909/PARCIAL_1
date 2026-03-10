import sys

def afd(entrada):
    entrada = entrada.upper()
    piezas = ['KRP', 'KNP', 'KBP', 'QBP', 'QNP', 'QRP',
              'QR', 'QN', 'QB', 'KB', 'KN', 'KR',
              'Q', 'K', 'R', 'N', 'B', 'P']
    columnas = {'QR', 'QN', 'QB', 'Q', 'K', 'KB', 'KN', 'KR'}
    filas = {'1','2','3','4','5','6','7','8'}
    jaque = {'+', '#'}
    
    q = 0
    qf = [5, 6, 7]
    token = ""

    e = 0
    while e < len(entrada):
        s = entrada[e]

        if q == 0:
            # acumulamos letras esperando pieza
            if s.isalpha():
                token += s
                siguiente = entrada[e+1] if e+1 < len(entrada) else ""
                if siguiente in (' ', '-', 'X') or siguiente == '':
                    if token in piezas:
                        q = 1
                        token = ""
                    else:
                        break
            else:
                break

        elif q == 1:
            # esperamos -> o espacio+X
            if s == ' ':
                pass  # ignorar espacio
            elif s == '-':
                siguiente = entrada[e+1] if e+1 < len(entrada) else ""
                if siguiente == '>':
                    q = 2
                    e += 1  # saltar el >
                else:
                    break
            elif s == 'X':
                q = 3
            else:
                break

        elif q == 2:
            # movimiento normal: esperamos columna
            if s.isalpha():
                token += s
                siguiente = entrada[e+1] if e+1 < len(entrada) else ""
                if siguiente.isdigit() or siguiente == '':
                    if token in columnas:
                        q = 4
                        token = ""
                    else:
                        break
            else:
                break

        elif q == 3:
            # captura: esperamos pieza capturada
            if s == ' ':
                pass  # ignorar espacio
            elif s.isalpha():
                token += s
                siguiente = entrada[e+1] if e+1 < len(entrada) else ""
                if siguiente.isdigit() or siguiente in jaque or siguiente == '':
                    if token in piezas:
                        q = 6
                        token = ""
                    else:
                        break
            else:
                break

        elif q == 4:
            # movimiento normal: esperamos fila
            if s in filas:
                q = 5
            else:
                break

        elif q == 5:
            # estado de aceptación: opcional jaque
            if s in jaque:
                q = 7
            else:
                break

        elif q == 6:
            # captura: opcional fila
            if s in filas:
                q = 5
            elif s in jaque:
                q = 7
            else:
                break

        e += 1

    if q in qf:
        print("ACEPTA")
    else:
        print("NO ACEPTA")

try:
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as en:
            datos = en.read().splitlines()
            for i in datos:
                if i.strip():
                    afd(i.strip())
    else:
        print("No se detectó archivo de entrada")
except FileNotFoundError:
    print("No se encontró el archivo")
except Exception as ex:
    print(f"Error: {ex}")
