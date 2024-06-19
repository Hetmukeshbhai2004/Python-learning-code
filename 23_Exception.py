try:
    age = int(input('Age : '))
    income=20000
    r=income/age
    print(age)
except ZeroDivisionError:
    print('Age Cant be Zero.')
except ValueError:
    print('Invalid Value')
