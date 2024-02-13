# This function uses global variable s

s1 = "abc"
def f():
	s3 = "pqr"
	print(s1)
	print(s2)
	print(s3)

# Global scope
s2 = "xyz"
f()
