weight = float(input('Enter Your weight : '))
l_k = str(input('(L)bs Or (K)g : '))
if l_k.upper() == "L":
    w = weight / 2.2
    print(f'Your Weight is {w} Kilograms.')
else:
    w = weight * 2.2
    print(f'Your Weight is {w} pounds.')
