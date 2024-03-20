# Ask the user for the number of times they rode the bus last month (what data type do you need to convert the input to?)
monthly_rides = int(input('How many times did you ride the bus last month? ')) # save in a variable (int for whole
# number, stored)
# Ask the user for the cost of one bus ride (what data type do you need to convert the input to?) and
cost_per_ride = float(input('How much was the cost of each ride?')) # save in another variable (float for
# non-whole numbers, stored)
print('Thank you.')  # for "politeness"
# Calculate the total cost of riding the bus last month.
# Multiply the two variables and store the result in a new variable.
monthly_cost = cost_per_ride * monthly_rides # mathing
# Print the number of rides, the cost of one bus ride, and the total cost for the user.
print() # for spacing
print('Travel Expenses') # title
print('Total number of bus rides, per month: ' + str(monthly_rides)) # string to put numbers with works
print('Cost of each bus ride: $' + str(cost_per_ride))
print('Monthly cost of riding the bus: $' + str(monthly_cost))
print() # for spacing
# Convert numeric variables to strings.
print('You rode the bus ' + str(monthly_rides) + ' times last month. One bus ride costs $' + str(cost_per_ride) + '. Your total cost was $' + str(monthly_cost) + '.') # I need the period