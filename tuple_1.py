def number(tuple):
    if len(tuple) == 0:
        return None, None  
    max_number = max(tuple)
    min_number = min(tuple)

    return max_number, min_number
The_tuple = (23, 1, 56, 5, 0)
max_numb, min_numb = number(The_tuple)

print(f"Tuple: {The_tuple}")
print(f"Maximum value: {max_numb}")
print(f"Minimum value: {min_numb}")
