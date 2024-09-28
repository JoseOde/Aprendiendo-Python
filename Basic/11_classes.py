#Classes

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

my_person = Person("José", "Odé")
print(f"{my_person.name} {my_person.surname}")


class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"
    
    def walk(self):
        print(f"{self.full_name}  Está caminando")

my_person = Person("José", "Odé")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Dayana", "Salvador", "MiAmor")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Hector de Leon (El loco de los perros)"
print(my_other_person.full_name)