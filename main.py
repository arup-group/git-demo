import os


def main(input: str):
    return f'Hello, {input}!'


if __name__ == '__main__':
    res = input("What's your name? ")
    hello = main(res)
    print(hello)
