
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hello(self):
        print("Hello, my name is", self.name)


    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"



person = Person("dk",6)

person.say_hello()


p = Person("hk", 3)
print(p)
print( person)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = heigcú
        return f"Rectangle with width={self.width} and height={self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


rect = Rectangle(4, 5)
print(str(rect)) # Output: Rectangle with width=4 and height=5
print(repr(rect)) # Output: Rectangle(4, 5)
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("John", 30)
print(repr(p)) # Output: Person('John', 30)

# Tái tạo đối tượng từ chuỗi biểu diễn
p2 = eval(repr(p))
print(p2.name) # Output: John
print(p2.age) # Output: 30

class congso:
    def __init__(self, so1, so2):
        self.so1 = so1
        self.so2 = so2

    def __add__(self, other):
        return congso(self.so1 + other.so1, self.so2 + other.so2)

c1 = congso(2, 3)
c2 = congso(4, 5)
c3 = c1 + c2
print(c3.so1)  # 6
print(c3.so2)  # 8
