# In Python, error handling can be done using a `try`/`except` block. Implement
# `except` blocks to handle the exceptions that will be raised for the following
# `try` blocks:

# Example 1
try:
    str = 'hello'
    str[0] = 'm'
    print(str)
except TypeError:
    print(f"Cannot modify string - strings are immutable")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    print('I happen regardless of any exceptions.')

# Example 2
try:
    print(x)
except NameError:
    print("Variable not defined")
except Exception as e:
    print("unexpected error: {e}")
finally:
    print('I happen regardless of any exceptions.')