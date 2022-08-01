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
    
    elif st == "none":
        return num
    else:
        return None


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
