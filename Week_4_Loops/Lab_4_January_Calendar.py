"""Write a program that uses a loop prints the date for every day in January. So, your program's output will look like
this. Make sure the first date is "January 1" and the last date is "January 31".
You'll only need one print statement - don't write 31 print statements! """

# if we need to something a specific number of times, for loops are best
# this prints numbers 0-10 and we need 1-31
# variable name needs to be more specific, describe data it is representing
# needs to have the word january before the number
for day_of_month in range(31):  # loops numbers 0 - 30, 0 counts as a number
    day_to_print = day_of_month + 1
    if day_to_print == 1 or day_to_print == 21 or day_to_print == 31:
        print(f'January {day_to_print}st')
    elif 20 >= day_to_print >= 4:
        print(f'January {day_to_print}th')
    elif day_to_print == 2 or day_to_print == 22:
        print(f'January {day_to_print}nd')
    elif day_to_print == 3 or day_to_print == 23:
        print(f'January {day_to_print}rd')
    elif 30 >= day_to_print >= 24:
        print(f'January {day_to_print}th')
# so if i add a note will it turn red
# no it wont i dont understand git
    # f string can write this way to make it neater - set in variable to tell program to do this
    # before print message

# print('January ' + str(day_to_print))   variable changed to more specific describer, added + 1 to get full range
# bonus question : i tried so many things to get this to work properly. I tried looking up something to help me
# identify the last digit in variable, but I was not able to understand it, so I ended up back at if/elif statements. I
# also needed a quick refresh on and vs. or. once I got those reminders I was able to finally pin it down. I enjoy f
# strings and the elif 20 >= day_of_print >= 4 format much more. It just clicks better in my head update 2/4 - I did
# ask a pal about this, he took a coding course last fall and I wanted to get his input. He brought up modulo,
# which i do remember doing a bit of research on before BUT he explained it to me in a way that clicked,
# and he helped me understand how the remainders worked and what it can do for a program. I'm still trying to
# understand the operator itself, but I want to return to this at some point to see how i can apply it as well. I'm
# wondering if it looks neater or more compact than what i came up with~
