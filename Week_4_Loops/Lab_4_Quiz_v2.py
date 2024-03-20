# same quiz as before, ,ake these edits
# 1 - only let the user have 3 attempts
# 2 Count how many attempts it took the user to get the answer right - may need another variable
# 3 if user gets it right before they run out of attempts, tell them how many attempts it took
# 4 if user runs out of attempts, print a message with the correct answer
answer = input('What is the capital of Wisconsin? ')
attempts_allowed = 2
total_attempts = 0
attempts_remaining = attempts_allowed - total_attempts

while answer.lower() != 'madison' and total_attempts < 2:  # telling the program to run these instances while the
    # conditions are met
    attempts_remaining = attempts_allowed - total_attempts # math for variable used in sentence sequence - i struggle
    # this part specifically
    total_attempts = total_attempts + 1 # needed to give the variable a bit a direction as the attempts are...attempted
    print(f'{answer} is incorrect. You have {attempts_remaining} attempt(s) remaining.') # using f strings is my
    # preferred way to string. It helps me with organization and seeing the information in a different way.
    answer = input('What is the capital of Wisconsin? ')  # asking user to input answer again, until attempts remaining
    # = 0
    #  ---if attempts_remaining == 0: print(f'You have {attempts_remaining} attempt(s) remaining. The correct answer
    # is "Madison".') --- I was trying to get this if statement to work off of the while command, but i was not able to
    # understand that and need to review the videos a bit more.

if answer.lower() == 'madison':
    print(f'Correct! It took you {total_attempts + 1} attempts(s).')
else:
    print(f'You have {attempts_remaining - 1} attempt(s) remaining. The correct answer is "Madison".') # used an else
    # with attempts -1 to tell the program that i want it to print a sentence explaining there are no attempts left.
    # I was not able to get the math to work out as well as i wanted it to, as it would always print 1 attempt left
    # when there were '0'. The else made it so attempts_remaining - 1 (0) would trigger the program to input the
    # message the while statement above may have had something to do with it - i do want to re-watch the lecture code
    # videos in their entirety to really wrap around this. So while statement about is running for < 3,
    # once that value hits 0 this else command will trigger

# TODO pause here for the night and come back when you re watch the videos and get a break  - re-open lecture_code:
#  quiz_practice with this lab
# update 2/4 - re-watched a few videos (thanks clara) on while loops and if statements.
# I had a hard time remembering where to place ifs and when to use an else.
# i was able to get the code to work with trail and error, moving if and else, and switching between if and while loops.
# i wanted to try and figure out a way to get the if statement to work as well, but i need more review before i try
# again. There are various notes and practice sections i made while trying to figure this one out, and the are labeled
# practicev2 and quizpraticev2 in lecture notes. Again, a lot of trial and error with back stepping in review here.

# scrap and practice code listed here/below:
# while answer != 'madison':
#     total_attempts =
#     print('Sorry, that is not correct. Please try again.')
#     answer = input('What is the capital of Wisconsin? ')

    # if answer.lower() == 'madison':
    #     print('Correct!')
