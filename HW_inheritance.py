from pprint import pprint


class Person:

    def __init__(self, first_name, second_name, age, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.gender = gender

    def greetings(self):
        print(f'Hello, my name is {self.first_name} {self.second_name}!')

    def action(self):
        print("I do nothing!")


class Student(Person):
    def __init__(self, first_name, second_name, age, gender):
        super().__init__(first_name, second_name, age, gender)

    def greetings(self):
        print(f'Hello, teacher! '
              f'My name is {self.first_name} {self.second_name}.')

    def action(self):
        print("I'm studying")


class Teacher(Person):
    def __init__(self, first_name, second_name, age, gender, salary, subject):
        super().__init__(first_name, second_name, age, gender)
        self.salary = salary
        self.subject = subject

    def greetings(self):
        if self.gender == "female":
            print(f'Hello, students! I am Mrs. {self.second_name}.')
        elif self.gender == "male":
            print(f'Hello, students! I am Mr. {self.second_name}.')
        else:
            print(f'Hello, students! I am teacher {self.second_name}.')

    def action(self):
        print(f'I\'m teaching {self.subject}')

    def experience(self):
        if self.salary < 0:
            print("Are you paying your employer for your work?")
        elif self.salary < 1000:
            print("You're assistant teacher")
        elif self.salary < 2000:
            print("You're category-1 teacher")
        else:
            print("You're Special-Grade teacher")


class Mathematician:

    def square_nums(self, nums: list):
        result = [num ** 2 for num in nums]
        print(result)

    def remove_positives(self, nums: list):
        result = [num for num in nums if num < 0]
        print(result)

    def filter_leaps(self, nums: list):
        result = []

        for num in nums:
            divided_by_100_and_400 = num % 100 == 0 and num % 400 == 0
            divided_by_4_not_100 = num % 4 == 0 and num % 100 != 0

            if num > 1582:
                if divided_by_100_and_400 or divided_by_4_not_100:
                    result.append(num)

        print(result)


class Product:

    def __init__(self, prod_type, name, price):
        self.prod_type = prod_type
        self.name = name
        self.price = price

    def ppprint(self):
        print(f'{self.prod_type} {self.name} {self.price}')


class ProductStore:

    def __init__(self):
        self.store = []
        self.product = None
        self.income = 0

    def add(self, product: Product, amount):
        self.product = product
        elem = {
            'prod_type': self.product.prod_type,
            'name': self.product.name,
            'price': round(self.product.price * 1.3, 2),
            'amount': amount,
        }
        self.store.append(elem)
        print(self.store)

    def set_discount(self, identifier, percent: int, identifier_type="name"):
        valid_ind_type = ["name", "prod_type"]
        if identifier_type in valid_ind_type:
            for item in self.store:
                if item[identifier_type] == identifier:
                    item["price"] = item["price"] * percent / 100
        else:
            return print("Make sure you enter right identifier type")
        print(self.store)

    def sell_product(self, product_name, amount):
        for item in self.store:
            if product_name == item["name"]:
                if item["amount"] >= amount:
                    item["amount"] = item["amount"] - amount
                    self.income += amount * item["price"]
                else:
                    raise Exception(f'Ooops, error! Don\'t have so '
                                    f'many {product_name} in stock, '
                                    f'only {item["amount"]} is available')

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.store

    def get_product_info(self, product_name):
        for item in self.store:
            if item["name"] == product_name:
                return tuple({item["name"], item["amount"]})
            else:
                print("Ooops, don\'t have this product in stock")


def main():
    # Task 1
    person1 = Person("Anna", "Tkach", 23, "female")
    student1 = Student("Yuliia", "Franko", 25, "female")
    teacher1 = Teacher("Larysa", "Tur", 52, "female", 1200, "Math")
    teacher2 = Teacher("Ihor", "Semenko", 48, "male", 2400, "History")
    person1.greetings()
    student1.greetings()
    teacher1.greetings()
    teacher2.greetings()
    person1.action()
    student1.action()
    teacher1.action()
    teacher2.action()
    teacher1.experience()
    teacher2.experience()

    # Task 2
    m = Mathematician()
    m.square_nums([7, 11, 5, 4])
    m.remove_positives([26, -11, -8, 13, -90])
    m.filter_leaps([2001, 1884, 1995, 2003, 2020])

    # Task 3
    p = Product('Sport', 'Football T-Shirt', 100)
    p2 = Product('Food', 'Ramen', 1.5)
    p3 = Product('Food', 'Ramen', 13)

    p.ppprint()
    p2.ppprint()

    s = ProductStore()

    s.add(p, 10)
    s.add(p2, 300)
    s.set_discount("Football T-Shirt", 70, "name")
    # s.add(p3, 50)
    s.sell_product("Ramen", 200)
    s.sell_product("Football T-Shirt", 5)
    print(s.get_income())
    pprint(s.get_all_products(), width=30)
    print(s.get_product_info("Ramen"))


if __name__ == '__main__':
    main()
