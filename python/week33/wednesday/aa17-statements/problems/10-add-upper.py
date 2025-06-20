# Create a function `add_upper` that takes a string and returns all of the
# uppercase characters in the string.

# Write your solution here.

def add_upper(string):
    result = ""
    for char in string:
        if char.isupper():
            result += char
    return result


print(add_upper("ApPlE"))        #> APE
print(add_upper("Coding"))       #> C
print(add_upper("PIano"))        #> PI
print(add_upper("SUPREME"))      #> SUPREME