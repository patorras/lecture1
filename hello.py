# This program says hello and asks for my nameself.

print('Hello World!')
print('What is you name?')  # ask for their name

myName = input()
print('It is good to meet you, ' + myName)
print('The lenght of your name is: ')
print(len(myName))
print('What is your age?')  #ask for their age

myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
