scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    return score > 75

over_75 = list(filter(is_A_student, scores))

print(over_75)

def less_zero(x):
    return x < 0


number_list = list(range(-5, 5))
# less_than_zero = list(filter(lambda x: x < 0, number_list))
less_than_zero = list(filter(less_zero, number_list))
print(less_than_zero)

