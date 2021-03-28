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


# return the largest prime number factor of a number
def prime_factors(n):
    prime = 2
    
    # Print the number of two's that divide n
    if n % 2 == 0:
        prime = 2
          
    # prime numbers not divisible by 2 begin at 3 and factors end at the last square root (n ** 1/2) that goes into the number.
    # counting numbers divisble by 2 is pointless, so the skip will be 2
    for i in range(3,int(n * (1/2))+1,2):
          
        # while n is divisible by numbers in the range, reset n and prime to the index
        while n % i== 0:
            n = n / i
            prime = i
            
              
    # if n is greater than 2 and not even, assign it to prime
    if (n > 2) & (n % 2 != 0):
        prime = n
    
    return prime

prime_factors(13195) # 29
