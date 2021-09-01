import math


def hello(name: str) -> str:
    """
    A hello world function to say hello to a user

    :param name: Who this function will say hello to
    :return: A simple greeting in the command line
    :rtype: str
    """

    return f'Hello, {name}!'


def pythagorean(a: float, b: float) -> float:
    """

    :param a: one side of a triangle
    :param b: the other side of a triangle
    :return: the length of the hypotenuse of the triangle
    :rtype: float
    """
    if a > 0 and b > 0:
        return math.sqrt(a ** 2 + b ** 2)
    else:
        raise Exception('Values must be greater than zero!!')


if __name__ == '__main__':
    # name = input("What's your name? ")
    # res = hello(name)
    # print(res)

    res = pythagorean(3, '4')
    print(res)
