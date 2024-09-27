#Dictionaries
#La cualidad más grande del diccionario es la facilidad para encontrar un elemento!!!

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"José", "Apellido":"Odé", "Edad":35, 1:"Python"}

my_dict = {
    "Nombre":"José",
    "Apellido":"Odé",
    "Edad":35,
    "Lenguajes": {"Python", "Java", "C#"},
    1:1.74
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro" #Se puede actualizar la variable desde la misma clave
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle Bolivar" #Asi se puede agrgar un nuevo campo al diccionario
print(my_dict)

del my_dict["Calle"] #Forma de eliminar elementos ""
print(my_dict)

print("José" in my_dict)
print("Nombre" in my_dict) #La busqueda se hace en la clave

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict) #Los keys que no existan se mostrara sin valores
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict) #Esta seria la forma correcta para aprovechar realmente el "fromkeys" 
print((my_new_dict))

my_new_dict = dict.fromkeys(my_dict, "Odé") #De esta forma se le pasa el valor a todas las claves Error!!!
print((my_new_dict))