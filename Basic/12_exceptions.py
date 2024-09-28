#Exceptions Handling

numberOne = 5
numberTwo = 1
numberTwo = "1"

# if numberOne == int:
#     print(numberOne + numberTwo)
# else:
#     print("No se cumplió") En este Ej. se esta haciendo un manejo del error de manera manual


#try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    #Se ejecuta si se produce una excepción
    print("Se ha producido un error")
    

#try except else

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    #Se ejecuta si no se produce una excepción (opcional)
    print("La ejecución continúa correctamente")

#try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    print("La ejecución continúa correctamente")
finally:
    #Se ejecuta siempre (opcional)
    print("La ejecución continúa")

#Captura de excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError:
    #Se ejecuta si se produce una excepción de tipo TypeError
    print("Se ha producido un error")
except ValueError:
    #Se ejecuta si se produce una excepción de tipo ValueError
    print("Se ha producido un error")

    #Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as error:
    print(error)