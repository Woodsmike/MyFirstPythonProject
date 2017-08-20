import random
import sys
import os


#numbers strings lists Tuples Dictionaries/Maps

#seven arithmetic operators = (+ - * / % ** //)

#tuple

pi_tuple = (3,1,4,1,5,9)
new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

#len(new_list).min(new_list).max(new_tuple)

#Dictionaries and maps  key=value
super_villains = {'Fiddler': 'Isaac Bowin', 'Captain Cold': 'Leonard Snart', 'Weather Wizard' : 'Mark Mardon',
                  'Mirror Master' : "Sam scudder"}

print(super_villains['Captain Cold'])

del super_villains['Fiddler']

super_villains['Weather Wizard'] = 'Mark Marton'

print(len(super_villains))

print(super_villains.get("Captain Cold"))

print(super_villains.keys())
print(super_villains.values())

#Conditionals
age = 30
if age > 16:
    print('You are old enough to drive')
else:
    print('You are not old enough to drive')

if age >= 21:
    print ('You are old enough to drive a tractor trailer')
elif age >=16:
    print ('You are enough to drive a car')
else:
    print("You are not old enough to drive a car")

#and or not

if(age >= 1) and (age <=18):
    print ('You get a Birthday')
elif (age == 21) or (age >= 56):
    print ('You get a birthday')
elif not(age == 30):
    print ('You do not get a birthday')
else:
    print("You get a birthday party");

#looping
for x in range (0,10):
    print(x, ' ', end="")

print('\n')

grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Hummus', 'Bananas']

for y in grocery_list:
    print (y)

for x in [2,4,6,8,10]:
    print (x)

num_list = [[1,2,3],[10,20,30],[100,200,300]]

for x in range(0,3):
    for y in range (0,3):
        print(num_list[x][y])


#while loop
'''
random_num = random.randrange(0,101)

while random_num !=15:
    print(random_num)
    random_num = random.randrange(0,101)'''

i=0;

while i <= 20:
    if  i % 2 == 0:
        print(i)
    elif i == 9:
        print()
