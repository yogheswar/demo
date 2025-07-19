def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # Found the target, return its index
    return -1  # Target not found

# Example usage
numbers = [10, 23, 45, 70, 11, 15]
search_value = 70

result = linear_search(numbers, search_value)

if result != -1:
    print(f"Value {search_value} found at index {result}.")
else:
    print(f"Value {search_value} not found in the list.")