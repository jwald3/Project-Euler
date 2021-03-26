def multiples_of_3_and_5(number):
    res = 0
    for num in range(1, number):
        if (num % 3 == 0) or (num % 5 == 0):
            res += num
    return res


print(multiples_of_3_and_5(10))
