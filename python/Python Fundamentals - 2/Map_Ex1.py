numbers = [2, 4, 8, 6, 8, 10]

def square(number):
  return number * number


squared_numbers = list(map(square, numbers))

# squared_numbers = set(map(square, numbers))

print(squared_numbers)



numbers = [1, 2, 3, 4]
result = map(square, numbers)
print(result)

numbersSquare = set(result)
print(numbersSquare)
