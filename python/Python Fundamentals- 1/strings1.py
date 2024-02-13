# # https://www.programiz.com/python-programming/methods/string
# # https://www.programiz.com/python-programming/methods/string/split 

# text = 'bat ball'

# print(len(text))

# # replace 'ba' with 'ro'
# replaced_text = text.replace('ba', 'ro')
# print(replaced_text)

# song = 'Let it be, let it be, let it be, let it be'

# # replacing only two occurrences of 'let'
# print(song.replace('let', "don't let", 2))

# message = 'python is popular programming language'

# # number of occurrence of 'p'
# print('Number of occurrence of p:', message.count('p'))

# # Output: Number of occurrence of p: 4

# quote = 'Let it be, let it be, let it be'

# # first occurance of 'let it'(case sensitive)
# result = quote.find('let it')
# print("Substring 'let it':", result)

# # find returns -1 if substring not found
# result = quote.find('small')
# print("Substring 'small ':", result)

# # How to use find()
# if (quote.find('be,') != -1):
#     print("Contains substring 'be,'")
# else:
#     print("Doesn't contain substring")



# quote = 'Do small things with great love'

# # Substring is searched in 'hings with great love'
# print(quote.find('small things', 10))

# # Substring is searched in ' small things with great love'
# print(quote.find('small things', 2))

# # Substring is searched in 'hings with great lov'
# print(quote.find('o small ', 10, -1))

# # Substring is searched in 'll things with'
# print(quote.find('things ', 6, 20))

class demo(dict):
	def __test__(self,key):
		return []
	a = demo()
	a['test'] = 7
	print(a)