numbers = (1, 2, 3, 4)

def square(number):
  return number * number

numbersSquare = list(map(lambda x: x*x, numbers))
# result = map(square, numbers)

print(numbersSquare)
