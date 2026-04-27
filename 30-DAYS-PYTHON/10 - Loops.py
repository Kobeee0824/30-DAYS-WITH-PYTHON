# Life is full of routines. In programming we also do lots of repetitive tasks. In order to handle repetitive task programming languages use loops. Python programming language also provides the following types of two loops:
from wsgiref.validate import header_re

""" While Loop - used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the lines of code after the loop will be continued to be executed.

SYNTAX:
while condition:
    code goes here
"""

count = 0
while count < 5:
    print(count)
    count = count + 1
# prints from 0 to 4

# In the above while loop, the condition becomes false when count is 5. That is when the loop stops. If we are interested to run block of code once the condition is no longer true, we can use else.

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# BREAK AND CONTINUE - PART 1
# Break: We use break when we like to get out of or stop the loop

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# CONTINUE: With the continue statement we can skip the current iteration, and continue with the next:
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1
# the above while loop only prints 0, 1, 2, and 4 (skips 3)



# FOR LOOP - similar with other programming languages, but with some syntax differences. For Loop is used of iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items. valid only inside this loop
    print(number) # the numbers will be printed line by line, from 0 to 5

# USING FOR LOOP ON STRING
language = 'Python'
for letter in language:
    print(letter)

for i in range (len(language)):
    print(language[i])

# USING FOR LOOP ON TUPLE
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# FOR LOOP WITH DICTIONARY LOOPING THROUGH A DICTIONARY GIVES YOU THE KEY OF THE DICTIONARY
person = {
    'first_name' : 'Asabeneh',
    'last_name' : 'Yetayeh',
    'age' : 250,
    'country':'Finland',
    'is_married':True,
    'skills':['Javascript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

# USING FOR LOOP IN SET
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

# BREAK AND CONTINUE
# Break - We use break when we want to stop our loop before it is completed.

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        break
# In the above example, the loop stops when it reaches 3
# Continue: We use continue when we want to skip some of the steps in the iteration of the loop

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand
print('outside the loop')

# In the example above, if the number equals 3, the step after the condition (but inside the loop) is skipped and the execution of the loop continues if there are any iterations left

# RANGE FUNCTION - range() function is used to return a list of numbers. The range(start, end, step) takes three parameters: starting, ending and increment. By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end). Creating sequences using range.
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11)) # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0, 11, 2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0, 11, 2))
print(st) # {0, 2, 4, 6, 8, 10}

# for backward from start to end
lst = list(range(11, 0, -2))
print(lst) # [11, 9, 7, 5, 3, 1]



for number in range(11):
    print(number) # prints 0 to 10, not including 11

# NESTED FOR LOOP
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# FOR ELSE - if we want to execute some message when the loop ends, we use else.
for number in range(11):
    print(number) # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

# PASS - in python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors. Also we can use it as a placeholder, for future statements
for number in range(6):
    pass

"""
for x in range(0, 11, 1):
    print(x)

num = 0
while num <= 10:
    print(num)
    num += 1    

for x in range(10, -1, -1):
    print(x)

num = 10
while num >= 0:
    print(num)
    num -= 1

for x in range(1, 8):
    for y in range(x):
        print('#', end='')
    print()


for x in range(8):
    for y in range(8):
        print('x', end=' ')
    print()

    """







