"""Metro Transit has an API with live bus information. These URLs return upcoming bus departures for the two bus
stops outside Minneapolis College on Hennepin Avenue at 16th Street. The numbers in the URLs are Metro Transit stop
ID numbers.

North from Hennepin Avenue and 16th Street: http://svc.metrotransit.org/NexTrip/17940?format=json

South from Hennepin Avenue and 16th Street: http://svc.metrotransit.org/NexTrip/17928?format=json

For this program, make two requests, one to each of these API URLs. Process the responses and print two tables,
one for each stop. Each table should have the bus number, route, and arrival time, for all of the next buses at both
of these stops.

You will need to get the route_id, (the bus number) the departure_text, (a human-readable time), and description (a
description of the bus route) from the response, for each bus.

Use string formatting and alignment to display the data in columns in the table. How to do alignment: Strings -
f-strings, decimal places, aligning

Use a function or functions; or a loop; so you don't have to write almost exactly the same code twice.

Hint: when you process the response, the first step is to understand the structure of the response. For example,
do you have a dictionary, and you need to get data by a key? Or do you have a list, so you'll start by looping over
the list?  Are there more dictionaries inside? Try printing the response or viewing it in your browser to see."""
import requests  # only need to type this once if more than one variable used as long as they are set

nb_response = requests.get('https://svc.metrotransit.org/NexTrip/17940?format=json').json()
sb_response = requests.get('http://svc.metrotransit.org/NexTrip/17928?format=json').json()

# different data to be expected due to live bus times - this will change whenever program is run
# print(nb_response)  # prints northbound response data
# sb_response = requests.get(sb_url).json()  # this calls .json from south bound url to convert to python code - second
# request
# print(sb_response)  # prints southbound response data

# we need value for departures
nb_departures = nb_response['departures']
sb_departures = sb_response['departures']

print(f'Route      Time        Bus Description')
for bus_info in nb_departures and sb_departures:
    route = bus_info['route_id']
    direction = bus_info['direction_id']
    time = bus_info['departure_text']
    description = bus_info['description']
    corrected = description.replace('via', ' / ')
    print(f'{route:<10} {time:<11} {corrected}')


# nb_departures = nb_response['departures']
# sb_departures = sb_response['departures']
# bus_info = nb_departures and sb_departures


# print('Route Time Bus Description')
#
#        if direction == 'NB':
#            print('Northbound buses arriving outside of Minneapolis College Campus are scheduled as follows: ')


# this is a list of dictionaries
# each dictionary has data about one bus

# we can only access data by index - a number
# or by using a loop

# for bus_info in departures_list:  # this will print each dictionary, per line - alot to look at in output - yeesh
#    route = bus_info['route_id']
#    direction = bus_info['direction_text']
#    time = bus_info['departure_text']
#    description = bus_info['description']
#    stop = bus_info['stop_id']

#    terminal_id = bus_info['terminal']   why is this breaking the code?
#    print(f'{route:<1} {direction:<14} {time:<17} {description}') -> use this for final code in Lab
# hint - check weather.py in lecture code for set up on table for lab question -> use this as ref for Lab


# if sb_response:
# route = sb_response['route_id']
# time = sb_response['departure_text']
# description = sb_response['description']
# print('Southbound buses arriving on Hennepin Avenue outside of Minneapolis College Campus')
# print()
# print(f'{route:<10} {time:<11} {description}')

# TODO - turn this partial Lab in and ask for help 4/7/24 - I have been working on this all week and I cannot figure
#  it out. Thinking maybe a function would help best - turning in what I have and will got to office hours or ask a
#  friend to help me with it. Unable to get the bus lists to separate to north / south, unable to get northbound and
#  southbound messages to print, unable to use multiple urls - super lost and brain dead at this point. need to revisit