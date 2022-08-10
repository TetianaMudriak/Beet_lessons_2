from typing import Any


class Author:
    def __init__(self, name: str, country: str, birthday: str,
                 books: list[str]):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __str__(self):
        return f'Author: {self.name}, {self.country},' \
               f' {self.birthday}, {self.books}'

    def __repr__(self):
        return self.__str__()


class Book:
    num_books: int = 0

    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.num_books += 1

    def __str__(self):
        return f'Book: {self.name}, {self.year}, {self.author}'

    def __repr__(self):
        return self.__str__()


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books: list[Book] = []
        self.authors: list[Author] = []
        self.author = None

    def new_book(self, book: Book) -> Any:
        self.books.append(book)
        if book.author not in self.authors:
            return self.authors.append(book.author)

    def group_by_author(self, author_name: str) -> Any:
        for author in self.authors:
            if author_name == author.name:
                return author.books
        return None

    def group_by_year(self, book_year: int) -> list:
        books_list_by_year: list = []
        for book in self.books:
            if book_year == book.year:
                books_list_by_year.append(book)
        print("-" * 50)
        return books_list_by_year

    def __str__(self):
        return f'Library: {self.name}, {self.books}, {self.authors}'

    def __repr__(self):
        return self.__str__()


def main():
    author1 = Author("Den Brown", "USA", "22.06.1964",
                     ["The Lost Symbol", "The Da Vinci Code", "Angels & Demons",
                      "Inferno", "Origin"])
    book1 = Book("Origin", 2017, author1)
    lib1 = Library("Home library")
    lib1.new_book(book1)
    author2 = Author("Daniel Keyes", "USA", "9.08.1927",
                     [" Flowers for Algernon", "The Minds of Billy Milligan",
                      "The Milligan Wars: A True-Story Sequel", "Until Death"])
    book2 = Book("The Minds of Billy Milligan", 1981, author2)
    lib1.new_book(book2)
    book3 = Book("The Da Vinci Code", 2003, author1)
    lib1.new_book(book3)
    print(lib1.group_by_author("Den Brown"))
    book4 = Book("The Da Vinci  extended", 2003, author1)
    lib1.new_book(book4)
    print(lib1.group_by_year(2003))
    print(f"Number of books: {Book.num_books}")


if __name__ == '__main__':
    main()
