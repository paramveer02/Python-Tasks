# student = {"name": "John Smith", "grades": [88, 76, 92, 85, 69]}

# # print(student.get("name", ()))
# # print(student["namee"])
# student["subjects".upper()] = (
#     "physics",
#     "chemistry",
#     "maths".title(),
# )  # new key value pair added

# del student["subjects".upper()]  # value delete
# student["grades"] = [55, 80]  # value change
# # print(student.get("subjects".upper()))
# # print(student)
# # print(len(student))


# movie = {
#     "title": "Avengers: Endgame",
#     "directors": ["Anthony Russo", "Joe Russo"],
#     "year": 2019,
# }

# meta_info = {
#     "runtime": 181,
#     "budget": "$356 million",
#     "earnings": "$2.798 billion",
#     "producer": "Kevin Feige",
# }

# # print("titlee" in movie)
# # print("Kevin Feige" in meta_info.values())

# # movie.update(meta_info)
# # movie.update({"test key": "Value Test"})
# # movie.pop("test key")
# # movie.popitem()
# # print(movie)


# vegetables = {"carrot", "lettuce", "broccoli", "onion"}
# mix = {"mango", "apple", "onion", "carrot"}

# vegetables.add("tomatoes")

# # print(vegetables.difference(mix))
# # print(mix.difference(vegetables))
# # print("mangoo" in mix)


# # only mutuals new set
# # new_intersection = vegetables.intersection(mix)

# # only mutuals in the same set
# # vegetables.intersection_update(mix)

# # only non common elements from both sets in new set
# # new_symettric_diff = vegetables.symmetric_difference(mix)

# # only non commonelements from both set in the same set
# # vegetables.symmetric_difference_update(mix)

# # print(new_symettric_diff)
# # print(new_intersection)
# # vegetables.remove("carrot")
# # Adding a new set to an existing set
# # vegetables.update(mix)

# # creating a new set using the other two sets
# # new_list = vegetables.union(mix)
# # vegetables.remove("lemon") # will give a key error whereas
# # vegetables.discard('lemon') # will NOT give a key error but None

# empty_set = set()
# new_set = {"delhi", "berlin", "barcelona"}
# empty_set.update(new_set)
# second_set = empty_set.intersection(new_set)

# # print(second_set)
# # print(empty_set)
# # print(type(empty_set))
# for number in range(1, 9):
#     empty_set.add(number)
# # print(empty_set)

# """
# 1) Define four functions: add, subtract, divide, and multiply.
# Each function should take two arguments, and they should print the result of the arithmetic operation indicated by the function name.

# When orders matters for an operation, the first argument should be treated as the left operand, and the second argument should be treated as the right operand.
# For example, if the user passes in 6 and 2 to subtract, the result should be 4, not -4.

# You should also make sure that the user can’t pass in 0 as the second argument for divide.
# If the user provides 0, you should print a warning instead of calculating their division.
# """


# def add(num1, num2):
#     # return f"Result: {num1 + num2}"
#     print(f"Result: {num1 + num2}")


# # add(num1=10, num2=20)
# # print(add())


# def division(dividend, divisor):
#     if divisor == 0:
#         print("WARNING: Please select a non zero number")
#     print(dividend / divisor)


# # division(divisor=6, dividend=60)


# tv_show = {"title": "Breaking Bad", "seasons": 8, "initial_release": 2008}


# # print_show_info(tv_show)

# series = [
#     {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
#     {"title": "Fargo", "seasons": 4, "initial_release": 2014},
#     {"title": "Firefly", "seasons": 1, "initial_release": 2002},
#     {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
#     {"title": "True Detective", "seasons": 3, "initial_release": 2014},
#     {"title": "Westworld", "seasons": 3, "initial_release": 2016},
# ]


# def print_show_info():
#     for serie in series:
#         print(
#             f'{serie["title"]} ({serie["initial_release"]}) - {serie["seasons"]} seasons'
#         )


# # print_show_info()


# def palindrome(word):
#     word = word.strip().lower()
#     reversed_word = reversed(word)

#     if list(word) == list(reversed_word):
#         print(True)
#     else:
#         print(False)


# # palindrome(word="hannah")

# names = ["Mike", "Fiona", "Patrick"]
# x = 53657


# def addition(a, b):
#     return a + b


# result = addition(5, 15)
# # print(result)


# # addition(5, 7)
# # print(globals())
# # print(locals())
# def greet(name):
#     greeting = f"Hello, {name}!"
#     print(greeting)


# # greet("Phil")
# # print(f"the function returns: {greet('Paramveer')}")


# def process_string(var):
#     return var.lower().strip()


# # print(process_string(var="    SangiTA    "))

# # name = input("Enter Name: ".strip().lower())
# # nationality = input("Enter Nationality: ".strip())
# # age = input("Enter Age: ".strip())


# def movie_info(tup):

#     # keys = ["name", "nationality", "age"]
#     name, nationality, age = info

#     new_dict = {
#         "name": name,
#         "nationality": nationality,
#         "age": age,
#     }

#     # movie_dict = {
#     #     key: val
#     #     for key, val in zip(
#     #         keys,
#     #         tup,
#     #     )
#     # }
#     return new_dict


# info = ("Akshay", "Indian", 55)
# # print(movie_info(info))
# # print(locals())


# def prime(dividend):
#     for divisor in range(2, dividend):
#         if dividend % divisor == 0:
#             return False
#     return True


# # print(prime(11))


# def exponent(base, power):
#     return base**power


# # print(exponent(10, 3))

# # intro = open("introduction.txt", mode="r")
# # print(intro.read())
# # intro.close()

# # context manager closes the file for us,
# # modes available: 'a' to append, 'w' to write and python create file for you if not exist already and 'r' to read!
# # with open("introduction.txt", mode="r") as write_file:
# # write_file.write("\nNow you have two lines! You're growing up so fast!")
# # print(write_file.read())


# # GOAL: Take this set of data from csv file and create a list of dictionaries from it
# # with open("iris.csv", "r") as iris_file:
# #     iris_data = iris_file.readlines()
# # print(iris_file.readlines())
# # print(iris_file.read().split("\n"))

# # irises = []

# # for iris in iris_data[1:]:
# #     sepal_length, sepal_width, petal_length, petal_width, species = iris.strip(
# #         "\n"
# #     ).split(",")

# #     headers = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
# #     data = [sepal_length, sepal_length, petal_length, petal_width, species]
# #     irises.append({key: val for key, val in zip(headers, data)})
# # # print(irises)

# # for iris in irises:
# #     v = ",".join(iris.values())
# #     # print(v)
# #     # sepal_length, sepal_width, petal_length, petal_width, species = iris.values()
# #     # print(f"{sepal_length},{sepal_width}, {petal_length}, {petal_width}")
# # with open("iris_2.csv", mode="w") as f:
# #     for iris in irises:
# #         f.write(",".join(iris.values()) + "\n")

# # Goal in this section is going to be to take this set of CSV data, and create a list of dictionaries from it.


# with open("iris.csv") as iris_file:
#     iris_data = iris_file.readlines()

# headers = iris_data[0].strip().split(",")
# iris_list = []


# for iris in iris_data[1:]:
#     data = iris.strip().split(",")

#     # columns = ("sepal_length", "sepal_width", "petal_length", "petal_width", "species")
#     # values = [sepal_length, sepal_width, petal_length, petal_width, species]
#     # iris_dict = {key: val for key, val in zip(headers, values)}

#     # or

#     iris_dict = dict(zip(headers, data))
#     iris_list.append(iris_dict)
# # if len(iris_list) == 15:
# #     print(True)
# # print(iris_list)
# # print(len(iris_list))

# # iriss = [
# #     ("sepal_length", 5.1),
# #     ("sepal_width", "3.5"),
# #     ("petal_length", "1.4"),
# #     ("petal_width", "0.2"),
# #     ("species", "Iris-setosa"),
# # ]
# # v = dict(iriss)
# # print(v)

# # Take the list of dictionaries we created from the Iris flower data set and write it to a new file in CSV format.
# # with open("iris_2.csv", "w") as iris_file2:
# #     for data in iris_list:
# #         iris_file2.write(",".join(data.values()) + "\n")
# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
# from math import pi

# """
# # Task 1: Write a function in Python that accepts one numeric parameter. This parameter will be the measure of an angle in radians.
# The function should convert the radians into degrees and then return that value.
# """


# def radian_to_degree_converter(angle):

#     return f"Angle in Degrees is: {angle * (180 / pi)}"


# print(radian_to_degree_converter(2))

# """
# # Task 2: Create a function in Python that accepts two parameters. The first will be a list of numbers.
# The second parameter will be a string that can be one of the following values: asc, desc, and none.

# If the second parameter is "asc," then the function should return a list with the numbers in ascending order.
# If it's "desc," then the list should be in descending order, and if it's "none," it should return the original list unaltered.
# """


# def list_sorter(num, st):

#     if st == "asc":
#         return sorted(num)

#     elif st == "desc":
#         return sorted(num, reverse=True)

#     return num


# # num_list = [10, 50, 20, 30, 60]

# print(list_sorter([10, 50, 20, 30, 60], "desc"))


# """
# # Task 3: Create a function in Python that accepts a single word and returns the number of vowels in that word.
# In this function, only a, e, i, o, and u will be counted as vowels — not y.
# """

# vowels = ["a", "e", "i", "o", "u"]

# new_list = []


# def vowels_finder(word):

#     # for x in word:
#     #     if x in vowels:
#     #         new_list.append(x)
#     # or
#     new_list = [x for x in word if x in vowels]
#     return f"New List but with dublicates: {new_list}"


# print(vowels_finder(word="Paramveer Singh Marwah"))

# # Remove dublicate items from the new list by converting it into a set and then back to list
# to_set = set(new_list)
# to_list = list(to_set)
# print("List without dublicates using set but unordered", to_list)

# # OR

# to_dict = dict.fromkeys(new_list)
# to_unique_list = list(to_dict)
# print("List without dublicates using dict but ordered", to_unique_list)

# """
# # Task 4: Write a function in Python that accepts a credit card number.
# It should return a string where all the characters are hidden with an asterisk except the last four.
# For example, if the function gets sent "4444444444444444", then it should return "4444".
# """
# creditNum = input("Enter your Credit Card Number: ")


# def card_crypting():

#     return creditNum[-4:].rjust(len(creditNum), "*")


# print(card_crypting())


# """
# # Task 5: Create a Python function that accepts a string. This function should count the number of Xs and the number of Os in the string.
# It should then return a boolean value of either True or False.

# If the count of Xs and Os are equal, then the function should return True.
# If the count isn't the same, it should return False.
# If there are no Xs or Os in the string, it should also return True because 0 equals 0. The string can contain any type and number of characters.
# """


# def alphabet_explorer(var):

#     x_count = var.count("x")
#     print("Number of x: ", x_count)
#     o_count = var.count("o")
#     print("Number of o: ", o_count)

#     if x_count == o_count:
#         return True
#     elif x_count != o_count:
#         return False


# print(alphabet_explorer(var="xinJianong"))

# """
# # Task 6: Write a Python function that accepts three parameters. The first parameter is an integer.
# The second is one of the following mathematical operators: +, -, /, or . The third parameter will also be an integer.

# The function should perform a calculation and return the results. For example, if the function is passed 6 and 4, it should return 24.
# """


# def calculator(int1, operator, int2):

#     if operator == "+":
#         return f"operator = +, Result:{int1 + int2}"
#     elif operator == "-" and int1 >= int2:
#         return f"operator = -, Result:{int1 - int2}"
#     elif operator == "*":
#         return f"operator = *, Result:{int1 * int2}"
#     print("Operator not recognized")


# print(calculator(5, "/", 2))


# """
# # Task 7: Create a function in Python that accepts two parameters.
# The first should be the full price of an item as an integer.
# The second should be the discount percentage as an integer.

# The function should return the price of the item after the discount has been applied.
# For example, if the price is 100 and the discount is 20, the function should return 80.
# """
# cost = int(input("Enter Cost: "))
# discount = int(input("How much discount you want? "))


# def marketSale():

#     amount_save = cost * (discount / 100)
#     discount_price = cost - amount_save
#     return f"Price after Discount: {discount_price}"


# print(marketSale())

# """
# Task 8: Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings.
# The function should return a list with only the integers in the original list in the descending order.
# """


# def int_list(l):

#     newlist = [x for x in l if isinstance(x, int)]
#     # or
#     # for x in l:
#     #     if isinstance(x, int):
#     #         newlist.append(x)
#     return sorted(newlist, reverse=True)


# print(int_list([1, 3, "Param", 6, 2]))

# """
# # Task 9: Create a Python function that accepts a string.
# The function should return a string, with each character in the original string doubled.
# If you send the function "now" as a parameter, it should return "nnooww," and if you send "123a!", it should return "112233aa!!".
# """


# def str_double(var):

#     obj = str()

#     for char in var:
#         obj = obj + char + char
#     return obj


# print(str_double("abc"))

# fruits = ("apple", "banana", "cherry", "tarbooj")

# (green, yellow, *red) = fruits
# print(green)

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     "car_number": 12.34,
# }

# int_dict = {
#     key: value
#     for key, value in thisdict.items()
#     if type(value) == str or type(value) == float
# }

# print(int_dict)

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
# import random

# """
# # Task 10: Write a function named capital_indexes. The function takes a single parameter, which is a string.
# Your function should return a list of all the indexes in the string that have capital letters.

# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
# """


# def func(var):

#     l = [x[0] for x in enumerate(var) if x[1].isupper()]
#     return l


# print(func("pAramvEEr"))

# """
# # Task 11: a) Ask the user to enter their given name and surname in response to a single prompt.
# # Use split to extract the names, and then assign each name to a different variable.
# # For this exercise, you can assume that the user has a single given name and a single surname.

# #11 b) Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method.
# """

# # a)
# name = input("Please give in your first and last name, comma seperated: ")


# def func():

#     name_list = name.split("; ")
#     first_name, last_name = name_list
#     print(f"First Name: {first_name}, Last Name: {last_name}")


# func()
# print(func())

# # b)

# l = [1, 2, 3, 4, 5]


# def format_converter(l):

#     str_list = [str(x) for x in l]
#     return " - ".join(str_list)


# print(format_converter(l=[1, 2, 3, 4, 5]))

# """
# # Task 12: Each quote is a string, but each string actually contains quote characters at the start and end.
# Extract the text from each string, without these extra quote marks, and print each quote in a new list.
# """

# quotes = [
#     "'What a waste my life would be without all the beautiful mistakes I've made.'",
#     "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
#     "'The very essence of romance is uncertainty.'",
#     "'We are not here to do what has already been done.'",
# ]


# def quote_extractor():

#     quotes_extracted = [quote[1][1:-1].strip() for quote in enumerate(quotes)]
#     # for x in enumerate(quotes):
#     #     new_l.append(x[1][1:-1])
#     print(f"Quotes: {quotes_extracted}")


# quote_extractor()


# """
# # Task 13: Ask the user to enter a word, and then print out the length of the word.
# You should account for any excess whitespace in the users input, so you are going to have to process the string before you find its length.

# If you want to take this a little bit further, you an ask the user for a long piece of text.
# You can then tell them how many how many characters are in the text overall, and you can also provide them a word count.
# """


# def word_clean(word):

#     word = word.strip()
#     return len(word)


# print(word_clean("      paramveer"))

# text = input("Please write a random sentence: ")


# def word_count():

#     print(f"Character Count: {len(text)}, Word Count: {len(text.split())}")


# word_count()

# """
# # Task 14: For this project, your program should do the following:

# a) Calculate the average budget of all movies in the data set.
# b) Print out every movie that has a budget higher than the average you calculated.
#    You should also print out how much higher than the average the movie's budget was.
# c) Print out how many movies spent more than the average you calculated.

# Additional Task: For the extra part of this assignment, we're going to:

# Ask the user how many movies they want to add to the list.
# Use range and a for loop to perform some option the specified number of times.
# Ask the user for a movie name and budget during each iteration of the loop, and append a tuple to the movies list containing this information.

# """

# movies = [
#     ("Eternal Sunshine of the Spotless Mind", 20000000),
#     ("Memento", 9000000),
#     ("Requiem for a Dream", 4500000),
#     ("Pirates of the Caribbean: On Stranger Tides", 379000000),
#     ("Avengers: Age of Ultron", 365000000),
#     ("Avengers: Endgame", 356000000),
#     ("Incredibles 2", 200000000),
# ]

# # a)

# movie_count = int(input("How many movie you want to add: ".title()))


# def average_budget():

#     for _ in range(movie_count):
#         movie_name = input("Enter the Movie Name: ")
#         movie_budget = int(input("Enter the Movie Budget: "))
#         new_movie = (movie_name, movie_budget)
#         movies.append(new_movie)

#     print(f"movies: {movies}")

#     budget_list = [budget[1] for budget in movies]
#     total_budget = sum(budget_list)

#     # or
#     # for budget in movies:
#     #     budget_list.append(budget[1])
#     #     total_budget = sum(budget_list)

#     avg_budget = total_budget / len(movies)
#     return avg_budget

#     # return f"Average Budget: {total_budget / len(movies)}"


# # b) and c)
# def above_average_budget():

#     avg_budget = average_budget()
#     above_average_budget_list = [movie[0] for movie in movies if movie[1] > avg_budget]

#     for movie in movies:
#         if movie[0] in above_average_budget_list:
#             print(
#                 f"Budget of {movie[0]} is above average by an Amount: {movie[1] - avg_budget}: "
#             )

#     return "List of movies with an above average budget -> {}".title().format(
#         above_average_budget_list
#     )


# print(above_average_budget())


# """
# # Task 15: Fizzbuzz challenge:

# One player starts by saying the number 1.
# Each player then takes it in turns to say the next number, counting one at a time.
# If the number is divisible by 3, instead of saying the number, the player should say, "Fizz".
# If the number is divisible by 5, instead of saying the number, the player should say, "Buzz".
# If the number is divisible by 3and5, instead of saying the number, the player should say, "Fizz Buzz".
# If you make a mistake, you're usually eliminated from the game, and the game continues until there's only a single player remaining.
# """


# def fizzBuzz():

#     l = []
#     for number in range(101):
#         if number % 3 == 0:
#             l.append("Fizz")
#             # print("Fizz")
#         elif number % 5 == 0:
#             # print("Buzz")
#             l.append("Buzz")
#         elif (number % 3 == 0) and (number % 5 == 0):
#             # print("Fizz Buzz")
#             l.append("Fizz Buzz")
#         else:
#             l.append(number)
#     return l


# print(fizzBuzz())


# """
# # Task 16:
# a) Write a short guessing game program using a while loop. The user should be prompted to guess a number between 1 and 100,
# and you should tell them whether their guess was too high or too low after each guess.
# The loop should keeping running until the user guesses the number correctly.

# b) Use a loop and the continue keyword to print out every character in the string "Python", except the "o".
# Remember that strings are collections, and they are iterable, so you can iterate over the string, which will yield one character at a time.

# c) TODO: Using one of the examples from earlier—or a solution entirely of your own—create a program that prints out every prime number between 1 and 100.
# """


# # a)

# target_number = random.randint(10, 15)


# def guessGame():

#     guess = int(input("Guess a number between 1 and 100: "))
#     while guess != target_number:
#         if guess > target_number:
#             print(f"{guess} is too High!")
#         elif guess < target_number:
#             print(f"{guess} is too low!")
#         guess = int(input("try again: ".title()))
#     print(f"Good Job! {guess} is correct")


# guessGame()

# # b)


# def characterTracker(var):

#     for char in var:
#         if char != "o":
#             print(char)
#             continue


# # or

# # for char in var:
# #     if char == "o":
# #         continue
# #     print(char)


# characterTracker(var="Python")

# """
# Task 17: To determine whether a given card number is valid or not using Luhn Algorithm.
# This algorithm is actually used in real-life applications to test credit or debit card numbers as well as SIM card serial numbers.

# Purpose of the Task: The purpose of the algorithm is to identify potentially mistyped numbers,
# because it can determine whether or not it's possible for a given number to be the number for a valid card.

# What the Luhn Algorithm states:
# 1. Remove the rightmost digit from the card number. This number is called the checking digit, and it will be excluded from most of our calculations.
# 2. Reverse the order of the remaining digits.
# 3. For this sequence of reversed digits, take the digits at each of the even indices (0, 2, 4, 6, etc.) and double them. If any of the results are greater than 9,
# subtract 9 from those numbers.
# 4. Add together all of the results and add the checking digit.
# 5. If the result is divisible by 10, the number is a valid card number. If it's not, the card number is not valid.

# """
# cardNum = list(input("Please enter your card number: ".strip()))

# processedDigits = []


# def credit_card_validator():

#     checkDigit = cardNum.pop()
#     cardNum.reverse()
#     print(cardNum)
#     for index, digit in enumerate(cardNum):
#         if index % 2 == 0:
#             doubleDigit = int(digit) * 2

#             if doubleDigit > 9:
#                 doubleDigit = doubleDigit - 9
#             processedDigits.append(doubleDigit)
#         else:
#             processedDigits.append(int(digit))

#     total = int(checkDigit) + sum(processedDigits)
#     if total % 10 == 0:
#         return f"valid card number".title()
#     return f"invalid card number".title()


# print(credit_card_validator())

# """
# Task 18: a) Inside the tuple we have the album name, the artist (in this case, the band),
# the year of release, and then another tuple containing the track list.

# Convert this outer tuple to a dictionary with four keys.

# b) Iterate over the keys and values of the dictionary you create in exercise 1.
# For each key and value, you should print the name of the key, and then the value alongside it.

# c) Delete the track list and year of release from the dictionary you created.
# Once you've done this, add a new key to the dictionary to store the date of release.
# The date of release for The Dark Side of the Moon was March 1st, 1973.

# d) Try to retrieve one of the values you deleted from the dictionary.
# This should give you a KeyError. Once you've tried this, repeat the step using the get method to prevent the exception being raised.
# """

# album = (
#     "The Dark Side of the Moon",
#     "Pink Floyd",
#     1973,
#     (
#         "Speak to Me",
#         "Breathe",
#         "On the Run",
#         "Time",
#         "The Great Gig in the Sky",
#         "Money",
#         "Us and Them",
#         "Any Colour You Like",
#         "Brain Damage",
#         "Eclipse",
#     ),
# )

# # create a list with a collection of required keys
# l = ["Album", "Band", "Year", "Tracks"]

# album_dict = {key: value for key, value in zip(l, album)}
# print(album_dict["Tracks"])


# for key, val in album_dict.items():
#     print(f"Key: {key}, Value: {val}")

# del album_dict["Tracks"]
# print(album_dict.get("Tracks"))
# # print(album_dict["Tracks"])
# album_dict["date of release".title()] = "March 1st, 1973"
# print(album_dict)


# """
# Task 19: For this project the application needs to have the following functionality:

# a) Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
# b) The program should store information about all of these books in a Python list.
# c) Users should be able to display all the books in their reading list, and these books should be printed out in a user-friendly format.
# d) Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program.

# """

# reading_list = []
# menu_prompt = """Please enter one of the following options:

# - 'a' to add a book
# - 'l' to list the books
# - 'q' to quit

# What would you like to do? """
# selected_option = input(menu_prompt)


# def add_book():
#     title = input("please enter the title: ".strip().title())
#     author = input("please enter the author: ".strip().title())
#     year = input("please enter the year of publication: ".strip().title())

#     book_keys = ["title", "author", "year"]
#     book_values = (title, author, year)

#     reading_list.append(
#         {
#             key: val
#             for key, val in zip(
#                 book_keys,
#                 book_values,
#             )
#         }
#     )
#     print(reading_list)


# def show_books():
#     for book in reading_list:
#         print(f"{book['title']}, by {book['author']} ({book['year']})")


# while selected_option != "q":
#     if selected_option == "a":
#         add_book()

#     elif selected_option == "l":
#         if reading_list:
#             show_books()
#         else:
#             print("yout reading list is empty".title())

#     else:
#         print("Invalid option selected")

#     selected_option = input(menu_prompt).strip().lower()

# """
# Task 20:
# For this project the application needs to have the following functionality:

# 1. Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
# 2. The program should store information about all of these books in a file called books.csv, and this data should be stored in CSV format.
# 3. Users should be able to retrieve the books in their reading list, and these books should be printed out in a user-friendly format.
# 4. Users should be able to search for a specific book by providing a book title.
# 5. Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program.
# """


# def add_book():
#     title = input("Enter the book title: ".strip().title())
#     author = input("Enter the book author: ".strip().title())
#     year = input("Enter the year of publication: ".strip().title())

#     with open("books.csv", "a") as book_file:
#         book_file.write(f"{title},{author},{year}\n")


# def get_all_books():
#     books = []
#     with open("books.csv", "r") as get_book:
#         book_data = get_book.readlines()
#         for row in book_data:
#             values = row.strip().split(",")
#             headers = ("title", "author", "year")
#             books_dict = dict(
#                 zip(headers, values)
#             )  # or implement dictionary comprehension
#             # books_dict = {key: val for key, val in zip(headers, values)}
#             books.append(books_dict)
#         return books


# def show_all_books(books):
#     print()  # generate an empty line
#     for book in books:
#         print(f"-> {book['title']}, by {book['author']}, published in {book['year']}")
#         print()


# def search_books():
#     all_books_list = get_all_books()
#     matched_books = []
#     search_term = input("Enter Book title you want to search: ".title()).strip().lower()
#     for book in all_books_list:
#         if search_term in book["title"].lower():
#             matched_books.append(book)
#     return matched_books


# menu_prompt = """ Please select one of the following options:

# - 'a' to add a book
# - 'l' to list the book
# - 's' to search the book
# - 'q' to quit

# Please Select an Option:
# """

# selected_option = input(menu_prompt)


# while selected_option != "q":
#     if selected_option == "a":
#         add_book()

#     elif selected_option == "l":
#         list_of_books = get_all_books()
#         if list_of_books:
#             show_all_books(list_of_books)
#         else:
#             print("the reading list is empty".title())

#     elif selected_option == "s":
#         filtered_books = search_books()
#         if filtered_books:
#             show_all_books(filtered_books)
#         else:
#             print("Sorry, could not find the book")

#     else:
#         print(f"{selected_option} is an invalid option, try again!")

#     selected_option = input(menu_prompt)

# Task 20:
# For this project the application needs to have the following functionality:

# 1. Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
# 2. The program should store information about all of these books in a file called books.csv, and this data should be stored in CSV format.
# 3. Users should be able to retrieve the books in their reading list, and these books should be printed out in a user-friendly format.
# 4. Users should be able to search for a specific book by providing a book title.
# 5. Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program.
# """


import enum
from audioop import avg
from itertools import count

from idna import valid_contextj


def add_book():
    title = input("enter book title: ".title())
    author = input("enter book author: ".title())
    year = input("enter book publication year: ".title())

    with open("books.csv", "a") as write_csv:
        write_csv.write(f"{title},{author},{year}\n")


def get_all_books():
    books_list = []
    with open("books.csv", mode="r") as read_csv:
        csv_data = read_csv.readlines()
        headers = ("title", "author", "year")
        for row in csv_data:
            values = row.strip("\n").split(",")
        books_dict = dict(zip(headers, values))
        books_list.append(books_dict)
    return books_list


def show_books(books):
    for book in books:
        print(f"-> {book['title']}, by {book['author']}, published in {book['year']}")


def search_books():
    list_of_books = get_all_books()
    filtered_books = []
    search_term = input("enter the book title to search: ".title()).strip().lower()

    for book in list_of_books:
        if search_term in book["title"].lower():
            filtered_books.append(book)
    return filtered_books


menu_prompt = """
Please select one of the following options:
- "a" to add books
- "l" to list books
- "s" to search for books
- "q" to quit

What do you want to do?
"""

# selected_option = input(menu_prompt).strip().lower()

# while selected_option != "q":

#     if selected_option == "a":
#         add_book()

#     elif selected_option == "l":
#         all_books = get_all_books()

#         if all_books:
#             show_books(all_books)
#         else:
#             print("Sorry, there are no books in the list")

#     elif selected_option == "s":
#         matched_books = search_books()

#         if matched_books:
#             show_books(matched_books)
#         else:
#             print("Sorry, this books are not available")

#     else:
#         print(f"{selected_option} is invalid, select again")

#     selected_option = input(menu_prompt).strip().lower()

# names = ["mary", "Richard", "Noah", "KATE"]
# names = [name.title() for name in names]
# print(names)

names = ("mary", "Richard", "Noah", "KATE")
ages = (36, 21, 40, 28)

people_set = {(name.title(), age) for name, age in zip(names, ages)}
# print(people_set)
# for name, age in zip(names, ages):
#     person_data = (name.title(), age)
#     people.append(person_data)
# or
student_ids = (112343, 134555, 113826, 124888)
names = ("mary", "Richard", "Noah", "KATE")

students = {key: val.upper() for key, val in zip(student_ids, names)}
# print(students)

# for student_id, name in zip(student_ids, names):
#     student = {student_id: name.title()}
#     students.update(student)
movie = {
    "title": "thor: ragnarok",
    "director": "taika waititi",
    "producer": "kevin feige",
    "production_company": "marvel studios",
}

movies = {key: val.title() for key, val in movie.items()}
# print(movies)

numbers = [56, 3, 45, 29, 102, 30, 73]
# print(min(numbers))


def get_name(student):
    return student["grade_average"]


students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92},
]

# students.sort(key=get_name)
# print(students)
# or
students.sort(key=lambda student: student["name"])
# print(students)

"""
Write a function named mid that takes a string as its parameter. 
Your function should extract and return the middle letter. 
If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
"""


def mid(string):
    if len(string) % 2 == 0:
        return ""
    return string[len(string) // 2]


print(33 / 2)
print(33 // 2)  # integer divison
