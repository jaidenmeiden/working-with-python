# Sugar syntax
def upperCase(original):
    # Envoltura
    def wrapper(text):
        return original(text).upper()
    return wrapper


@upperCase
def message(name):
    return f'{name}, get a message'


print(message('Jaiden'))
