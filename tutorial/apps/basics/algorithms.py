from functools import reduce

def check_anagram(str1, str2):
    """
    Check if two strings are anagrams.

    Parameters:
    str1 (str): First string.
    str2 (str): Second string.

    Returns:
    bool: True if str1 and str2 are anagrams, False otherwise.
    """
    return sorted(str1) == sorted(str2)  # Compare sorted strings

def is_string_palindrome(phrase):
    """
    Check if a given string is a palindrome.

    Parameters:
    phrase (str): The string to be checked.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    return phrase == phrase[::-1]  # Compare the string with its reverse

def calculate_factorial(number):
    """
    Calculate the factorial of a given number.

    Parameters:
    number (int): The number to calculate the factorial of.

    Returns:
    int: The factorial of the given number.
    """
    if number > 1:
        return number * calculate_factorial(number - 1)  # Recursive call for factorial calculation
    else:
        return 1  # Base case: factorial of 1 is 1

def levenshtein_distance(str1, str2):
    """
    Calculate the Levenshtein distance between two strings.

    The Levenshtein distance is a measure of the number of single-character edits
    (insertions, deletions, or substitutions) required to change one word into the other.

    Parameters:
    str1 (str): First string.
    str2 (str): Second string.

    Returns:
    int: The Levenshtein distance between the two strings.
    """
    if not str1:
        return len(str2)
    if not str2:
        return len(str1)

    return min(
        levenshtein_distance(str1[1:], str2[1:]) + (str1[0] != str2[0]),  # Substitution
        levenshtein_distance(str1[1:], str2) + 1,                          # Deletion
        levenshtein_distance(str1, str2[1:]) + 1                           # Insertion
    )


def calculate_powerset(set_elements):
    """
    Calculate the powerset of a given set.

    The powerset includes all possible subsets of a set,
    including the empty set and the set itself.

    Parameters:
    set_elements (set): The set for which the powerset is to be calculated.

    Returns:
    list: A list of sets representing the powerset of the input set.
    """
    return reduce(lambda P, x: P + [subset | {x} for subset in P], set_elements, [set()])

def rotate_thirteen(text):
    """
    Encrypt or decrypt a text using Caesar's cipher with a rotation of 13.

    This function rotates each letter in the text by 13 positions in the alphabet.
    It encrypts the text if it's plain, or decrypts it if it's already encrypted.

    Parameters:
    text (str): The text to be encrypted or decrypted.

    Returns:
    str: The encrypted or decrypted text.
    """
    abc = "abcdefghijklmnopqrstuvwxyz"
    return "".join([abc[(abc.find(c) + 13) % 26] for c in text])

def sieve_of_eratosthenes(limit):
    """
    Find all prime numbers up to a given limit using the Sieve of Eratosthenes.

    Parameters:
    limit (int): The upper limit for finding prime numbers.

    Returns:
    set: A set of all prime numbers up to the given limit.
    """
    return reduce(lambda r, x: r - set(range(x ** 2, limit, x)) if x in r else r, range(2, int(limit ** 0.5) + 1),
                  set(range(2, limit)))

def calculate_fibonacci_series(length):
    """
    Calculate the Fibonacci series up to a given length.

    Parameters:
    length (int): The number of elements in the Fibonacci series to calculate.

    Returns:
    list: A list containing the Fibonacci series up to the specified length.
    """
    return reduce(lambda x, _: x + [x[-2] + x[-1]], [0] * (length - 2), [0, 1])

def binary_search(arr, target, low, high):
    """
    Perform a binary search for a target value in a sorted array.

    Parameters:
    arr (list): The sorted array to search.
    target (int): The target value to search for.
    low (int): The lower index for the search range.
    high (int): The higher index for the search range.

    Returns:
    int: The index of the target in the array if found, -1 otherwise.
    """
    if low > high:
        return -1  # Target not found
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid  # Target found
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)  # Search in the left half
    else:
        return binary_search(arr, target, mid + 1, high)  # Search in the right half

def quicksort(arr):
    """
    Sort an array using the Quicksort algorithm.

    Parameters:
    arr (list): The array to be sorted.

    Returns:
    list: The sorted array.
    """
    if not arr:
        return []
    return quicksort([x for x in arr[1:] if x <= arr[0]]) + [arr[0]] + quicksort([x for x in arr if x > arr[0]])
