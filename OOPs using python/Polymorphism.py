# Method overriding

class Bird:
    def fly(self):
        print('Bird can fly')


class Sparrow(Bird):
    def fly(self):
        print('Sparrow can fly')


class Crow(Sparrow):
    def walk(self):
        print('Crow can walk')


b = Bird()
b.fly()
s = Sparrow()
s.fly()
c = Crow()
c.fly()

print(Crow.mro())
print()


# Que. How multiple inheritance is possible in python?
# Ans. Because of MRO(Method Resolution Order) multiple inheritance is possible in python
class A:
    def hello(self):
        print('A')


class B:
    def hello(self):
        print('B')


class C(A, B):
    # def hello(self):
    #     print('C')
    pass


class D(B, A):
    # def hello(self):
    #     print("D")
    pass


print(C.mro())
print(D.mro())
d = D()
d.hello()

c = C()
c.hello()
print()


# Method Overloading

class Calculator:
    def sum(self, a, b, c=0):
        return a + b + c

    def add(self, *args):
        s = 0
        for i in args:
            s += i
        return s


c = Calculator()
print(c.sum(1, 3))
print(c.sum(1, 2, 3))
print(c.add(1))
print(c.add(1, 2))
print(c.add(1, 2, 3))
print(c.add(1, 2, 3, 4))

