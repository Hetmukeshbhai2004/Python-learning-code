# num = [5, 2, 9, 2, 4, 3, 7]
# num.append(20)
# num.insert(1, 3)
# num.remove(9)

# num.clear()
# print(num.index(9))
# print(num)

# print(num.count(2))
# num.sort()
# num.reverse()
#
# num2=num.copy()
# num.append(10)
# print(num2)
# num2 is copy variable, it means don't change original, when you edit num2,

# print(50 in num)


# Remove the duplicates in a list

num = [5, 2, 9, 2, 4, 3, 4, 5, 9, 9, 7]
num1=[]
for n in num:
    if n not in num1:
        num1.append(n)
num1.sort()
print(num1)