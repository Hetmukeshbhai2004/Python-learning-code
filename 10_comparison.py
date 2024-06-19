# if temprature is greater than 30
#     it is a hot day
# otherwise if it is less than 10
#     it is a cold day
# otherwise
#     it is neighter hot nor cold

# user = int(input('Temp : '))
#
# if user >= 30:
#     print('It is a hot day')
# elif user<10:
#     print('It is a cold day')
# else:
#     print('It is normal temprature')


name = str(input('Enter Your Name : '))
if len(name) < 3:
    print('at least 3 charactr in your name') 
elif len(name) > 50:
    print('name must be max 50 character ')
else:
    print('Looks good')
