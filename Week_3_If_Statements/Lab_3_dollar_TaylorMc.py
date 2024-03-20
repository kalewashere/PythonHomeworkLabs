"""Write a program that asks the user how many cents (penny coins) they have.

If they have less than 100 cents, print the message 'you have less than a dollar'.
Or, the user could have exactly 100 cents, so print the message 'you have exactly one dollar'
Or, they could have more than 100 cents, so print the message 'you have more than one dollar'
"""
number_of_cents = int(input('How many cents do you have? '))


def convert_pennies_to_dollars(number_of_cents):  # def used here to 'create function'. I was wondering how we got
    # programs
    pennies = number_of_cents % 100  # 100 pennies in a dollar
    dollars = number_of_cents // 100  # divided by 100 to get amount in dollars
    print(f"If you have {number_of_cents} pennies, that means you have exactly ${dollars}.")  # i can only get
    # the def program to run IF i type the convert_pennies_to_dollars up here
    # i have an idea
    # the idea was to
    # move code farther up, but i cannot get the message to print without setting the number_of_cents and not what
    # the user input
    # OKAY GOT IT TO WORK - although I am not sure what 'f'' marker is called, but i have noticed it allows me
    # to use words and numbers without the + or extra '' I am also not 100% sure how that math works - I noticed if i
    # entered {pennies}, I would get a random 0 after the initial 600 from user input. I was reading that % operator
    # is also used for remainders and such. A way to calculate cents, perhaps?
    # I added a line of code at the bottom that finally got the message to print
    # after running 'pass' command was automatically added as a placeholder for python. I read it does nothing once
    # it runs, so i removed it to add the convert_pennies_to_dollars


if 100 > number_of_cents >= 1:  # this was an auto-correction from python. interesting, I was playing with if/and
    # statements and couldn't figure it out.
    # I ended up with:
    # if pennies < 100 and >= 1:
    #   print('You have less than one dollar.') i wanted to do this so that if someone entered '0' when prompted, they
    #   would get a different message. Interesting how code can be shortened. I am understanding the way pyhton changed
    #   it for me.
    # code looks much MUCH neater this way. Good to know how to get that point first, though!
    print('You have less than a dollar.')  # this code is conditional
elif number_of_cents == 100:
    print('You have exactly one dollar.')
elif number_of_cents >= 100:
    print('You have more than one dollar.')
elif number_of_cents == 0:
    print('You have...no money.')  # feels extremely satisfying to wonder if I can experiment with code while learning
    # it, and once it clicks and works
# (Bonus question, +3 points: extend your program to check if the user has an exact number of dollars in cents
# (penny coins), for example 100 or 300 or 700 pennies. Print a message if so. Hint: look up the modulo % operator. It's
# covered in Chapter 1 of the textbook.)
# for this question I searched '% modulo operator' and found realpython.com/python-modulo-operator/#how-to-convert-units
# I used this site to about the % operator with int and float numbers, which I do believe I am sort of understanding.
# they have examples on their site, but their conversion of units is inches to feet, I wanted to find an example that
# didn't use the same or similar units, so I can try it myself.
convert_pennies_to_dollars(number_of_cents)
