# Accept an input number
# Within the range (1, number), determine the numbers that are divisible by either 3 or 5
# Find the sum of those numbers

def multiples_of_3_and_5(number):
    res = 0
    for num in range(1, number):
        if (num % 3 == 0) or (num % 5 == 0):
            res += num
    return res


print(multiples_of_3_and_5(49)) # 543 

# Accept an input number
# within the range (1, number), determine the numbers within the fibonacci sequence that are even
# Find the sum of the even numbers

def fiboEvenSum(n):
    results = 0
    fib = 1
    prevFib = 1
    
    while fib <= n:
        if fib % 2 == 0:
            results += fib
            
        fib += prevFib
        prevFib = fib - prevFib
        
    return results

fiboEvenSum(1000) # 798
