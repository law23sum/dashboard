import tutorial.app.basics.algorithms

# Test the function
print(tutorial.app.basics.algorithms.check_anagram("elvis", "lives"))                         # Should print True
print(tutorial.app.basics.algorithms.check_anagram("elvise", "livees"))                      # Should print True
print(tutorial.app.basics.algorithms.check_anagram("elvis", "dead"))                         # Should print False

# Test the function
print(tutorial.app.basics.algorithms.is_string_palindrome("anna"))                            # Should print True
print(tutorial.app.basics.algorithms.is_string_palindrome("kdljfasjf"))                         # Should print False
print(tutorial.app.basics.algorithms.is_string_palindrome("rats live on no evil star"))       # Should print True

# Test the function
n = 5
print(tutorial.app.basics.algorithms.calculate_factorial(n))                                 # Should print 120

# Test the function
a = "cat"
b = "chello"
c = "chess"

print(tutorial.app.basics.algorithms.levenshtein_distance(a, b))  # Should print 5
print(tutorial.app.basics.algorithms.levenshtein_distance(a, c))  # Should print 4
print(tutorial.app.basics.algorithms.levenshtein_distance(b, c))  # Should print 3

# Test the function
s = {1, 2, 3}
print(tutorial.app.basics.algorithms.calculate_powerset(s))  # Should print the powerset of {1, 2, 3}

# Test the function
t = "xthexrussiansxarexcoming"
print(tutorial.app.basics.algorithms.rotate_thirteen(t))                                       # Encrypt the text
print(tutorial.app.basics.algorithms.rotate_thirteen(tutorial.app.basics.algorithms.rotate_thirteen(t)))  # Decrypt the text (should return original text)

# Test the function
n = 100
print(tutorial.app.basics.algorithms.sieve_of_eratosthenes(n))  # Should print the set of prime numbers up to 100

# Test the function
n = 10
print(tutorial.app.basics.algorithms.calculate_fibonacci_series(n))  # Should print the first 10 numbers in the Fibonacci series


# Test the function
l = [3, 6, 14, 16, 33, 55, 56, 89]
x = 33
print(tutorial.app.basics.algorithms.binary_search(l, x, 0, len(l) - 1))  # Should print 4, the index of 33 in the list

# Test the function
unsorted = [33, 2, 3, 45, 6, 54, 33]
print(tutorial.app.basics.algorithms.quicksort(unsorted))  # Should print the sorted list: [2, 3, 6, 33, 33, 45, 54]
