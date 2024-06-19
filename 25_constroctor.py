# class Point5:
#     def __int__(self, x, y):
#         self.x = x
#         self.y = y
#         print(x)
#         print(y)
#     def move(self):
#         print('move')
#
#     def draw(self):
#         print('draw')
#
#
# point = Point5(10, 20)
# point.x = 11

class Person:

    def __init__(self, name_p):
        self.name_p = name_p

    def talk_style(self):
        print(f'Hi ,i am {self.name_p}')


name_p = str(input("Enter Your Name : "))
user=Person(name_p)
# print(user.name_p)
user.talk_style()


