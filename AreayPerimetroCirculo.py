#CÓDIGO PARA CALCULAR ÁREA X Y PERÍMETRO Y DE UN CÍRCULO

#IMPORTAR BIBILIOTECA
import math

# #ENTRADA DE DATOS
    #Valor de radio

número_1 = float (input("Ingrese LONGITUD de RADIO en CENTIMETROS:")) 
PI = 3.1416

#PROCESO
multiplicación = PI * (número_1 **2)
potencia = PI * (número_1 *2)

#SALIDA Y EJECUCIÓN
print("El resultado de área es= ", round(multiplicación))
print("y perímetro es= ", round(potencia))
