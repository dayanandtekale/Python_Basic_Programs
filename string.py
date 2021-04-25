# defining strings in Python
# all of the following are equivalent
#my_string = 'Hello'
#print(my_string)

#my_string = "Hello"
#print(my_string)

#my_string = '''Hello'''
#print(my_string)

# triple quotes string can extend multiple lines
#my_string = """Hello, welcome to
#           the world of Python"""
#print(my_string)




#Accessing string characters in Python
#str = 'programiz'
#print('str = ', str)

#first character
#print('str[0] = ', str[0])

#last character
#print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
#print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
#print('str[5:-2] = ', str[5:-2])




#If we try to access an index out of the range or use numbers other than an integer, we will get errors.

# index must be in range
#>>> my_string[15]  
#...
#IndexError: string index out of range

# index must be an integer
#>>> my_string[1.5] 
#...
#TypeError: string indices must be integers




# Python String Operations
#str1 = 'Hello'
#str2 ='World!'

# using +
#print('str1 + str2 = ', str1 + str2)

# using *
#print('str1 * 3 =', str1 * 3)





# Iterating through a string
#count = 0
#for letter in 'Hello World':
#    if(letter == 'l'):
#        count += 1
#print(count,'letters found')



#Similarly, len() returns the length (number of characters) of the string.

#str = 'cold'

# enumerate()
#list_enumerate = list(enumerate(str))
#print('list(enumerate(str) = ', list_enumerate)

#character count
#print('len(str) = ', len(str))




#One way to get around this problem is to use triple quotes. Alternatively, we can use escape sequences.
# using triple quotes
#print('''He said, "What's there?"''')

# escaping single quotes
#print('He said, "What\'s there?"')

# escaping double quotes
#print("He said, \"What's there?\"")



#We can use positional arguments or keyword arguments to specify the order.

# Python string format() method

# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)