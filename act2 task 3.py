def insert_at(arr, index, value):
    # Gumawa ng bagong list at i-insert ang value sa ibinigay na index
    return arr[:index] + [value] + arr[index:]


# Original na list
numbers = [10, 20, 30, 40]

# I-insert ang 25 sa index 2 at i-print ang result
print(insert_at(numbers, 2, 25))