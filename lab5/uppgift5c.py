def contains(word,haystack):
    filtered_haystack = list(filter(lambda x : word == x, haystack))
    if len(filtered_haystack) > 0:
        return True

    return False

haystack = 'Can you find the needle in this haystack?'.split ()

print(contains('find', haystack))
print(contains('needle', haystack))
print(contains('haystack', haystack))
