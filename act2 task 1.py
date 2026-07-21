def find_maximum(values):
    # Assume the first value is the largest to start
    maximum = values [0]  

    # Check each value in the list 
    for value in values:
        # Update maximum if a larger value is found
        if value > maximum:
            maximum = value 
    # Return the largest number
    return maximum 

numbers = [15, 8, 42, 19, 3]
print(find_maximum(numbers))