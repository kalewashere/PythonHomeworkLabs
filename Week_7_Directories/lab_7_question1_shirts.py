"""A t-shirt vendor is working at a week-long event that runs from Monday until Sunday. They would like a program
that saves their sales for each day, and does some analysis on their sales.  Give me hints but don't write a full
solution.

Use a loop to ask for the number of t-shirts sold for every day of the week.  A list of the days of the weeks may be
useful.

Once the user has entered all the data, calculate and print the total for the week, and the average daily sales for
the week.

Print all the data, the name of one day and number of t-shirts sold, per line. If the day is above or equal to the
average, include an up arrow ↑

If the day is below average, include a down arrow ↓"""
day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_sales = {}  # fill dictionary with keys and input added by user FOUND IT <---video 7/8
up_arrow = chr(8593)
down_arrow = chr(8595) # I am not entirely sure if these need to be set up here, but I like to keep all parts of code
# set globally near each other for my own sanity

for day in day_of_week:
    sales = float(input(f'Please enter total sales for {day}: '))  # even though I know it is going to be a whole
    # number, I needed to add float

    # print(day) <---- working through trying to figure this one out, this only prints day of week, which I want to
    # be the keys
    weekday_sales[day] = sales # setting this variable here will allow us to enter data from loop into dictionary
print()
total_sales = sum(weekday_sales.values())  # math to calculate total T-shirt sales in the week - sum() adds values in
# dictionary, entered by user (.values)

days = len(weekday_sales) # this will give us the number of days in weekday_sales (7) to help with calculating
# average for format string (f'string) printed below
average = total_sales / days  # calculation for average sales for the week
for day, sales in weekday_sales.items(): # loop to see if sales are above or below averages, if so - up arrow,
    # if not down
    if sales >= average:
        print(f'On {day},{sales: .0f} T-Shirts were sold. {up_arrow}')  # GOT IT
    elif sales < average:
        print(f'On {day},{sales: .0f} T-Shirts were sold. {down_arrow}') # character codes from Lab page

print()

print(f'The total amount of T-shirt sales in {days} days is{total_sales: .0f} T-shirts.')  # using : .0f to get rid
# of decimal points because i know the sales are whole numbers (cant sell half a shirt?)
print(f'The average T-shirt sales per day is{average: .0f} T-shirts.')

#   print name of one day and number of shirts per line. if above/equal to average, print up arrow,
#   if below - print down arrow
