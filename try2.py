'''#Convert Lettrs from CamelCase to snake_case :>---------------------------------

ph = input()    #input any phase 
fis = ph[0].lower()  #first letter of phase
letter = ""
for word in ph[1: ]:
    if word.isupper():
        word ="_"+word.lower() 
    #print(word)
    letter +=  word
print(fis+letter) '''

# work with a list from this variable
numbers = [int(n) for n in input()]

# change the next two lines
less_than_5 = [int(num) for num in numbers if num < 5]
greater_than_5 = [int(num) for num in numbers if num > 5]

# printing your results
print(less_than_5)
print(greater_than_5)

        
        



