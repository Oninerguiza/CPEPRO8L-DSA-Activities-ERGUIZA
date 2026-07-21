def find_maximum(values):
    # Assume natin na yung first value is the largest to start
    maximum = values [0]  

    # Check natin each value na nasa list 
    for value in values:
        # Update natin yung maximum pag may larger na value na nahanap
        if value > maximum:
            maximum = value 
    # Ibalik ang pinakamataas na numero
    return maximum 

numbers = [15, 8, 42, 19, 3]
print(find_maximum(numbers))