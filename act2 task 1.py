def find_maximum(values):
    maximum = values [0]

    for value in values:
        if value > maximum:
            maximum = value 

    return maximum 

numbers = [15, 8, 42, 19, 3]
print(find_maximum(numbers))