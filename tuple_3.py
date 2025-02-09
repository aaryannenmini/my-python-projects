def find(tuple):
    if len(tuple) == 0:
        return None, None  
    
    first_element = tuple[0]  # First element
    last_element = tuple[-1]  # Last element
    
    return first_element, last_element

# Example usage
the_tuple = (10, 20, 30, 40, 50)
first, last = find(the_tuple)

print(f"Tuple: {the_tuple}")
print(f"First element: {first}")
print(f"Last element: {last}")
