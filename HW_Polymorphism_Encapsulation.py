from math import gcd


class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("Implemented by sub class")


class Cat(Animal):
    def talk(self):
        print("Niau-niau!")


class Dog(Animal):
    def talk(self):
        print("Gau-gau!")


def animal_talk(animals):
    for animal in animals:
        animal.talk()


class Author:
    def __init__(self, name, country, birthday, books: list):
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
    num_books = 0

    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.num_books += 1

    def __str__(self):
        return f'Book: {self.name}, {self.year}, {self.author}'

    def __repr__(self):
        return self.__str__()


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []
        self.book = None
        self.author = None

    def new_book(self, book: Book):
        self.book = book
        self.books.append(book)
        if book.author not in self.authors:
            self.authors.append(book.author)

    def group_by_author(self, author_name):
        for author in self.authors:
            if author_name == author.name:
                print(author.books)

    def group_by_year(self, book_year: int):
        books_list_by_year = []
        for book in self.books:
            if book_year == book.year:
                books_list_by_year.append(book)
        print("-" * 50)
        print(books_list_by_year)

    def __str__(self):
        return f'Library: {self.name}, {self.books}, {self.authors}'

    def __repr__(self):
        return self.__str__()


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if self.denominator == 0 or other.denominator == 0:
            print("Can't divide by zero")
        num = self.numerator * other.denominator + \
              self.denominator * other.numerator
        den = self.denominator * other.denominator
        self.numerator = int(num / gcd(num, den))
        self.denominator = int(den / gcd(num, den))
        return self

    def __sub__(self, other):
        if self.denominator == 0 or other.denominator == 0:
            print("Can't divide by zero")
        num = self.numerator * other.denominator - \
              self.denominator * other.numerator
        den = self.denominator * other.denominator
        self.numerator = int(num / gcd(num, den))
        self.denominator = int(den / gcd(num, den))
        return self

    def __mul__(self, other):
        if self.denominator == 0 or other.denominator == 0:
            print("Can't divide by zero")
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        self.numerator = int(num / gcd(num, den))
        self.denominator = int(den / gcd(num, den))
        return self

    def __truediv__(self, other):
        if self.denominator == 0 or other.denominator == 0:
            print('Can\'t divide by zero')
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        self.numerator = int(num / gcd(num, den))
        self.denominator = int(den / gcd(num, den))
        return self

    def __str__(self):
        return f'Fraction({self.numerator}, {self.denominator})'

    def __repr__(self):
        return self.__str__()


def main():
    # Task 1
    animals = [Cat("Kuzia"), Dog("Timur"), Cat("Malko"), Dog("Linda")]
    animal_talk(animals)

    # Task 2
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
    lib1.group_by_author("Den Brown")
    book4 = Book("The Da Vinci  extended", 2003, author1)
    lib1.new_book(book4)
    lib1.group_by_year(2003)
    print(f"Number of books: {Book.num_books}")

    # Task 3
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x + y)
    # print(x - y)
    # print(x * y)
    # print(x / y)


if __name__ == '__main__':
    main()
