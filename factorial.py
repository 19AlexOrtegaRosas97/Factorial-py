#@author: Alejandro Ortega Rosas
import sys
def factorial(num):
    if (num==1):
    	print("1 Multiplicaciones")
    else:
    	print(num, end=" * ")
    if(num!=1):
        num=num*factorial(num-1)
    print("Valor final es igual a ->",num) 
    return num

if(len(sys.argv)==2):
	try:
 		valor = int(sys.argv[1])
 		if(valor <= 0):
 			print("Que chistoso :) el parametro debe ser entero positivo")
 			bandera=False
 		else:
 			bandera=True
	except:
		print("Error el parametro No puede tener letras")
		bandera=False

	if(bandera==True):
		factorial(valor)		
else:
	print("Error introduce los argumentos correctamente")
	print("Ejemplo: factorial.py 123")

