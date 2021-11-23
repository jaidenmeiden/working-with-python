# Nested function
def main_return():
    z = 3

    def nested():
        return z

    return nested()


print("Experiment 1:")
my_function = main_return()
print(my_function)

