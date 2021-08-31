def hello(name: str) -> str:
    """
    A hello world function to say hello to a user

    :param name: Who this function will say hello to
    :return: A simple greeting in the command line
    :rtype: str
    """

    return f'Hello, {name}!'


if __name__ == '__main__':
    name = input("What's your name? ")
    res = hello(name)
    print(res)
