"""PS: I am going to talk with Python Interpreter (name it Jarvis) in its language and then rather than thinking like programmer, I would like to give it a human touch.
Doing this way so that I would be more indulged in learning like communication. Do not assume it would be formal and informative. Haha. I hope Jarvis will ignore this comment and that is how I learned what comment is."""

#Jarvis please greet the world by saying 'Hello world' in terminal
print('Hello World!')


#Jarvis create a variable meal and update to reflect each meal of the day before you show it

#morning
meal = 'muffin'
print('morning:',meal)

#afternoon
meal = 'rice'
print('afternoon:', meal)

#evening
meal = 'biryani'
print('evening:', meal)


"""
Jarvis I recently watched movie and I would like to write review about them
- create 3 variables to store release year, runtime and rating out of 10
- also store values in them.
- I want rating as float: decimal
"""
release_year = 2024
runtime = 120
rating_out_of_10 = 9.4

"""
Jarvis I heard you are good in calculation.
- tell me output of 25 * 68 + 13 / 28
"""
print(25 * 68 + 13 / 28)

"""
I have decided to get into quilting. 
For my first quilt, I am thinking it to be 8 square wide and 12 square long.
- create 2 variables to store them.
- find and tell me the number of squares I need in total for my first quilt
"""
quilt_width = 8
quilt_length = 12

square_count = quilt_width * quilt_length

print('Squares in my first quilt: ', square_count)

"""Jarvis I guess I need more material, Let's keep quilt only 8 square long.
Now tell me how many squares I need """

quilt_length = 8

print("Squares count in my first quilt after review: ", square_count)

"""
OOPS! Jarvis I got wrong answer. You should I have told me to recalculate square count as you are storing the old value.
"""
square_count = quilt_length * quilt_width
print("Squares count in my first quilt after review: ", square_count)

"""
I am thinking to make square quilt only. so we do not need  2 variables.
- create one variable for side
- tell me the square count of 6x6 quilt
EASY YEAH :)
- yes! I am suggesting to go like this 6^2 but in your language.
"""

quilt_side = 6
square_count = quilt_side ** 2
print("Squares count in my first square quilt: ", square_count)

"""
GREAT! Now our square quilt is popular in market.
6 people have requested 6 quilts.
- tell me how many total tiles I need
"""
customer_count = 6
quilt_requested_count_per_customer = 6
total_quilt_requested = customer_count * quilt_requested_count_per_customer
quilt_side = 6
square_count = (quilt_side ** 2) * total_quilt_requested 
print('Total square needed for requested quilts by ', customer_count, 'customers are: ', square_count )


"""
Jarvis! I am opening an online shop and I would like to offer discount.
- Every 11th customer will get 11% off of their next order.
For your ease
- Order numbers that are divisible by 11 will get coupon.
Here comes order #263
- create a variable to store the remainder of order 263 upon division by 11
- create another variable to store whether order gets coupon or not
"""
qualifier_constant = 11 
order_no = 263

order_remainder = order_no % qualifier_constant
print("Customer place for order number - ",order_no," is : ", order_remainder) 

order_263_coupon = "no"

"""
I see order_remainder is 10 and it should be 0 to be considered as every 11th customer.

let's check for another order no.
"""
order_no = 264

order_remainder = order_no % qualifier_constant
print("Customer place for order number - ",order_no," is : ", order_remainder) 

order_264_coupon = "yes"


"""
Jarvis, I have fun exercise for you. Help me to do string concatenation to
create a short paragraph from them.
"""
string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

message = string1 + string2 + string3 + string4 + string5 + string6
print(message)

"""
Jarvis, you never told me I can use Plus Equals concept.
so everytime I calculate total of something. I do not need to recalculate from start.
I can keep a grand total and update it when I have added something further.

Also I can use it for string concatenation.
"""

#see Jarvis I amazing this PLUS EQUAL can be.

linked_caption = "#CGIACADEMIA "
linked_caption += "#dailychallenge "
linked_caption += "#pythonista "

print('my linkedin caption: ',linked_caption)

"""
Okay here is another amazing case:
I am doing online shopping
- first I found sneakers for 50.00
- then after 10 mins I found fun books for 39.00
- just before checkout I found sweater for 100.00

- obviously in the beginning total price I need to pay is 0, so create a variable to store it and
- tell me total price I paid after checkout.
- however show me the use of PLUS EQUALS by calculating total price each time I found new item.
"""

total_price = 0
sneakers = 50.00

total_price += sneakers

fun_books = 39.00
total_price += fun_books

sweater = 100.00
total_price += sweater

print("Total Price after checkout: ", total_price)


"""
Jarvis, I know you are poet like famous influencer these days on instagram
and you want to post 4 lines poetry. However, you want the formatting like real poetry with proper spacing and line indentation: exactly I gave as input should be represented in terminal.

I know we can do that with multi-line string. 
"""
lines = """
Love of my life!
    Take a knife.
            Keep it tight.
    I am so bright.
Isn't it right?
"""
print("poetry with line indentation in terminal: ", lines)
