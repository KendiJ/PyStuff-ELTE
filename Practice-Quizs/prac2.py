# function called count_characters(word) that takes a string. 
# It should return a dictionary where the keys are the characters and the values are how many times that character appears.

def count_charactors(word):
    counts = {}

    for char in word:
        if char in counts:
            counts[char] = counts[char] + 1
        else:
            counts[char] = 1
    return counts

print(count_charactors('banana'))
print(count_charactors('mississippi'))
print(count_charactors('My super app will work today'))