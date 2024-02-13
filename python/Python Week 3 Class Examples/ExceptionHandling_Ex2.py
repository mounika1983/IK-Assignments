
try:
    import xyz
    print(10)

except:
    print("Error: We couldn't find this module")

print(200)

# Catching Specific Exceptions in Python

try:

    even_numbers = [2, 4, 6, 8]
    print(even_numbers[5])
    x = 5 / 0
    print(x)

except ZeroDivisionError:
    print("Denominator cannot be 0.")

except IndexError:
    print("Index Out of Bound.")

# Output: Index Out of Bound