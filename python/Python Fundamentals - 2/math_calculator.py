

pi = 3.14

e = 2.71

person1 = {
  "name": "John",
  "age": 36,
  "country": "US"
}

def find_sqaure(n):
    return n * n

def find_log_base_10(n):
    ans = 0
    while n > 0:
        n = n//10
        ans += 1

    return ans


def find_square_root(n):
    return n**(0.5)