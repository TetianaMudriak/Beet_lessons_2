import re
from functools import wraps

class EmailValidator:
    def __init__(self, email):
        self.validate(email)
        self.email = email

    @classmethod
    def validate(cls, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.match(regex, email):
            print(f'Email {email} is invalid. Please check the correctness!')
        else:
            print("Email is valid")


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self._id = id_
        self._name = name
        self._company = company
        self._workers = []

    @property
    def id_(self):
        return self._id

    @id_.setter
    def id_(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, value):
        self._workers.append(value)

    def __str__(self):
        return f'{self.__class__.__name__} name: {self.name}'

    def __repr__(self):
        return f'{self.__class__.__name__} name: {self.name}'


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self._id = id_
        self._name = name
        self._company = company
        self._boss = boss

    @property
    def id_(self):
        return self._id

    @id_.setter
    def id_(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, value: Boss):
        self._boss = value

    def add_worker(self):
        self._boss.workers = self

    def __str__(self):
        return f'{self.__class__.__name__} name: {self.name}'

    def __repr__(self):
        return f'{self.__class__.__name__} name: {self.name}'


class TypeDecorators:
    @staticmethod
    def to_int(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return int(f(*args, **kwargs))
            except ValueError:
                return "Can't convert this type to integer"
        return wrapper

    @staticmethod
    def to_str(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return str(f(*args, **kwargs))
            except ValueError:
                return "Can't convert this type to string"
        return wrapper

    @staticmethod
    def to_bool(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return bool(f(*args, **kwargs))
            except ValueError:
                return "Can't convert this type to boolean"
        return wrapper

    @staticmethod
    def to_float(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return float(f(*args, **kwargs))
            except ValueError:
                return "Can't convert this type to float"
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


def main():
    # Task 1
    em1 = EmailValidator('popy@gmail.com')
    em2 = EmailValidator('fgn.com')

    # Task2
    boss1 = Boss(1, "Billy", "ABC")
    boss2 = Boss(2, "Villy", "ABC")
    worker1 = Worker(1, "Max", "ABC", boss1)
    worker2 = Worker(2, "Ann", "ABC", boss1)
    worker1.add_worker()
    worker2.add_worker()
    worker1.boss = boss2
    print(boss1.workers)

    # Task 3
    print(do_something("True"))
    print(do_nothing(25))


if __name__ == '__main__':
    main()
