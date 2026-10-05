def main():
  ARCHIVO="empleados.txt"
  print("-"*80)
  total = 0.0
  cantidad = 0
  print(f"Acreditacion De Sueldos")
  print("-"*80)
  with open(ARCHIVO,"r",encoding="utf-8") as archivo:
    for linea in archivo:
      empleado=(linea.strip())
      legajo,nombre,cbu,salario=empleado.split(";")
    #   print(cbu)
      salario=float(salario)
      print(f"Se transfirio al CBU {cbu} el monto de ${salario}")
      total=total+salario
      cantidad=cantidad+1
    print("-"*80)  
    print(f"El monto total a transferir es {total}") 
    print(f"La cantidad de montos transferidos es {cantidad}")




if __name__ == "__main__":
	main()