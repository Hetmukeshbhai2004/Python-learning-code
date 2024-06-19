# Dic = {
#     'name ':'Het Patel',
#     'age': 30,
#     'is_verified':True
# }
# # Dic.get('name1 ''Patel Dev')
# Dic['name1 ']='Patel Dev'
# print(Dic['name1 '])

user = input('>>> ')

dic = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',

}
out = ''

for i in user:
    out += dic.get(i, '!') + (' ')
print(out)
