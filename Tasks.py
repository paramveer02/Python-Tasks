import random
from math import pi

"""
# Task 1: Write a function in Python that accepts one numeric parameter. This parameter will be the measure of an angle in radians. 
The function should convert the radians into degrees and then return that value.
"""


def radian_to_degree_converter(angle):

    return f"Angle in Degrees is: {angle * (180 / pi)}"


print(radian_to_degree_converter(2))

"""
# Task 2: Create a function in Python that accepts two parameters. The first will be a list of numbers. 
The second parameter will be a string that can be one of the following values: asc, desc, and none.

If the second parameter is "asc," then the function should return a list with the numbers in ascending order. 
If it's "desc," then the list should be in descending order, and if it's "none," it should return the original list unaltered.
"""


def list_sorter(num, st):

    if st == "asc":
        return sorted(num)

    elif st == "desc":
        return sorted(num, reverse=True)

    return num


# num_list = [10, 50, 20, 30, 60]

print(list_sorter([10, 50, 20, 30, 60], "desc"))


"""
# Task 3: Create a function in Python that accepts a single word and returns the number of vowels in that word. 
In this function, only a, e, i, o, and u will be counted as vowels — not y.
"""

vowels = ["a", "e", "i", "o", "u"]

new_list = []


def vowels_finder(word):

    # for x in word:
    #     if x in vowels:
    #         new_list.append(x)
    # or
    new_list = [x for x in word if x in vowels]
    return f"New List but with dublicates: {new_list}"


print(vowels_finder(word="Paramveer Singh Marwah"))

# Remove dublicate items from the new list by converting it into a set and then back to list
to_set = set(new_list)
to_list = list(to_set)
print("List without dublicates using set but unordered", to_list)

# OR

to_dict = dict.fromkeys(new_list)
to_unique_list = list(to_dict)
print("List without dublicates using dict but ordered", to_unique_list)

"""
# Task 4: Write a function in Python that accepts a credit card number. 
It should return a string where all the characters are hidden with an asterisk except the last four. 
For example, if the function gets sent "4444444444444444", then it should return "4444".
"""
creditNum = input("Enter your Credit Card Number: ")


def card_crypting():

    return creditNum[-4:].rjust(len(creditNum), "*")


print(card_crypting())


"""
# Task 5: Create a Python function that accepts a string. This function should count the number of Xs and the number of Os in the string. 
It should then return a boolean value of either True or False.

If the count of Xs and Os are equal, then the function should return True. 
If the count isn't the same, it should return False. 
If there are no Xs or Os in the string, it should also return True because 0 equals 0. The string can contain any type and number of characters.
"""


def alphabet_explorer(var):

    x_count = var.count("x")
    print("Number of x: ", x_count)
    o_count = var.count("o")
    print("Number of o: ", o_count)

    if x_count == o_count:
        return True
    elif x_count != o_count:
        return False


print(alphabet_explorer(var="xinJianong"))

"""
# Task 6: Write a Python function that accepts three parameters. The first parameter is an integer. 
The second is one of the following mathematical operators: +, -, /, or . The third parameter will also be an integer.

The function should perform a calculation and return the results. For example, if the function is passed 6 and 4, it should return 24.
"""


def calculator(int1, operator, int2):

    if operator == "+":
        return f"operator = +, Result:{int1 + int2}"
    elif operator == "-" and int1 >= int2:
        return f"operator = -, Result:{int1 - int2}"
    elif operator == "*":
        return f"operator = *, Result:{int1 * int2}"
    print("Operator not recognized")


print(calculator(5, "/", 2))


"""
# Task 7: Create a function in Python that accepts two parameters. 
The first should be the full price of an item as an integer. 
The second should be the discount percentage as an integer.

The function should return the price of the item after the discount has been applied. 
For example, if the price is 100 and the discount is 20, the function should return 80.
"""
cost = int(input("Enter Cost: "))
discount = int(input("How much discount you want? "))


def marketSale():

    amount_save = cost * (discount / 100)
    discount_price = cost - amount_save
    return f"Price after Discount: {discount_price}"


print(marketSale())

"""
Task 8: Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings. 
The function should return a list with only the integers in the original list in the descending order.
"""


def int_list(l):

    newlist = [x for x in l if isinstance(x, int)]
    # or
    # for x in l:
    #     if isinstance(x, int):
    #         newlist.append(x)
    return sorted(newlist, reverse=True)


print(int_list([1, 3, "Param", 6, 2]))

"""
# Task 9: Create a Python function that accepts a string. 
The function should return a string, with each character in the original string doubled. 
If you send the function "now" as a parameter, it should return "nnooww," and if you send "123a!", it should return "112233aa!!".
"""


def str_double(var):

    obj = str()

    for char in var:
        obj = obj + char + char
    return obj


print(str_double("abc"))

fruits = ("apple", "banana", "cherry", "tarbooj")

(green, yellow, *red) = fruits
print(green)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "car_number": 12.34,
}

int_dict = {
    key: value
    for key, value in thisdict.items()
    if type(value) == str or type(value) == float
}

print(int_dict)

"""
# Task 10: Write a function named capital_indexes. The function takes a single parameter, which is a string. 
Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
"""


def func(var):

    l = [x[0] for x in enumerate(var) if x[1].isupper()]
    return l


print(func("pAramvEEr"))

"""
# Task 11: a) Ask the user to enter their given name and surname in response to a single prompt. 
# Use split to extract the names, and then assign each name to a different variable. 
# For this exercise, you can assume that the user has a single given name and a single surname.

#11 b) Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method. 
"""

# a)
name = input("Please give in your first and last name, comma seperated: ")


def func():

    name_list = name.split("; ")
    first_name, last_name = name_list
    print(f"First Name: {first_name}, Last Name: {last_name}")


func()
print(func())

# b)

l = [1, 2, 3, 4, 5]


def format_converter(l):

    str_list = [str(x) for x in l]
    return " - ".join(str_list)


print(format_converter(l=[1, 2, 3, 4, 5]))

"""
# Task 12: Each quote is a string, but each string actually contains quote characters at the start and end. 
Extract the text from each string, without these extra quote marks, and print each quote in a new list.
"""

quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'",
]


def quote_extractor():

    quotes_extracted = [quote[1][1:-1].strip() for quote in enumerate(quotes)]
    # for x in enumerate(quotes):
    #     new_l.append(x[1][1:-1])
    print(f"Quotes: {quotes_extracted}")


quote_extractor()


"""
# Task 13: Ask the user to enter a word, and then print out the length of the word. 
You should account for any excess whitespace in the users input, so you are going to have to process the string before you find its length.

If you want to take this a little bit further, you an ask the user for a long piece of text. 
You can then tell them how many how many characters are in the text overall, and you can also provide them a word count.
"""


def word_clean(word):

    word = word.strip()
    return len(word)


print(word_clean("      paramveer"))

text = input("Please write a random sentence: ")


def word_count():

    print(f"Character Count: {len(text)}, Word Count: {len(text.split())}")


word_count()

"""
# Task 14: For this project, your program should do the following:

a) Calculate the average budget of all movies in the data set.
b) Print out every movie that has a budget higher than the average you calculated. 
   You should also print out how much higher than the average the movie's budget was.
c) Print out how many movies spent more than the average you calculated.

Additional Task: For the extra part of this assignment, we're going to:

Ask the user how many movies they want to add to the list.
Use range and a for loop to perform some option the specified number of times.
Ask the user for a movie name and budget during each iteration of the loop, and append a tuple to the movies list containing this information.

"""

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000),
]

# a)

movie_count = int(input("How many movie you want to add: ".title()))


def average_budget():

    for _ in range(movie_count):
        movie_name = input("Enter the Movie Name: ")
        movie_budget = int(input("Enter the Movie Budget: "))
        new_movie = (movie_name, movie_budget)
        movies.append(new_movie)

    print(f"movies: {movies}")

    budget_list = [budget[1] for budget in movies]
    total_budget = sum(budget_list)

    # or
    # for budget in movies:
    #     budget_list.append(budget[1])
    #     total_budget = sum(budget_list)

    avg_budget = total_budget / len(movies)
    return avg_budget

    # return f"Average Budget: {total_budget / len(movies)}"


# b) and c)
def above_average_budget():

    avg_budget = average_budget()
    above_average_budget_list = [movie[0] for movie in movies if movie[1] > avg_budget]

    for movie in movies:
        if movie[0] in above_average_budget_list:
            print(
                f"Budget of {movie[0]} is above average by an Amount: {movie[1] - avg_budget}: "
            )

    return "List of movies with an above average budget -> {}".title().format(
        above_average_budget_list
    )


print(above_average_budget())


"""
# Task 15: Fizzbuzz challenge:

One player starts by saying the number 1.
Each player then takes it in turns to say the next number, counting one at a time.
If the number is divisible by 3, instead of saying the number, the player should say, "Fizz".
If the number is divisible by 5, instead of saying the number, the player should say, "Buzz".
If the number is divisible by 3and5, instead of saying the number, the player should say, "Fizz Buzz".
If you make a mistake, you're usually eliminated from the game, and the game continues until there's only a single player remaining.
"""


def fizzBuzz():

    l = []
    for number in range(101):
        if number % 3 == 0:
            l.append("Fizz")
            # print("Fizz")
        elif number % 5 == 0:
            # print("Buzz")
            l.append("Buzz")
        elif (number % 3 == 0) and (number % 5 == 0):
            # print("Fizz Buzz")
            l.append("Fizz Buzz")
        else:
            l.append(number)
    return l


print(fizzBuzz())


"""
# Task 16: 
a) Write a short guessing game program using a while loop. The user should be prompted to guess a number between 1 and 100, 
and you should tell them whether their guess was too high or too low after each guess. 
The loop should keeping running until the user guesses the number correctly.

b) Use a loop and the continue keyword to print out every character in the string "Python", except the "o".
Remember that strings are collections, and they are iterable, so you can iterate over the string, which will yield one character at a time.

c) TODO: Using one of the examples from earlier—or a solution entirely of your own—create a program that prints out every prime number between 1 and 100.
"""


# a)

target_number = random.randint(10, 15)


def guessGame():

    guess = int(input("Guess a number between 1 and 100: "))
    while guess != target_number:
        if guess > target_number:
            print(f"{guess} is too High!")
        elif guess < target_number:
            print(f"{guess} is too low!")
        guess = int(input("try again: ".title()))
    print(f"Good Job! {guess} is correct")


guessGame()

# b)


def characterTracker(var):

    for char in var:
        if char != "o":
            print(char)
            continue


# or

# for char in var:
#     if char == "o":
#         continue
#     print(char)


characterTracker(var="Python")

"""
Task 17: To determine whether a given card number is valid or not using Luhn Algorithm.
This algorithm is actually used in real-life applications to test credit or debit card numbers as well as SIM card serial numbers.

Purpose of the Task: The purpose of the algorithm is to identify potentially mistyped numbers, 
because it can determine whether or not it's possible for a given number to be the number for a valid card.

What the Luhn Algorithm states:
1. Remove the rightmost digit from the card number. This number is called the checking digit, and it will be excluded from most of our calculations.
2. Reverse the order of the remaining digits.
3. For this sequence of reversed digits, take the digits at each of the even indices (0, 2, 4, 6, etc.) and double them. If any of the results are greater than 9, 
subtract 9 from those numbers.
4. Add together all of the results and add the checking digit.
5. If the result is divisible by 10, the number is a valid card number. If it's not, the card number is not valid.

"""
cardNum = list(input("Please enter your card number: ".strip()))

processedDigits = []


def credit_card_validator():

    checkDigit = cardNum.pop()
    cardNum.reverse()
    print(cardNum)
    for index, digit in enumerate(cardNum):
        if index % 2 == 0:
            doubleDigit = int(digit) * 2

            if doubleDigit > 9:
                doubleDigit = doubleDigit - 9
            processedDigits.append(doubleDigit)
        else:
            processedDigits.append(int(digit))

    total = int(checkDigit) + sum(processedDigits)
    if total % 10 == 0:
        return f"valid card number".title()
    return f"invalid card number".title()


print(credit_card_validator())

"""
Task 18: a) Inside the tuple we have the album name, the artist (in this case, the band), 
the year of release, and then another tuple containing the track list.

Convert this outer tuple to a dictionary with four keys.

b) Iterate over the keys and values of the dictionary you create in exercise 1. 
For each key and value, you should print the name of the key, and then the value alongside it.

c) Delete the track list and year of release from the dictionary you created. 
Once you've done this, add a new key to the dictionary to store the date of release. 
The date of release for The Dark Side of the Moon was March 1st, 1973.

d) Try to retrieve one of the values you deleted from the dictionary. 
This should give you a KeyError. Once you've tried this, repeat the step using the get method to prevent the exception being raised.
"""

album = (
    "The Dark Side of the Moon",
    "Pink Floyd",
    1973,
    (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse",
    ),
)

# create a list with a collection of required keys
l = ["Album", "Band", "Year", "Tracks"]

album_dict = {key: value for key, value in zip(l, album)}
print(album_dict["Tracks"])


for key, val in album_dict.items():
    print(f"Key: {key}, Value: {val}")

del album_dict["Tracks"]
print(album_dict.get("Tracks"))
# print(album_dict["Tracks"])
album_dict["date of release".title()] = "March 1st, 1973"
print(album_dict)


"""
Task 19: For this project the application needs to have the following functionality:

a) Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
b) The program should store information about all of these books in a Python list.
c) Users should be able to display all the books in their reading list, and these books should be printed out in a user-friendly format.
d) Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program. 

"""

reading_list = []
menu_prompt = """Please enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 'q' to quit

What would you like to do? """
selected_option = input(menu_prompt)


def add_book():
    title = input("please enter the title: ".strip().title())
    author = input("please enter the author: ".strip().title())
    year = input("please enter the year of publication: ".strip().title())

    book_keys = ["title", "author", "year"]
    book_values = (title, author, year)

    reading_list.append(
        {
            key: val
            for key, val in zip(
                book_keys,
                book_values,
            )
        }
    )
    print(reading_list)


def show_books():
    for book in reading_list:
        print(f"{book['title']}, by {book['author']} ({book['year']})")


while selected_option != "q":
    if selected_option == "a":
        add_book()

    elif selected_option == "l":
        if reading_list:
            show_books()
        else:
            print("yout reading list is empty".title())

    else:
        print("Invalid option selected")

    selected_option = input(menu_prompt).strip().lower()
