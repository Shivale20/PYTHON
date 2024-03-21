"""
Magic 8 Ball
Link: https://en.wikipedia.org/wiki/Magic_8_Ball

Design and usage

One of the possible responses of the Magic 8 Ball.
The Magic 8 Ball is a hollow plastic sphere resembling a black-and-white 8 ball. Its standard size is larger than an ordinary pool ball, but it has been made in different sizes. Inside the ball, a cylindrical reservoir contains a white plastic 20-sided regular icosahedron die floating in approximately 100 ml (3+1⁄2 US fl oz) of alcohol dyed dark blue. Each of the die's 20 faces has an affirmative, negative, or non-committal statement printed in raised letters. These messages are read through a window on the ball's bottom.

To use the ball, it must be held with the window initially facing down to allow the die to float within the cylinder. After asking the ball a yes–no question, the user then turns the ball so that the window faces up. The die floats to the top, and one face presses against the window; the raised letters displace the blue liquid to reveal the message as white letters on a blue background. 


Possible answers
A standard Magic 8 Ball has twenty possible answers, including ten affirmative answers (●), five non-committal answers (●), and five negative answers (●).

● It is certain
● It is decidedly so
● Without a doubt
● Yes definitely
● You may rely on it

● As I see it, yes
● Most likely
● Outlook good
● Yes
● Signs point to yes

● Reply hazy, try again
● Ask again later
● Better not tell you now
● Cannot predict now
● Concentrate and ask again

● Don't count on it
● My reply is no
● My sources say no
● Outlook not so good
● Very doubtful
"""

"""
My Logic:
This is YES-NO question. so there is one question.
say question = 'Do you love cricket?'

Now suppose intially answer = ''

Then after asking each time we get reply out of 20 possible combination. 
Main catch is this happen randomly

so answer is based on random option between 1 and 20.

I can assign number to each option between 1 and 20.

then generate random number between 1 and 20 and accordingly, we will get answer stored in it.

-- if question is empty string, then ask user to provide their questions.

-- introduce user name and include them as User asks question: question.

-- make sure if user name is empty then print only question: question.
"""
import random

question = "Do you love cricket?"
answer = "" #intially it is empty string
user = 'Manish'
random_number = random.randint(1, 20) # generate random number

#print(random_number) # check for random number being generated

if random_number == 1:
    answer  = "It is certain"
elif random_number == 2:
    answer  = "It is decidedly so"
elif random_number == 3:
    answer  = "Without a doubt"
elif random_number == 4:
    answer  = "Yes definitely"
elif random_number == 5:
    answer  = "You may rely on it"
elif random_number == 6:
    answer  = "As I see it, yes"
elif random_number == 7:
    answer  = "Most likely"
elif random_number == 8:
    answer  = "Yes"
elif random_number == 9:
    answer  = "Signs point to yes"
elif random_number == 10:
    answer  = "Better not tell you now"
elif random_number == 11:
    answer  = "Cannot predict now"
elif random_number == 12:
    answer  = "Concentrate and ask again"
elif random_number == 13:
    answer  = "Don't count on it"
elif random_number == 14:
    answer  = "My reply is no"
elif random_number == 15:
    answer  = "My sources say no"
elif random_number == 16:
    answer  = "Outlook not so good"
elif random_number == 17:
    answer  = "Very doubtful"
elif random_number == 18:
    answer  = "Outlook good"
elif random_number == 19:
    answer  = "Reply hazy, try again"
elif random_number == 20:
    answer  = "Ask again later"
else:
    answer = 'Error'


print("----------------------------------------\n")

if question == '':
    print('Kindly ask YES-NO question to try your luck.')
else:
    if user == "":
        print("Question: ", question)
    else:
        print(user ,"asks question: ", question)
    print("Magic 8-Ball's answer: ", answer)

print("\n------------End of output------------")
