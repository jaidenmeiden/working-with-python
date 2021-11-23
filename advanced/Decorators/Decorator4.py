# Sugar syntax
def with_custom_message(message):
    def with_message(original):
        print(f'The function is {message}')

        # Envoltura
        # Recibe cualquier cantidad los argumentos posicionales (args) o argumentos nombrados (kwargs)
        def wrapper(*args, **kwargs):
            original(*args, **kwargs)

        return wrapper

    return with_message


@with_custom_message("multiplying")
def multiplier(a, b):
    c = a * b
    print(f'Result of {a} * {b} is {c}')


multiplier(10, 2)
