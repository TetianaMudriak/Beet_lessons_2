def to_power(x: int | float, exp: int) -> int | float:
    if exp < 0:
        raise ValueError("This function works only with exp > 0.")
    if exp == 0:
        return 1
    return x * to_power(x, exp - 1)


def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) < 1:
        return True
    if looking_str[0] == looking_str[-1]:
        return is_palindrome(looking_str[1:-1])
    return False


def mult(a: int, n: int) -> int:
    if a < 0 or n < 0:
        raise ValueError("This function works only with positive integers")
    if n == 0:
        return 0
    return a + mult(a, n-1)


def reverse(input_str: str) -> str:
    if len(input_str) < 1:
        return input_str
    else:
        return input_str[-1] + reverse(input_str[:-1])


def sum_of_digits(digit_string: str) -> int:
    if not digit_string.isnumeric():
        raise ValueError("input string must be digit string")
    if len(digit_string) == 1:
        return int(digit_string)
    return int(digit_string[0]) + sum_of_digits(digit_string[1:])


def main():
    # Task 1
    print(to_power(2, 3))
    print(to_power(3.5, 2))
    # print(to_power(2, -1))

    # Task 2
    print(is_palindrome('mom'))
    print(is_palindrome('sassas'))
    print(is_palindrome('o'))

    # Task 3
    print(mult(2, 4))
    print(mult(2, 0))
    print(mult(2, -4))

    # Task 4
    print(reverse("hello"))
    print(reverse("tania"))
    print(reverse("0"))

    # Task 5
    print(sum_of_digits("26"))
    print(sum_of_digits("test"))


if __name__ == '__main__':
    main()
