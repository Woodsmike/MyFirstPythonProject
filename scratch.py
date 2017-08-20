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

#strings

long_string = "I'll catch you if you fall - The Floor"

print(long_string[0:4])
print(long_string[-5:])
print(long_string[:-5])
print(long_string[:4] + " be there")
print("%c is my %s letter and my number %d number is %.2f" %
      ('X', 'favorite', 1, 14))

print(long_string.capitalize())
print(long_string.find("Floor"))
print(long_string.isalpha())
print(long_string.isalnum())
print(len(long_string))
print(long_string.strip())
quote_list = long_string.split(" ")
print(quote_list)

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
        break
    else:
        i+=1
        continue

    i+= 1


#functions

def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum

print(addNumber(4,9))

#input from the user

'''print("What is your name?")

name = sys.stdin.readline()

print('Hello', name)'''


#files in file IO(input Output)

'''test_file = open("test.txt", "ab")

print(test_file.mode)

test_file.write(bytes("Write me to a file\n", "UTF-8"))

test_file.close()

test_file = open("test.txt", "r+" )
text_in_file = test_file.read()
print(text_in_file)'''

#os.remove(name of file)

#objects

class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

#Constructor

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound


    def set_name(self, name):
        self.__name = name

    def set_height(self, height):
        self.__height = height

    def set_weight(self, weight):
        self.__weight = weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_name(self):
        return self.__name

    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__weight

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print('Animal')


    def toString(self):
        return"{} is {} cm tall and {} kilograms and says {}".format(self.__name,
                                                                    self.__height,
                                                                    self.__weight,
                                                                    self.__sound)

ape = Animal('Mike', 170 , 10, 'un uh uh')

print(ape.toString())

class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self, owner):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toString(self):
        return"{} is {} cm tall and {} kilograms and says {} and his owner is {}".format(self.get_name(),
                                                                    self.get_height(),
                                                                    self.get_weight(),
                                                                    self.get_sound(),
                                                                    self.__owner)

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)

spot = Dog("Spot", 53, 27, 'ruff ', 'Derek')

print(spot.toString())
print(spot.multiple_sounds( 5 ))

class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(ape)
test_animals.get_type(spot)

