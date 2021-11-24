# Generator
def my_gen():
    """Generator example"""

    print('Hello world!')
    n = 0
    yield n

    print('Hello heaven!')
    n = 1
    yield n

    print('Hello hell!')
    n = 2
    yield n


a = my_gen()
try:
    print(next(a))  # Hello world!
    print(next(a))  # Hello heaven!
    print(next(a))  # Hello hell!
    print(next(a))  # StopIteration
except StopIteration:
    pass

