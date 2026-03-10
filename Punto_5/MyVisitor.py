from MaclaurinVisitor import MaclaurinVisitor

class MyVisitor(MaclaurinVisitor):

    def visitExpr(self, ctx):
        x = self.visit(ctx.numero())
        n = int(ctx.n.text)          # ← ctx.n por el alias
        
        print(f"e^{x} con {n} términos:\n")
        
        termino = 1.0   # término 0 = x⁰/0! = 1
        suma    = 1.0   # se suma el término 0
      
        # Todo se muestra con 6 decimales
        print(f"  término 0: x⁰/0! = 1.000000  →  suma: {suma:.6f}")
        
        for k in range(1, n):
            # cada término = término anterior * x/k
            # esto equivale a x^k/k! sin recalcular
            termino *= x / k
            suma    += termino
            print(f"  término {k}: x^{k}/{k}! = {termino:.6f}  →  suma: {suma:.6f}")
        
        print(f"\ne^{x} ≈ {suma:.6f}")
        print(f"Valor real: {2.718281828459045 ** x:.6f}")
        return suma

    def visitNumero(self, ctx):
        signo = -1 if ctx.SIGNO() and ctx.SIGNO().getText() == '-' else 1
        
        if ctx.DECIMAL():
            valor = float(ctx.DECIMAL().getText())
        else:
            valor = float(ctx.ENTERO().getText())
        
        return signo * valor
