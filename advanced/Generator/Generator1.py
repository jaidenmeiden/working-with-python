# Generator
my_list = [0, 1, 4, 7, 9, 10]

print("list comprehension:")
my_second_list = [print(x * 2) for x in my_list]  # list comprehension
print("Generator expression:")
my_second_gen = (x * 2 for x in my_list)  # Generator expression
for element in my_second_gen:
    print(element)
