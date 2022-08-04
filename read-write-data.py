import json

"""
TASK: Reading/Writing JSON data
For this project the application needs to have the following functionality:

1. Users should be able to add a product to their shopping cart by providing a product name, category, and cost.
2. The program should store information about all of these products in a file called product.json, and this data should be stored in JSON format.
3. Users should be able to retrieve the products in their shopping cart, and these products should be printed out in a user-friendly format.
4. Users should be able to search for a specific product by providing the product name.
5. Users should be able to delete products
6. Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program.
"""


def add_product():
    products = get_all_products()

    name = input("enter product name: ".title()).strip()
    category = input("enter product category: ".title()).strip()
    cost = input("enter product cost: ".title()).strip()

    products.append(
        {
            "name": name,
            "category": category,
            "cost": cost,
        }
    )

    with open("products.json", "w") as create_product:
        json.dump(products, create_product)


def get_all_products():
    with open("products.json", "r") as list_product:
        return json.load(list_product)


def view_products(products):
    for product in products:
        print("Name: {name}, Category: [{category}], Cost: {cost} Rs".format(**product))


def search_product():
    matched_products = []

    products = get_all_products()
    search_term = input(
        "enter product name to perform desired operation: ".title()
    ).strip()
    for item in products:
        if search_term in item["name"]:
            matched_products.append(item)
    return matched_products


def delete_product():
    all_products = get_all_products()
    product_to_delete = search_product()

    if product_to_delete:
        all_products.remove(product_to_delete[0])
        print(f"{product_to_delete[0]['name']} has been deleted!!".title())

    with open("products.json", "w") as rewrite_products:
        json.dump(all_products, rewrite_products)


prompt_menu = """
Please select one of the following options.
- a: to add a product
- l: to list all products
- s: to search for a product by it's name
- d: to delete a product
- q: to quit the menu
What do you want to do?

"""

selected_option = input(prompt_menu).strip().lower()

while selected_option != "q":

    if selected_option == "a":
        add_product()

    elif selected_option == "l":
        products = get_all_products()
        if products:
            view_products(products=products)

    elif selected_option == "s":
        filtered_products = search_product()
        if filtered_products:
            view_products(filtered_products)

    elif selected_option == "d":
        delete_product()

    else:
        print("please select a valid option")

    selected_option = input(prompt_menu).strip().lower()


"""
Task: Reading writing CSV data : 
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


def delete_book():
    all_books = get_all_books()
    search_term = input("Delete book by author name: ".title()).strip().lower()
    for book in all_books:
        if search_term in book["author"].lower():
            all_books.remove(book)


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

    elif selected_option == "d":
        delete_book()

    else:
        print(f"{selected_option} is an invalid option, try again!")

    selected_option = input(menu_prompt)
