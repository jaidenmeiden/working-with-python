# Decorator
def decorator(original):
    # Envoltura
    def wrapper():
        print('It is added to original function')
        original()

    return wrapper


def greeting():
    print('!Hello¡')


greeting()

greeting = decorator(greeting)
greeting()
