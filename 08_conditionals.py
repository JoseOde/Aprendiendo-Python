#Conditionals

my_condition = False

if my_condition: #Para que se ejecute la condición debe ser VERDADERO!!!
    print("Se ejecuta la condicion del if")

my_condition = 5 * 5 

if my_condition == 10: # Aca se le obliga a comprobar algo en concreto no solo que tenga un valor 
    print("Se ejecuta la condicion del segundo if")

if my_condition > 10 and my_condition <20:
    print("Es mayor que 10 y menor que 20") 
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual a 20") 

print("La ejecucion continua")

my_string = "" #Si la cadena de texto esta vacia el IF lo tomara como un False!!!

if not my_string:
    print("Mi cadena de texto es vacia")