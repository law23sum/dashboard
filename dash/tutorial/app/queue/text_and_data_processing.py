# Counting word occurrences in a given string
news = (
    '''Python is an interpreted, high-level and mini_apps.py-purpose programming
     language. Python's design philosophy emphasizes sample_code readability with
     its notable use of significant whitespace. 
     Its language constructs and object-oriented approach aim to help 
     programmers write clear, logical sample_code for small- and large-scale 
     projects.'''
)

word_count = dict()
words = news.split()

for word in words:
    # `dict.get(key, default)` returns the value for the given key if it exists, otherwise it returns the default value.
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)

max_count = max(word_count.values())
most_frequent_words = [word for word, count in word_count.items() if count == max_count]

print("Most frequent word(s):", ', '.join(most_frequent_words))

# Extracting last name from an email
email = "John.Smith@uky.edu"
name, domain = email.split('@')
first, last = name.split('.')
print(f"Last name is {last}")

# Working with a list
lst = [1, "a", "hello"]
lst.append(2)
print(lst)
