# hot=False
# cold=True
#
# h = 'hot'
# c = 'cold'
# a = str(input('Enter Queter Name : '))
# if a == h:
#     print('It is a hot day,')
#     print('Drink plenty of water.')
# elif a == c:
#     print('It is cold day,')
#     print('Wear Worm cloths.')
# else :
#     print('It is rainy day,')
#     print('wear rain cort.')
# print('Enjoy your day')


# example

print('>> Price of a house is $1M')
a = str(input('True/False : '))
good_creadit = a
prise = 1000000

if good_creadit:
    print('They Need to put down 10%')
    down = 0.1 * prise
else:
    print('They Need to put down 20%')
    down = 0.2 * prise

print(f'Down payment:{down}')
