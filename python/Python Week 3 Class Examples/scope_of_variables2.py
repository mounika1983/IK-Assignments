# https://www.geeksforgeeks.org/python-scope-of-variables/


def fun():
    #print(s)
    global s
    s = "abc"
    print(s)


# Global scope
s = "xyz"
fun()
print(s)
