# Variables

#from operator import le

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_string_variable = str(my_int_variable)
print(my_int_to_string_variable)
print(type(my_int_to_string_variable))

my_bool_variable = True
print(my_bool_variable)

#Concatenación de variables en un print
print(my_string_variable, my_int_to_string_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

#Algunas funciones del sistema
print(len(my_int_to_string_variable))

#Variables en una sola linea
name, surname, alias, age = "José", "Odé", "Odesito", 32
print("Me llamo:", name, surname, ", mi edad es:", age, "y mi alias es:", alias) 

