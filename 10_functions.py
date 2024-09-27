#Functions

def my_function():
    print("Esto es una función")

my_function() #Se tiene que llamar a la función para que funcione
my_function()
my_function()

def sum_two_values (first_number, second_number):
    print(first_number + second_number)

sum_two_values(5, 7)
sum_two_values(5324234, 2342347)
sum_two_values("5", "7") #Solo concatena los Strings
sum_two_values(1.4, 7.2)

def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name("José", "Odé")

def print_name_with_default(name, surname, alias = "Sin alias"): #Al darle un valor por defecto, ya no es necesario parametros para que funcione 
    print(f"{name} {surname} {alias}")

print_name_with_default("José", "Odé")

def print_texts(*text): #"*" convierte los parametros dinamicos
    print(text)

print_texts("Hola", "Puthon", "Dev")
print_texts("Hola")

def print_texts(*texts):
    for text in texts:
        print(text)

print_texts("Hola", "Puthon", "Dev")
print_texts("Hola")

def print_upper_texts(*texts): #Ej. de función con parametros arbitrarios
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Puthon", "Dev")
print_upper_texts("Hola")