'''6.5 Write code using find() and string slicing (see section 6.10)
to extract the number at theend of the line below.
Convert the extracted value to a floating point number and print it out.'''

#ans:

text = "X-DSPAM-Confidence:    0.8475";
fi=text.find('   ')
piece=text[fi+4:]
num=float(piece)
print(num)
