#Wrong scripting try to solve again properly with recursion
'''Fill in the blanks to make the is_power_of function return whether
the number is a power of the given base.
Note: base is assumed to be a positive number.
Tip: for functions that return a boolean value, you can return the result of a comparison.'''

#Ans:

def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number > base:
    # If number is equal to 1, it's a power (base**0).
    return (base**2)*base==number

  # Recursive case: keep dividing number by base.
  return is_power_of((number/base)/base,base)

print(is_power(8,2)) # Should be True
print(is_power(64,4)) # Should be True
print(is_power(70,10)) # Should be False
