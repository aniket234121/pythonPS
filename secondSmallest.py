def second_smallest(numbers):
    if len(numbers) < 2:
        return "List should have at least two elements"

    smallest = float('inf')
    second_smallest = float('inf')

    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    return second_smallest

numbers_list = [5, 3, 8, 2, 7, 1]
result = second_smallest(numbers_list)

print(f"The second smallest number is: {result}")
