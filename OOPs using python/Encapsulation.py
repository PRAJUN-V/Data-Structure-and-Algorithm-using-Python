class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # This is private attribute

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


p1 = Person("Prajun", 23)
print(p1.name)
# print(p1.__age) # This will cause error because age is private
print(p1.get_age())
p1.set_age(24)
print(p1.get_age())
