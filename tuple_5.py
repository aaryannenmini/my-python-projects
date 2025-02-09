def product(tuple):
    if len(tuple) == 0:
        return 1  
    product = 1
    for num in tuple:
        product *= num 

    return product

the = (2, 3, 4, 5)
result = product(the)

print(f"Tuple: {the}")
print(f"Product of elements: {result}")
