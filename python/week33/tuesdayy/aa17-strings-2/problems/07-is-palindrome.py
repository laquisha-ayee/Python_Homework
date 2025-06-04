# Create a function that returns whether or
# not the string is a Palindrome.

# Write your function here.

#def is_palindrome(word):
#    return word.lower() == word.lower() [::-1]

#so this uses a loop. it works the same. 
def is_palindrome(word):
    word = word.lower()
    for i in range(len(word) // 2):
        if word[i] != word[-(i + 1)]:
            return False
    return True


print(is_palindrome("kayak")) # True
print(is_palindrome("app"))  # False
print(is_palindrome("racecar")) # True
print(is_palindrome("valid")) # False