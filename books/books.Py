import csv
def read_books_from_csv(filename):
    books = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books

def get_books_by_author(books, author):
    return [book for book in books if 'author' in book and book['author'] == author]


def get_book_by_isbn(books, isbn):
    for book in books:
        if 'ISBN' in book and book['ISBN'].lower() == isbn.lower():
            return book.get('title'), float(book.get('price'))
    return None, None


def get_books_in_price_range(books, min_price, max_price):
    return [book for book in books if 'price' in book and min_price <= float(book['price']) <= max_price]

def search_books():
    filename = input("Enter the filename: ")
    books = read_books_from_csv(filename)

    while True:
        print("\nSearch options:")
        print("1. Search by author")
        print("2. Search by ISBN")
        print("3. Search by price range")
        print("4. Add a new book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            author = input("Enter the author name: ")
            author_books = get_books_by_author(books, author)
            if author_books:
                print("Books by", author + ":")
                for book in author_books:
                    print(book['title'])
            else:
                print("No books found by", author)

        elif choice == '2':
            isbn = input("Enter the ISBN: ")
            title, price = get_book_by_isbn(books, isbn)
            if title and price:
                print("Title:", title)
                print("Price:", price)
            else:
                print("Book not found with ISBN", isbn)

        elif choice == '3':
            min_price = float(input("Enter the minimum price: "))
            max_price = float(input("Enter the maximum price: "))
            price_books = get_books_in_price_range(books, min_price, max_price)
            if price_books:
                print("Books within price range", min_price, "-", max_price + ":")
                for book in price_books:
                    print(book['title'])
            else:
                print("No books found within the price range", min_price, "-", max_price)

        elif choice == '4':
            title = input("Enter the book title: ")
            author = input("Enter the author name: ")
            isbn = input("Enter the ISBN: ")
            price = float(input("Enter the price: "))

            new_book = {'title': title, 'author': author, 'ISBN': isbn, 'price': str(price)}
            books.append(new_book)

            with open(filename, 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=new_book.keys())
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow(new_book)

            print("Book added successfully!")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

search_books()
