# Author: Jacqueline Garcia
# GitHub username: Jgarcia2
# Date: 02/04/2025
# Description: Without Duplicates 

def without_duplicates(lst):
    """
    Returns a new list with duplicates removed while maintaining the original order.

    Parameters:
    lst (list): The input list with potential duplicates.

    Returns:
    list: A list containing unique elements in the order they first appeared.
    """
    seen = set()
    unique_list = []
    
    for item in lst:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    
    return unique_list

# Example usage:
my_list = [8, 'hello', 8, True, -1000000.4, 'hello', 8]
result = without_duplicates(my_list)
print(result)  # Output: [8, 'hello', True, -1000000.4]
