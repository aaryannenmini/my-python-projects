#creating list to hold the values with duplicates
a = [1, 2, 3, 4, 2, 5, 3]

b = (set(a))


if len(a) != len(b):
    print("Duplicates were found and removed.")
else:
    print("No duplicates found.")
print("List with duplicates removed:", b)