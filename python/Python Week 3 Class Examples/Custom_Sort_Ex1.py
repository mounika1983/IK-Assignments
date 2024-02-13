

# points = [[1,2], [0,4], [6,3], [1, 3]]

# points.sort(key = lambda x: x[1])

# print(points)



# points = [[1,3], [2,2], [6,3], [1, 2]]

# def sort_by_y_axis(point):
#     return point[1]

# points.sort(key = sort_by_y_axis)

# points = [[6, 3], [2, 2], [1, 3], [2, 4]]


# def select(point):
#     return point[1],point[0]


# points.sort(key=select)
# print("Hi ", points)

# '''
# [1,2] ==> x-coord = 1 , y-coord = 2 




# '''

# print(points)

# def custom_sort(self, string_list):
# 	string_list.sort(key = len()):

#     return string_list

def myFun(e):
    return len(e)
 
points = ["Tesla", "Ford", "BMW", "Honda"]
points.sort(key = myFun)
print(points)