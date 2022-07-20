class Person:

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(
            f'Hello, my name is {self.firstname} {self.lastname} '
            f'and I\'m {self.age} years old')


class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        human_age = self.age * self.age_factor
        print(f'Your dog\'s age is {human_age} in human equivalent')


class TVController:

    def __init__(self, CHANNELS):
        self.CHANNELS = CHANNELS
        self.current = CHANNELS[0]

    def first_channel(self):
        fst_channel = self.CHANNELS[0]
        self.current = fst_channel
        print(fst_channel)

    def last_channel(self):
        lst_channel = self.CHANNELS[-1]
        self.current = lst_channel
        print(lst_channel)

    def turn_channel(self, N):
        self.N = N
        turned_channel = self.CHANNELS[N - 1]
        self.current = turned_channel
        print(turned_channel)

    def next_channel(self):
        if self.current == self.CHANNELS[-1]:
            nxt_channel = self.CHANNELS[0]
        else:
            nxt_channel = self.CHANNELS[(self.CHANNELS.index(self.current)) + 1]
        self.current = nxt_channel
        print(nxt_channel)

    def previous_channel(self):
        if self.current == self.CHANNELS[0]:
            prw_channel = self.CHANNELS[-1]
        else:
            prw_channel = self.CHANNELS[(self.CHANNELS.index(self.current)) - 1]
        self.current = prw_channel
        print(prw_channel)

    def current_channel(self):
        print(self.current)

    def is_exist(self, name):
        self.name = name
        if isinstance(self.name, str) and self.name in self.CHANNELS:
            print('Yes')
        elif isinstance(self.name, int) and self.name <= len(self.CHANNELS):
            print('Yes')
        else:
            print('No')


def main():
    # Task 1
    person1 = Person('Tetiana', 'Mudriak', '25')
    person2 = Person('Taras', 'Kvas', '27')
    person3 = Person('Carl', 'Johanson', '26')

    person1.talk()
    person2.talk()
    person3.talk()

    # Task 2
    germ_sheppard = Dog(2)
    korgi = Dog(5)
    husky = Dog(12)
    spaniel = Dog(9)

    germ_sheppard.human_age()
    korgi.human_age()
    husky.human_age()
    spaniel.human_age()

    # Task 3
    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = TVController(CHANNELS)
    controller.first_channel()
    controller.last_channel()
    controller.turn_channel(1)
    controller.next_channel()
    controller.previous_channel()
    controller.current_channel()
    controller.is_exist('BBC')
    controller.is_exist('BB')
    controller.is_exist(4)
    controller.is_exist(3)


if __name__ == '__main__':
    main()
