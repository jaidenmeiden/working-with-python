# Sugar syntax
def decorator(original):
    # Envoltura
    def wrapper():
        print('It is added to original function')
        original()

    return wrapper


@decorator
def greeting():
    print('!Hello¡')


greeting()
