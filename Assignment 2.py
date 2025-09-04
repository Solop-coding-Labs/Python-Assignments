#Question 1
class Vehicle:
    def __init__(self, brand, model):
        self.brand= brand
        self.model= model
    def start_engine(self):
        return f'In this {self.brand} {self.model} there are two subclasses which are car and bike.'
class Car(Vehicle):
    def start_engine(self):
        return f'The car {self.brand} {self.model} is a very durable vehicle but lacks comfort as it not part of a luxury line.'
class Bike(Vehicle):
    def start_engine(self):
        return f'The bike {self.brand} {self.model} is an Italian fast cruising motorcycle with a powerful engine.'
vehicle= Vehicle('vehicle' , 'class')
car= Car('Toyota', 'Corolla bubble')
bike= Bike('BMW' , 'S1000R')

print(vehicle.start_engine())
print(car.start_engine())
print(bike.start_engine())

#Question 2
import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height


def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

myshapes = Circle(3), Rectangle(4, 5), Circle(2), Rectangle(2, 3)

print(f"Total area:", total_area(myshapes))

#Question 3

class Shape:
    def __init__(self, name="GenericShape"):
        self.name = name
        print(f"Shape.__init__ called: Initialized shape with name '{self.name}'")

    def calculate_area(self):
        print("Shape.calculate_area called (does nothing)")

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def calculate_area(self):
        super().__init__("RectangleFromArea")

        super().calculate_area()

        area = self.width * self.height
        print(f"Rectangle.calculate_area: width={self.width}, height={self.height}, area={area}")
        return area

rect = Rectangle("MyRectangle", 5, 10)
print(f"Initial name: {rect.name}")

area1 = rect.calculate_area()
print(f"Area: {area1}")
print(f"Name after calculate_area: {rect.name}")


#Question 4

def process_sound(sound_object):
    print("Processing sound...")
    sound_object.make_sound()  # No need to check type

class Dog:
    @staticmethod
    def make_sound():
        print("Woof!")

class Cat:
    @staticmethod
    def make_sound():
        print("Meow!")

dog = Dog()
cat = Cat()
process_sound(dog)
process_sound(cat)

#Quesstion 5
from abc import ABC, abstractmethod

class FileHandler(ABC):

    @abstractmethod
    def read(self, file_path):
        """Read data from a file"""
        pass

    @abstractmethod
    def write(self, file_path, data):
        """Write data to a file"""
        pass

class TextFileHandler(FileHandler):

    def read(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content

    def write(self, file_path, data):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)

class BinaryFileHandler(FileHandler):

    def read(self, file_path):
        with open(file_path, 'rb') as file:
            content = file.read()
        return content

    def write(self, file_path, data):
        with open(file_path, 'wb') as file:
            file.write(data)

if __name__ == "__main__":
    text_handler = TextFileHandler()
    binary_handler = BinaryFileHandler()

    text_handler.write("example.txt", "Hello, is today a good or day like any other")
    print(text_handler.read("example.txt"))

    binary_handler.write("example.bin", b"\x00\x01\x0110")
    print(binary_handler.read("example.bin"))






