# Author: Jacqueline Garcia
# GitHub username: Jgarcia2
# Date: 02/04/2025
# Description: surname.

def add_surname(names):
    """
    Returns a list of names that start with 'K', with 'Kardashian' added as a surname.
    
    Parameters:
    names (list): A list of first names.

    Returns:
    list: A list of names with 'Kardashian' added to those starting with 'K'.
    """
    return [name + " Kardashian" for name in names if name.startswith("K")]

# Example usage:
name_list = ["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"]
result = add_surname(name_list)
print(result)  # Output: ['Kiki Kardashian', 'Krystal Kardashian', 'Koala Kardashian']
