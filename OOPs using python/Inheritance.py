# There are two types of inheritance one is multi level inheritance and multiple inheritance
# both are possible in python because of MRO

class A:
    def a(self):
        print('a')

class B(A):
    def b(self):
        print('b')

b_object = B()
b_object.a()
