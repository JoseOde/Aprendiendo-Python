#Error Types

#SyntaxError
#print "¡Hola comunidad!"
print("¡Hola comunidad!")

#NameError
language = "Spanish" #Si se comenta esta linea, no se ha declarado la variable, de ahi el error
print(language)

#IndexError
my_list = ["Python", "Swift", "Java", "C#", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[5]) #El indice esta fuera del rango

#ModuleNotFoundError
#import maths #No existe el modulo "maths" es math
import math

#AttributeError
#print(math.PI) #El atributo esta en mayusculas=no existe "PI" 
print(math.pi)

#KeyError
my_dict = {"Nombre":"José", "Apellido":"Odé", "Edad":35, 1:"Python"}
print(my_dict["Edad"])
#print(my_dict["Apelido"]) #Error en la key, no existe "apelido"

#TypeError
#print(my_list["Edad"]) #Error de tipo, para lista Ej.[0] no en string ""

#ImportError
#from math import PI #pi esta en mayusculas
from math import pi

#ValueError
my_int = int("10")
#my_int = int("10 años") #Error de valor "10" si puede volverse entero pero "años" no
print(type(my_int +5))

#ZeroDivisionError
print(4/2)
#print(4/0) #No se puede dividir entre "0" 