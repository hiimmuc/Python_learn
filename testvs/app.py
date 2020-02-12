import re
from collections import OrderedDict
from question import Point
from question import Chef
from question import Student
from question import Vietnamese_chef
import math
from random import randint
from package import some_external_function
from question import Question
import turtle

# '''
# student_count = 1000
# rating = 4.99
# is_published = True
# course_name = "python programming"
# message = \'''hi
# im'm nam
# \'''
# return = "\"something here\""
# full = f"{course_name} {return}"
# print(course_name.capitalize())
# print(course_name.upper())
# print(course_name.title())
# print("pro" in course_name)
# print(course_name.replace("python", "java"))
# print(course_name.strip())
# math.ceil()
# '''
# x = int(input("x: "))
# y = int(x) + 1
# print(f"x: {x} , y: {y}")
# if y > x and x != 0:
#     print("y is greater than x")
#     print("x is different from zero")
# elif x == 0:
#     print("x equal zero")
# print(y + x)

# #excercise
# count = 0
# for number in range(0, 10, 2):
#     if number != 0:
#         print(number)
#         count += 1
# print(f"there are {count} even numbers")

# create function

# *arg -> tuples
# **arg -> dictionary
# do not define a global variable inisde the function
# convert to commment use crtl + / or crtl + K + C


# def multiply(*numbers):
#     result = 1
#     for number in numbers:
#         result *= number
#     return result


# def save_user(**user):
#     print(user['age'])


# #save_user(id=1, name="john", age=22)
# print("start")
# print(multiply(1, 2, 3))

# excercise 2

# def fizz_buzz(number):
#     if (number % 5 == 0) and (number % 3 == 0):
#         return "Fizz Buzz"
#     if number % 3 == 0:
#         return "Fizz"
#     if number % 5 == 0:
#         return "Buzz"
#     return f"{number}"


# print(fizz_buzz(int(input("Enter number: "))))

# matrix input output

# row = int(input("Enter the number of rows: "))
# col = int(input("Enter the number of cols: "))
# some_external_function.print_mat(
#     some_external_function.input_mat(row, col), row, col)

# [] for list () for tuple {} for dictionary

# list, tuple, dictionary
friends_name = ["Someone", "Kevin", "Karen"]
coordinates_ = [(1, 2, 3), (4, 5, 6), (5, 6, 7)]
fruits_store = {"banana": 4000, "apple": 5000,
                "grape": 10000, "pineapple": 15000}

# #1
# print(dot_product(vector1=input_vector(), vector2=input_vector()))
# #2
# price = fruits_store.get(input("enter fruit's name you want to buy: "))
# if price:
#     print(f"The price of it is {price}VND")
# else:
#     print("No kind of that fruit in this store")
question_prompts = [
    "x equals:\n(a) 1\n(b) 2\n(c) 3",
    "y equals:\n(a) 1\n(b) 2\n(c) 3",
    "z equals:\n(a) 1\n(b) 2\n(c) 3",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]


def run_test():
    Q = questions[randint(0, 2)]
    print(Q.promts)
    ans = input("enter answer: ")
    if ans == Q.answer:
        print("you're right")
    else:
        print("wrong answer")


student1 = Student("Nam", "EEE8", 3.1)
student2 = Student("Trung", "EEE8", 3.5)


# mychef = Chef()
# mychef.make_chicken()

# myVNchef = Vietnamese_chef()
# myVNchef.make_salad()

# exercise
# find maximum number in list
# remove the duplicate number in list


# size = randint(1, 10)
# print(size)
# random_list = [randint(0, 100) for index in range(size)]
# print(random_list)
# print(f"maximum number in the list is {max_number(random_list)}")
# print(
#     f"the list after remove duplicators is:\n{removing_duplicators(random_list)}")


# for fun
# nam_turtle = turtle.Turtle()
# nam_turtle.speed(1)


# while True:
#     square_r()
#     nam_turtle.forward(100)


sentence = 'da daad adsad '  # input("Enter the sentence: ")
# 1
words_ = list(set(sentence.split(' ')))
words_list = [['', 0] for index in range(len(words_))]
for index in range(len(words_)):
    words_list[index][0] = words_[index]
    for word in sentence.split(' '):
        if word == words_[index]:
            words_list[index][1] += 1

words_count = {}
words_count.update(words_list)
print(words_count)
# 2
words_dict = dict()
for word in words_:
    words_dict[word] = 0
    for other_word in sentence.split(' '):
        if word == other_word:
            words_dict[word] += 1
print(words_dict)
