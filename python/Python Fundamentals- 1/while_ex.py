

# find sum of digits of a number

# n = 5013 , ans = 5 + 0 + 1 + 3 = 9

sum = 0
n = 5013

while n > 0:
    d = n % 10
    sum += d
    n //= 10


print(sum)



