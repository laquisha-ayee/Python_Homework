# Create a function which adds spaces before every capital in a word. Lower case
# the whole string afterwards.

# Write your function here.

def cap_space(word):
    result = ""
    for i, char in enumerate(word):
        if i > 0 and char.isupper():
            result += " "
        result += char
    return result.lower()


print(cap_space("helloWorld"))     #> "hello world"
print(cap_space("iLoveMyTeapot"))  #> "i love my teapot"
print(cap_space("stayIndoors"))    #> "stay indoors"