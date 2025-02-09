def count(tuple):
    even = 0
    odd = 0

    for num in tuple:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd

th_tuple = (10, 15, 20, 25, 30, 35, 40)
even, odd = count(th_tuple)

print(f"Tuple: {th_tuple}")
print(f"Number of even numbers: {even}")
print(f"Number of odd numbers: {odd}")
