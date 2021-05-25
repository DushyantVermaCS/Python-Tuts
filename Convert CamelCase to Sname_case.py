# Convert Lettrs from CamelCase to snake_case :>---------------------------------

ph = input()    #input any phase 
fis = ph[0].lower()  #first letter of phase
letter = ""
for word in ph[1: ]:
    if word.isupper():
        word ="_"+word.lower() 
    #print(word)
    letter +=  word
print(fis+letter)
        
        

''' -----------------BY  USING Replace Method---------------------------------------
text = input()

for letter in text:
    if letter.isupper():
        text = text.replace(letter, "_" + letter.lower(), 1)

print(text)
 '''


