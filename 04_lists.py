#Lists

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [32, 1.74, "José", "Odé"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4]) #Los menos hacen que se enumeren del ultimo al primero "Ej: 32"
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError 

age, height, name, surname = my_other_list
print(name)

print(my_list + my_other_list)

my_other_list.append("Enterprice") #Aumente el nuevo item al final de la lista
print(my_other_list)

my_other_list.insert(1, "negro") #Inserta el nuevo item en la posicion senalada
print(my_other_list)

my_other_list[1] = "verde" #Modifica un el item especificado []
print(my_other_list)

my_other_list.remove("verde") #Elimina el item indicado ""
print(my_list)

del my_list[2] #Elimina el item por indice []
print(my_other_list)

my_list.pop() #Elimina el ultimo elemento por defecto
print(my_list)

my_new_list = my_list.copy() #Copia la lista, se puede modificar la antigua lista sin afectar la copia

my_list.clear() #Limpia toda la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() #Invierte la lista
print(my_new_list)

my_new_list.sort() #Ordena de menor a mayor por defecto
print(my_new_list) 

print(my_new_list[1:3]) #Ordena por sub-listas

my_list = "Hola Python" #Cambio a String y dejo de ser lista!!!
print(my_list)
print(type(my_list))