#Strings

my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

#Formateo

name, surname, age = "José", "Odé", 32

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) #No es una buena practica!!!
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #La más útil!!!

#Desempaquetado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e) 

#División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

#Reverse

reversed_language = language[::-1]
print(reversed_language)

#Funciones

print(language.capitalize()) #Pone en mayuscula la primera letra
print(language.upper()) #Pone en mayusculas toda la palabra
print(language.count("t")) #cuenta la cantidad del valor ""
print(language.isnumeric()) #Nos dice si es un numero con "boolean"
print(language.lower()) #Pone en minusculas toda la palabra
print(language.upper().isupper()) #isupper comprueba con "boolean" si es mayuscula
print(language.startswith("Py")) #Nos dice con "boolean" si es verdad que comienza con ""
print("Py" == "py") #No es lo mismo