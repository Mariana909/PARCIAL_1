import sys
# ID = [𝐴 − 𝑍𝑎 − 𝑍][𝐴 − 𝑍𝑎 − 𝑧0 − 9] *
# Estados ={q0,q1}
# Estado de inicio = q0
# Estados de aceptacion = {q1}
def afd2(string):
    q0=0
    qf=1
    q=q0
    for i in string:
        if q==q0:
            if i.isalpha():
                q=qf
            else:
                break
        elif q==qf:
            if i.isalnum():
                q=qf
            else:
                break
    if q==qf:
        print("ACEPTA")
    else:        
        print("NO ACEPTA")
try:
	if len(sys.argv) > 1:
		entrada = sys.argv[1]
		with open(entrada, 'r') as en:
			datos = en.read().split()
			for i in datos:
				afd2(i)
	else:
		print("No se detectó archivo de entrada")

except:

	print(" No se encontró el archivo")   
