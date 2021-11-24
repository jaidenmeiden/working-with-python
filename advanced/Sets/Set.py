# Set (Unique and immutable)
# Un set no puede contener un objeto mutable
my_set = {3, 4, 5}
print("my_set =", my_set)

my_set1 = {"Hola", 3, 4, 5, False, True}
print("my_set1 = ", my_set1)

my_set2 = {3, 3, 5}
print("my_set2= ", my_set2)

my_set3 = {(1, 2, 3), 4}
print("my_set3 = ", my_set3)

# La lista no puede ser almacenada, ya que es mutable
# Following code show an exception
my_set4 = {[1, 2, 3], 4}
print("my_set4 = ", my_set4)
