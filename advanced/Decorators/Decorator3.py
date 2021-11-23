# Sugar syntax
from datetime import datetime


def execution_time(original):
    # Envoltura
    # Recibe cualquier cantidad los argumentos posicionales (args) o argumentos nombrados (kwargs)
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        original(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Passed: " + str(time_elapsed.total_seconds()) + " seconds")

    return wrapper


@execution_time
def random_function():
    for _ in range(1, 1000000):
        pass


@execution_time
def random_function_limit(limit):
    for _ in range(1, limit):
        pass


@execution_time
def adder(a: int, b: int) -> int:
    print(a + b)
    return a + b


@execution_time
def greeting(name="Alfredo"):
    print(f'Hi {name}')


random_function()
random_function_limit(100000000)
adder(7, 14)
greeting("Jaiden")
greeting()
