## PYTHON ##

# Cracteristicas:
 
                # Lenguaje de alto nivel ( mas parecido al lenguaje natural)
                # Gramatica sencilla, clara y legible.
                # Tipado dinamico y fuerte.
                # Orientado a objetos 100%.
                # Open Source.
                # Libreria estandar muy amplia.
                # Interpretado
                # Vesatil (apps de escritorio, servidor, apps webs)

# Tipos de datos

        # Textos
        # Booleanos---- True / False
        # Numericos---- int  /  float  / Complejos

# Operadores
             # Aritmeticos ----  +  |  -  |  *  |  /  | modulo % |  Exponente **  | Division entera  //  ||
             # Comparacion ---- ==  |  != |  >  |  <  | >= |  >=  | 
             # Logicos -------- AND | OR  | NOT |     |    |   
             # Asignacion -----  =  | +=  | -=  | *=  | /= | %= | **= | //= |
             # Especiales -----  IS | IS NOT || IN | NOT IN ||

# Variable = Espacio en la memoria dond se almacenara un valor que podra cambiar durante la ejecucion.
      
    # Ejemplo variable: nombre = 5

# Funciones

# Funciones predefinidas:

                         # type(nombre) --> resultado -> <class 'int'>

                         #print(nombre)
'''
 numero1=5
 numero2=7

 if numero1>numero2:
    print("El numero 1 es mayor")
 else:
    print("El numero 2 es mayor")
'''   

# Sintaxis funcion

# def nombre_funcion(parametros):
   
   # Instrucciones de la funcion

   # return ( opcional )

# Primeras funciones

'''
def mensaje():

      print("Mensaje 1")
      print("Mensaje 2")
      print("Mensaje 3")

mensaje()
'''
# Mismos valores
'''
def suma():
    num1=5
    num2=7
    print(num1+num2)

suma()
'''
# Diferentes valores, parametros o argumentos
'''
def suma(num1,num2):

  print(num1+num2)

suma(5,7)
suma(3,7)
'''


'''
def suma(num1,num2):

 resultado=(num1+num2)

 return resultado

print(suma(8,8))

almacena_reultado=(suma(5,6))
print almacena_reultado   
'''

'''
def resta(num1,num2):

 num=1
 num=2
 print(num1-num2)

resta(5,5)
'''

#########  Listas  ##########################################################################################################

# Sintaxis --> nombrLista=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

##############  Ejemplo --> miLista=["El", "Ella", "Tu", "Yo"] ||

#############   Mostrar elementos -> print(miLista)  ||  print(miLista[0])  ||  print(miLista[0:3]) || print(miLista[2:]) || 

##############  Agregar elemento --> miLista.append ||  miLista.insert(2,"Nosotros")  || miLista.extend(["Vosotros", "Ellos"]) ||

##############  Buscar ------------> print(miLista.index("Nosotros")) || Comprobar si esta en lista print("Tu" in miLista) ||

##############  Eliminar ----------> miLista.remove("Tu") || Ultimo elemento --> mi.Lista.pop()  ||

############## Sumar listas ------> miLista3=miLista1+miLista2 (concadenar)

############## Repetir nombrLista=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 3 


#------------------------------------------------------------------------------------------------------#


###################################### TUPLAS ############################################################






