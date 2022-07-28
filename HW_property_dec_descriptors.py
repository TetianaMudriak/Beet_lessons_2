import re


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
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss


def main():
    # Task 1
    em1 = EmailValidator('popy@gmail.com')
    em2 = EmailValidator('fgn.com')

    # Task2
    boss1 = Boss(1, "Billy", "ABC")


if __name__ == '__main__':
    main()
