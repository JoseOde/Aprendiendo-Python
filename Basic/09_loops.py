#Loops

#While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition +=2
else: #Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecucion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es 15")
        break

    print(my_condition)

print("La ejecucion continua")

#For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (32, 1.74, "José", "Odé")

for element in my_tuple:
    print(element)

my_set = {"José", "Odé", 32}

for element in my_set:
    print(element)

my_dict = {"Nombre":"José", "Apellido":"Odé", "Edad":32, 1:"Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
else: 
    print("El bucle for para diccionario ha finalizado")