# compare the size
import sys

my_list = [0, 1, 2, 5, 10]
my_tuple = (0, 1, 2, 5, 10)

print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")