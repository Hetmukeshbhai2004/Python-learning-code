# def lbs_to_kg(weight):
#     # w = float(weight * 0.45)
#     return weight * 0.45
#
#
# def kg_to_lbs(weight):
#     # w = float(weight * 2.2)
#     return weight /0.45


# Example>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def max_num(numbers):
    max = numbers[0]
    for n in numbers:
        if n > max:
            max = n
    print(max)


def min_num(numbers):
    min = numbers[0]
    for n in numbers:
        if n < min:
            min = n
    print(min)
