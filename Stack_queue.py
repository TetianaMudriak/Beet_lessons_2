from collections import deque
from queue import LifoQueue


def reverse_list(given_list: list[str | int]) -> list[str | int]:
    stack = deque()
    reversed_list = []
    popped = None
    for elem in given_list:
        stack.append(elem)
    while len(stack) > 0:
        popped = stack.pop()
        reversed_list.append(popped)

    return reversed_list


def balancing_parentheses(user_string: str):
    opening_braces: list[str] = ["(", "{", "["]
    stack = deque()

    for symbol in user_string:
        if symbol in opening_braces:
            stack.append(symbol)

        else:
            if not stack:
                return False

            if (stack[-1] == "(" and symbol == ")") or (
                    stack[-1] == "{" and symbol == "}") or (
                    stack[-1] == "[" and symbol == "]"):
                stack.pop()

            else:
                return False

    if stack:
        print('Not balanced!')
    else:
        print('Balanced!')


class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

    def get_from_stack(self, elem_name):
        for elem in self.stack:
            if elem == elem_name:
                self.stack.remove(elem)
                return elem_name
        else:
            raise ValueError('Given element not found in stack')

    def __str__(self):
        return f'{self.__class__.__name__}: {self.stack}'


class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def get_from_queue(self, elem_name):
        for elem in self.queue:
            if elem == elem_name:
                self.queue.remove(elem)
                return elem_name
        else:
            raise ValueError('Given element not found in queue')

    def __str__(self):
        return f'{self.__class__.__name__}: {self.queue}'


def main():
    # Task 1
    print(reverse_list(["a", "b", "c"]))
    print(reverse_list([1, 2, 3, 4, 5]))

    # Task 2
    balancing_parentheses("([]){}[]")
    balancing_parentheses("((()[]{})")
    balancing_parentheses("{[]}(){}")

    # Task 3
    stack1 = Stack()
    stack1.push("a")
    stack1.push("b")
    stack1.push("c")
    stack1.push("d")
    stack1.get_from_stack("c")
    print(stack1)
    # stack1.get_from_stack("e")


if __name__ == '__main__':
    main()
