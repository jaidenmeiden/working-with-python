# Iterator
my_list = [1,2,3,4,5]
my_iter = iter(my_list)

# Iterando un iterator
print("First element: ", next(my_iter))

# When doesn't hove data, exception StopIterando is showing

# If We have one million elements, then
print("Other elements with infinite while:")
while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break

# We can use for (Syntactic sugar) to loop iterator, for cycle convert element in iterator
print("Elements with for:")
for element in my_list:
    print(element)
