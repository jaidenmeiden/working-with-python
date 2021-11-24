# Set (Unique and immutable)
# Covert to set
my_set = {1, 2, 3}
print("my_set =", my_set)

# Add element
my_set.add(4)
print("my_set =", my_set)

# Add multiply elements
my_set.update([1, 2, 5])
print("my_set =", my_set)

# Add multiply elements
my_set.update((1, 7, 2), {6, 8})
print("my_set =", my_set)

# Discard an element
my_set.discard(1)
print("my_set =", my_set)

# Remove an element
my_set.remove(2)
print("my_set =", my_set)

# Discard an element
my_set.discard(10)
print("my_set =", my_set)

# Delete random element
my_set.pop()
print("my_set =", my_set)

# Clean list
my_set.clear()
print("my_set =", my_set)

# No puedo remover un elemento que no existe y muestra KeyError.
# Esta es la diferencia entre discard y remove
# Remove an element
my_set = {1, 2, 3}
my_set.remove(12)
print("my_set =", my_set)
