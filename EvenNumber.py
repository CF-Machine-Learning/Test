def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Test the function
number = 12  # Example number
if is_even(number):
    print(f"{number} is an even number")
else:
    print(f"{number} is not an even number")
