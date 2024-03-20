# Article I, Section 3 of the United States Constitution sets out three qualifications for senators:
# (1) they must be at least 30 years old,
# (2) they must have been citizens of the United States for at least the past nine years,
# and (3) they must live in the state they seek to represent at the time of their election. Write a program that asks
# the user four questions:
# 1. The state they want to be a senator in,
# 2. Their age, as an int number,
# 3. If they have been a citizen of the US for at least 9 years.
# 4. The state they currently live in.(to be eligible, this needs to be the same as the state they want to be the
# senator of). Think about how you'll ask the user for this information.

state = input('Which State would you like to represent? ')  # not a float or int
age = int(input('How old are you, in years? '))  # int number for whole years
citizen = float(input('How long have you been a US citizen, in years? ')) # float, just in case users are at 8.5 or something
current_state = input('Which state do you currently reside in? ')  # not a number either
# Print one message telling the user if they are eligible to be a senator or not.
if state == current_state and age >= 30 and citizen >= 9:  # if these conditions are met, users are greated with a congrats
    print('Congratulations! You are eligible.')
elif state != current_state and age < 30 and citizen < 9:  # buuuut if not, put this elif here to tell the program to
    # run this first to see if these conditions have been met. if so, it lets the users know why they are not eligible.
    print('You are not eligible because you must reside in the state you wish to represent, you are too young, and you have not lived in the US long enough. ')
else:   # used this else to let the program know there are other options too; some stored variables may qualify the
    # users for eligibility, but if one does not match the if statement above, the user is provided with an individual
    # reason as to why on each line.
    print('Sorry, you are not eligible.')
    if state != current_state:
        print('You are not eligible because you live in a different state. ')
    if age < 30:
        print('You are not eligible because you are too young.')
    if citizen < 9:
        print('You are not eligible because you have not been a citizen of the US for long enough.')

# Optional extra question +3 points: extend your program to print the specific reasons why the person is not eligible.
# this extra question took me a bit to figure out. I tried putting elifs and doing different ifs under the else section
# at first, but then realized i needed the program to recognize the full sentence first. It will then move down to the
# else statements. I am wondering (and will continue to fiddle with) getting the program to have more complete answers
# with the else portions. The person is old enough, but not in the same state but has not been a citizen of the US for 9
#  years: 'You are not eligible due to residing outside of desired state of representation and you have not been a
# citizen for at least 9 years' - something like that? I suppose I could use and statements, seems a bit tedious though?