# Function >>>>>>>>>>>>>>>>>>>>>>>>>>
# def great_user():
#     print('Hi there !')
#     print('Welcome ')

# print('start')
# great_user() # if  this function is not define then this functio not print

# # it is predefined func
# # def great_user():
# #     print('Hi there !')
# #     print('Welcome ')

# print('finish')


# Parameter >>>>>>>>>>>>>>>>>>>>>>>>>>

# def user(first_name,last_name):
#     print(f'Hi {first_name}')
#     print(f'Welcome to {last_name}')
# print('start')
# fn = str(input('Your name = '))
# n= fn.split(' ')
# # print(n[1])
# user(last_name=n[0],first_name=n[1]) #it parameter keyword change
# print('Stop')


# def cost_total(total, shiping, discount):
#     t=total+shiping+discount
#     print(t)
# user=input('')
# s=user.split(' ')
# print(s)
# s=cost_total(total=s[0],shiping=s[1],discount=[2])




# return statements >>>>>>>>>>>>>>>>>>>>>

def squre(num):
     print(num*num)
     return None
n=int(input('> '))
result = squre(n)
print(result)