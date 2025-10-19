class Shape:
    def area(self):
        print("Any area")


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):  # instance method
        print(f"Area of rectangle: {self.width * self.length}")


class Triangle:
    def __init__(self, t_width, t_length):
        self.t_width = t_width
        self.t_length = t_length

    def area(self):  
        print(f"Area of triangle: {0.5 * self.t_width * self.t_length}")



r = Rectangle(4, 5)
r.area()  

t = Triangle(4, 5)
t.area()  



class Dog:
    def speak(self):
        return "woof"

class Cat:
    def speak(self):
        return "meow"

class Duck:
    def speak(self):
        return "quack"


animals = [Dog(), Cat(), Duck()]

for animal in animals:
    print(animal.speak())



class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class Motorcycle(Vehicle):
    pass  


bike = Motorcycle("Yamaha", "MT-07", 2023)
print(bike.make)   
print(bike.model)  
print(bike.year)   





class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position


class Developer(Person, Employee):
    def __init__(self, name, age, employee_id, position, programming_language):
        Person.__init__(self, name, age)       
        Employee.__init__(self, employee_id, position)  
        self.programming_language = programming_language

dev = Developer("Alice", 30, "E123", "Software Engineer", "Python")
print(dev.name)                
print(dev.age)                  
print(dev.employee_id)          
print(dev.position)             
print(dev.programming_language) 




class Animal:
    def eat(self):
        print("The animal is eating.")

class Bird(Animal):
    def eat(self):  
        print("The bird is pecking at seeds.")

    def fly(self):  
        print("The bird is flying high in the sky!")


b = Bird()
b.eat()  
b.fly()  

class Swimmer:
    def swim(self):
        print("The animal is swimming.")


class Walker:
    def walk(self):
        print("The animal is walking.")

class Amphibian(Swimmer, Walker):
    pass 


frog = Amphibian()
frog.swim()  
frog.walk()  



class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        
        super().speak()
        
        print("Dog barks")


d = Dog()
d.speak()

import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height


def print_areas(shapes):
    for shape in shapes:
        print(f"{shape.__class__.__name__} area: {shape.area():.2f}")


shapes = [Circle(5), Rectangle(4, 6), Circle(2)]
print_areas(shapes)
