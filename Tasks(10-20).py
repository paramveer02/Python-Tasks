import random
from collections import Counter 


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
Task 11: a) Ask the user to enter their given name and surname in response to a single prompt. 

Extract the names, and then assign each name to a different variable. 
For this exercise, you can assume that the user has a single given name and a single surname.

#11 b) Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5  
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
    # or
    word_count = Counter(text)
    print(word_count)


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

"""
Task 20: 
For this project the application needs to have the following functionality:

1. Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
2. The program should store information about all of these books in a file called books.csv, and this data should be stored in CSV format.
3. Users should be able to retrieve the books in their reading list, and these books should be printed out in a user-friendly format.
4. Users should be able to search for a specific book by providing a book title.
5. Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program.
"""


def add_book():
    title = input("Enter the book title: ".strip().title())
    author = input("Enter the book author: ".strip().title())
    year = input("Enter the year of publication: ".strip().title())

    with open("books.csv", "a") as book_file:
        book_file.write(f"{title},{author},{year}\n")


def get_all_books():
    books = []
    with open("books.csv", "r") as get_book:
        book_data = get_book.readlines()
        for row in book_data:
            values = row.strip().split(",")
            headers = ("title", "author", "year")
            books_dict = dict(
                zip(headers, values)
            )  # or implement dictionary comprehension
            # books_dict = {key: val for key, val in zip(headers, values)}
            books.append(books_dict)
        return books


def show_all_books(books):
    print()  # generate an empty line
    for book in books:
        print(f"-> {book['title']}, by {book['author']}, published in {book['year']}")
        print()


def search_books():
    all_books_list = get_all_books()
    matched_books = []
    search_term = input("Enter Book title you want to search: ".title()).strip().lower()
    for book in all_books_list:
        if search_term in book["title"].lower():
            matched_books.append(book)
    return matched_books


menu_prompt = """ Please select one of the following options: 

- 'a' to add a book
- 'l' to list the book
- 's' to search the book
- 'q' to quit

Please Select an Option:  
"""

selected_option = input(menu_prompt)


while selected_option != "q":
    if selected_option == "a":
        add_book()

    elif selected_option == "l":
        list_of_books = get_all_books()
        if list_of_books:
            show_all_books(list_of_books)
        else:
            print("the reading list is empty".title())

    elif selected_option == "s":
        filtered_books = search_books()
        if filtered_books:
            show_all_books(filtered_books)
        else:
            print("Sorry, could not find the book")

    else:
        print(f"{selected_option} is an invalid option, try again!")

    selected_option = input(menu_prompt)
