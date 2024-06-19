# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.
# when same data in different class
#     then it use inheritance and made a parent class and it is call in child class


class Mammul:      #parent class
    def walk(self):
        print('walk')

class Dog(Mammul):      #child class
    pass

class Cat(Mammul):      #child class
    pass

dog1=Dog()
dog1.walk()
