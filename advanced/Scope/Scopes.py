# Scopes
z = 5


def my_function():
    z = 3
    print(z)


def my_other_function():
    print(z)


my_function()
my_other_function()
print(z)
