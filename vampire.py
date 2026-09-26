name = 'Carol'  # Initial variable assignment
age = 3000  # Initial variable assignment

# Check if the name is 'Alice', print a personalized message if true
if name == 'Alice': 
    print('Hi, Alice.')

# Check if the age is less than 12, print a message if the name is not 'Alice' and the age is less than 12
elif age < 12:
    print('You are not Alice, kiddo.')

# Check if the age is greater than 2000, print a message if the name is not 'Alice', the age is less than 12, 
# and the age is greater than 2000
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')

# Check if the age is greater than 100, print a message if the conditions above are not met
elif age > 100:
    print('You are not Alice, grannie.')