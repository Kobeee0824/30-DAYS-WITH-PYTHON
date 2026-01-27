multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
I created 30 days of python.'''
print(multiline_string)

# pwede rin tatlong """ """

first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Asabeneh Yetayeh
# Checking the length of a string using len() built-in function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # TRUE
print(len(full_name)) # 16

print('I hope everyone is enjoying the Python Challenge.\nAre you?')
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('This is a backlash symbol (\\)') # To write a backslash
print('In every proramming language it starts with \"Hello, World!\"') # To write a double quote inside a single quote

a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y

print('------------------')
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

print('------------------')
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

print('------------------')
language = 'Python'
first_three = language[0:3] # starts at zerp index and up to 3 but not include 3
print(first_three)
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

print('------------------')
# REVERSE A STRING
greeting = "Hello, World!"
print(greeting[::-1])

language = 'Python'
pto = language[0:6:2]
print(pto)

print('------------------')
# capitalize(): Converts the first character of the string to capital letter
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'

print('------------------')
# count(count(): returns occurrences of substring in string
# count(substring, start=.., end=..). The start is a starting
# indexing for counting and end is the last index to count.
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1,
print(challenge.count('th')) # 2

print('------------------')
# endswith(): Checks if a string ends with a specified ending
challenge = 'thirty days of python'
print(challenge.endswith('on')) # True
print(challenge.startswith('on')) # False

print('------------------')
# expandtabs(): Replaces tab character with spaces, default tab size is 8.
# It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

print('------------------')
# find(): Returns the index of the first occurence of a substring
# if not found, it returns -1
challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))

print('------------------')
# rfind(): Returns the index of the last occurrence of a substring
# if not found, it returns -1
challenge = 'thirty days of python'
print(challenge.rfind('y'))
print(challenge.rfind('th'))

print('------------------')
# format(): formats string into a nicer output
first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, job, age, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314

print('------------------')
# index(): Returns the lowest index of a substring
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))
# (ERROR) print(challenge.index(sub_string, 9))

print('------------------')
# rindex(): Returns the highest index of a substring
# additional arguments indicate starting and ending index
# (default 0 and string length -1)
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string)) # 7
# (ERROR) print(challenge.rindex(sub_string, 9)) # error
print(challenge.rindex('on', 8)) # 19

print('------------------')
# isalnum(): Checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2026'
print(challenge.isalnum()) # False

print('------------------')
# isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

print('------------------')
# isdecimal(): Checks if all characters in a string are decimal (0-9)
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # True
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed

print('------------------')
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True

print('------------------')
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True

print('------------------')
#isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False


print('------------------')
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

print('------------------')
# islower(): Checks if all alphabet characters in the string are lowercase
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

print('------------------')
# isupper(): Checks if all alphabet characters in the string are uppercase
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True

print('------------------')
# join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result)

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

print('------------------')
# strip(): Removes all given characters starting from the beginning and end of the string
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'

print('------------------')
# replace(): Replaces a substring with a given string
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

print('------------------')
# split(): Splits the string, using given string or space as a separator
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

print('------------------')
# title(): Returns a title cased string
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

print('------------------')
# swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
challenge = 'thirty days of python'
print(challenge.swapcase()) # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase()) # tHIRTY dAYS oF pYTHON

print('------------------')
challenge = 'thirty days of python'
print(challenge.startswith('thirty'))

challenge = '30 days of python'
print(challenge.startswith('thirty'))

print('--------ACTIVITIES----------')

variable = 'Coding For All'

print(variable)
print(len(variable))
print(variable.upper())
print(variable.lower())
print(variable.capitalize())
print(variable.title())
print(variable.swapcase())
print(variable[7:])
print(variable.find('Coding'))
print(variable.replace('Coding', 'Python'))
print(variable.split())
print(variable[0])
print(variable[-1])
print(variable[10])
print(variable[0], variable[7], variable[11])
print(variable.index('C'))
print(variable.index('F'))

print('\n-----------------')
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('b'))
print(sentence.find('because'))
print(variable.startswith('Coding'))
print(variable.endswith('coding'))

print('\n-----------------')
variable3 = '   Coding for All   '
print(variable3.strip())

print('\n-----------------')
print('30DaysOfPython'.isidentifier())
print('ThirtyDaysOfPython'.isidentifier())

print('\n-----------------')
list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(list))

print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\t\tCountry\t\tCity')
print('Asabeneh\t250\t\tFindland\tHelsinki')

radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square')



print('\n-----------------')
variable1 = 'Python for Everyone'
print(variable.replace('Everyone', 'All'))

variable2 = 'Facebook, Google, Microsoft, Apple, IBM, Oracle'
print(variable2.split(", "))


