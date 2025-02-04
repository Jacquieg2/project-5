def find_median(numbers):
    """
    Returns the median of a list of numbers.
    
    The function sorts the list and returns the middle value if the list length is odd.
    If the list length is even, it returns the average of the two middle values.
    """
    sorted_numbers = sorted(numbers)  # Sort the list
    n = len(sorted_numbers)
    mid = n // 2  # Find the middle index
    
    if n % 2 == 1:
        return sorted_numbers[mid]  # Return the middle element for an odd-length list
    else:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2  # Average of two middle elements for even-length list

# Example usage:
some_nums = [13, 7, -3, 82, 4]
result = find_median(some_nums)
print(result)  # Output: 7
