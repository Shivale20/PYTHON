"""Jarvis I am going to learn 
Concepts to implements
Loop, Exception, Conditionals and 
controlss in Python"""

# QUOTE : It is not about just coding but what thought process you have before even first code line.

print("Learn Conditional Statement: ", "\n")
print("Boolean Expression \n")
your_name = 'Jarvis'
bool_name = (your_name != 'Manish')

# what do you think this will give?
print(bool_name)

# 100% TRUE. because I stored Jarvis name in your_name and it is not equal to 'Manish'.

""" When it is raining, I make two choices
- choice 1: keep umbrella
- choice 2: do not keep umbrella

so here it is raining is a boolean expression

if it is raining == True, then [keep umbrella]

this is conditional statement.
"""

# create a bool variable to check if raining.
# it is better to use is_verbing to check boolean expression
is_raining = True
if is_raining:
    print('Keep Umbrella, Value of is_raining is ', is_raining)

""" Jarvis I know only you use my computer without my permission.
I will use control statement to keep you away from my computer
"""
# enter your username
user_name = 'Jarvis'

if user_name == 'Manish':
    print("WELCOME BACK HERO! \n")

if user_name != 'Manish':
    print("Get off my computer Jarvis \n")

print("\n----------------------------------------")
print("End of output.")
print("----------------------------------------\n")

"""
Jarvis, I will give one more chance. I know you have been using Siri username as well.
I will not allow you with that username either
"""
# enter your username
user_name = 'Siri'

if (user_name != 'Manish') and (user_name == 'Siri'):
    print("Get off my computer Jarvis. You can not fool me with username: ", user_name)

"""
I am allowed though to use your computer.
"""
# enter your username. Remember I am Jarvis's property
user_name = 'Manish'
if (user_name == 'Jarvis') or (user_name == 'Manish'):
    print('Welcome back HERO KE HERO')

print("\n----------------------------------------")
print("End of output.")
print("----------------------------------------\n")

"""
Jarvis lets check multiple criteria based on your age
"""
# enter your age and nationality
jarvis_age = 16
jarvis_nationality = 'Canada'

# if age is not greater or equal to 18, you are not allowed in party.
eligible_age = 18
if not (jarvis_age >= eligible_age):
    print("You are not allowed in party, Jarvis. \nYour age is ", jarvis_age, " and eligibile age is ", eligible_age)

# if you are not from India and above eligible age, then you are not allowed in party.
eligible_nationality = 'India'
if not (jarvis_age >= eligible_age) and not ( jarvis_nationality == 'India'):
    print("\n")
    print("You are not allowed in party, Jarvis. \nYour age is ", jarvis_age, " and eligibile age is ", eligible_age, 'and nationality allowed is ', eligible_nationality)

print("\n----------------------------------------")
print("End of output.")
print("----------------------------------------\n")

"""
Jarvis, I have used enough of IFS
Now I will keep my else option as well.
what do I need to do if condition I am checking false.

if it is raining, I will keep umbrella, else, I will not keep umbrella.
"""

# Jarvis see what will happen if you fulfil my condition of entry.
print("\n")

jarvis_age = 19
jarvis_nationality = 'India'

if not (jarvis_age >= eligible_age) and not ( jarvis_nationality == 'India'):
    print("\n")
    print("You are not allowed in party, Jarvis. \nYour age is ", jarvis_age, " and eligibile age is ", eligible_age, 'and nationality allowed is ', eligible_nationality)
else:
    print(" Jarvis! ENJOY THE PARTY with amazing  ME :>.")

print("\n----------------------------------------")
print("End of output.")
print("----------------------------------------\n")

"""
Jarvis I am thinking to donate few million dollars to ESG initation.
They will give us some elite type of status.
Let's check what status will we get upon different amount of donation amount in million.

However since we will have different criteria, we will use if, else if and else statements.
"""
donation = 50

print("Thank you for your DONATION to ESG. \n")
if donation >= 1000:
    print('Achieved PLATINUM status')
elif donation >= 500:
    print('Achieved GOLD status')
elif donation >= 100:
    print('Achieved SILVER status')
else:
    print('NEXT TIME - KINDLY EARN MORE MONEY.')

print("\n----------------------------------------")
print("End of output.")
print("----------------------------------------\n")

