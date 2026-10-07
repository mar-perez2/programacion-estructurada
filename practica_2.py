saldo = float(input("Ingresa el saldo:"))
monto = float(input("Ingresa el monto:"))
retiro = float(input("Ingresa el retiro de hoy:"))
#########
if monto % 50!=0:
     print("monto no valido")
elif monto>saldo:
     print("saldo insuficiente")
elif retiro + monto>6000:
    print("limite diario excedido")

else:
   saldo= saldo-monto
print("entregado")
print("saldo restante",saldo)

print("Fin")