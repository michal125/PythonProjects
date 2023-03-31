from abc import ABC, abstractmethod
from copy import deepcopy


#fabryka

class Pet:
    def __init__(self, name):
        self.name = name

class Dog(Pet):
    def speak(self):
        return "Woof"

class Cat(Pet):
    def speak(self):
        return "Meow"

class PetFactory:
    def get_pet(self, pet_type, name):
        if pet_type == "dog":
            return Dog(name)
        elif pet_type == "cat":
            return Cat(name)
        else:
            return None

factory = PetFactory()
pet = factory.get_pet("dog","Fido")
print(pet.speak())

pet = factory.get_pet("cat", "Fluffy")
print(pet.speak())

##########

#budowniczy

class Builder(ABC):
    ##INTERFEJS DLA BUDOWNICZEGO

    @abstractmethod
    def add_engine(self):
        pass

    @abstractmethod
    def add_wheels(self):
        pass

    @abstractmethod
    def add_body(self):
        pass

    @abstractmethod
    def get_result(self):
        pass

class CarBuilder(Builder):
    #BUDOWNICZY

    def __init__(self):
        self._car = car

    def add_enqine(self):
        self._car.add_part("enqine", "V8")

    def add_wheels(self):
        self._car.add_part("wheel","4")

    def add_body(self):
        self.car.add_part("body","sedan")

    def get_result(self):
        return self._car

class Car:
    def __init__(self):
        self_.parts = {}

    def add_part(self, key, value):
        self_parts[key] = value

    def __str__(self):
        return f"Car with {self._parts['enqine']} enqine, {self._parts['wheel']} wheels and {self._body['body']} body"

class Director:
    #TUTAJ STERUJEMY JAKBYSMMY CHCIELI ZBUDOWAC AUTO INNEGO TYPU

    def __init__(self,builder):
        self._builder = builder
    def construct_car(self):
        self._builder.add_engine()
        self._builder.add_wheels()
        self._builder.add_body()

director = Director(Builder)

####
#Prototyp
class School:
    def __init__(self,name):
        self.name = name

    #def copy(self):
     #   return School(self.name) stare podejscie bez wzorca

class Student:
    def __init(self, last_name: str, school: School):
        self.last.name = last.name
        self.school = school

school = School("Szkola A")
this_is_student = Student()
print("school", id(school))
print("student's school", id(this_is_student))
print("student", id(this_is_student))


this_is_student_copy = deepcopy(this_is_student)
print("-----"*10)
print("COPY school", id(school))
print("COPY student's school", id(this_is_student_copy))
print("COPY student", id(this_is_student_copy))

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

person = Person("John", 38)
copy = deepcopy(person)
copy.name = "Bill"

print("Orginal person: ", person.name, person.age)
print("Copy person: ", copy.name, copy.age)