def next_lexicographical_sequence(s: str) -> str:
    letters = list(s)

    pivot = len(letters) - 2
    while pivot >= 0 and letters[pivot] >= letters[pivot + 1]:
        pivot -=1

    if pivot == -1:
        return ''.join(reversed(letters))

    righmost_successor = len(letters) - 1
    while letters[righmost_successor] <= letters[pivot]:
        righmost_successor -=1 

    letters[pivot], letters[righmost_successor] = letters[righmost_successor], letters[pivot]

    letters[pivot+1:] = reversed(letters[pivot + 1:])
    return ''.join(letters)


print(next_lexicographical_sequence("abdc"))  # Output: "acbd"
print(next_lexicographical_sequence("dcba"))  # Output: "abcd"
