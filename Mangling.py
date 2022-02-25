class Person:
    def __init__(self, name):
        self.__name = name

    def display(self):
        print(self.__name)


p1 = Person("Mayank")
p1.display()
# print(p1.name)
# print(p1.__name)
print(p1._Person__name)
