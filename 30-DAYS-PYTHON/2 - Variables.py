import math

# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'Asabeneh',
    'lastname': 'Yetayeh',
    'country': 'Finland',
    'city': 'Helsinki'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', '250', True

print(first_name, last_name, country, age, is_married)
print('First name: ', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

# CHALLENGE

first_name = 'Kobe'
last_name = 'Bryant'
team = 'Lakers'
jerseynum = 24
age = 40

print(type(first_name))
print(type(team))
print(type(jerseynum))
print(type(age))

print(len(first_name))
print(len(last_name))

num_one = 5
num_two = 4

total = num_two - num_one
print(total)

product = num_two * num_one
print(product)

division = num_one / num_two
print(division)

remainder = num_two % num_one
print(remainder)

exp = num_one ** num_two
print(exp)

floor_division = num_one // num_two
print(floor_division)

radius = int(input('Enter radius: '))
area_of_circle = math.pi * radius ** 2
print(area_of_circle)

circum_of_circle = 2 * math.pi * radius
print(circum_of_circle)



