def print_divisible_by_3(numbers):
    for num in numbers:
        if num % 3 != 0:
            continue  # Skip numbers not divisible by 3
        print(num)

# Example usage
numbers_list = [10, 12, 15, 19, 21, 25, 30]
print_divisible_by_3(numbers_list)