# Sequential Scopes
z = 5


def my_function():
    z = 3

    def my_other_function():
        z = 2
        print(z)

    my_other_function()
    print(z)


my_function()
print(z)
