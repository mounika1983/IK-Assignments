
def greet():
    print("Hello")

def greet_someone(name: str):
    print("Hello "+ name)

greet()
greet_someone("Vandana")


def find_sum_of_digits(n: int ):
    sum = 0
    while n > 0:
        d = n % 10
        sum += d
        n //= 10

    return sum


n = 5013
print(find_sum_of_digits(n))
print(find_sum_of_digits(49213))
print(find_sum_of_digits(20473))


def fun(a):
    a = a + 10
    print("Inside fun: ", a) # 30

a = 20
print(a) # 20
fun(a)
print(a) # 20