'''Complete the script by filling in the missing parts.
The function receives a name, then returns a greeting based on
whether or not that name is "Taylor".  '''

#Ans:

def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))
