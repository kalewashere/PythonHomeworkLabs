# final updated version of Lab 9!
# Over the past few weeks, I spoke with my friends Connor and Brendon. Connor is more
# familiar with other coding languages, but helped me understand how setting variables in functions worked,
# and helped me realize I didn't need to set variables outside a def function. Brendon works with Python alot,
# and wrote a program recently for his kickball team. His program would take information provided by players and
# determine which position to put them in based on their preferences. I took a look at his program, which was full of
# def functions. He walked me through how it was written, and his choices for organization. After speaking with them
# and just talking shop with them, AND with the edits Clara provided to my turned in lab, I know feel much more
# confident in my understanding of defining a function, format strings and spacing, as well as organization and where
# I can place different parts of the code.
# cheers!!
import requests


def main():
    north_url = 'https://svc.metrotransit.org/NexTrip/17940?format=json'
    south_url = 'http://svc.metrotransit.org/NexTrip/17928?format=json'

    print_bus_table(north_url, 'Northbound')
    print_bus_table(south_url, 'Southbound')  # Python auto-formatted these bus_direction text boxes - I like that it
    # did that and I think I get why it did, it helps me AND the program understand where and what bus_direction is
    # being set and called from


def print_bus_table(bus_url, bus_direction):
    response = requests.get(bus_url).json()
    departures = response['departures']
    print(f'{bus_direction} buses arriving outside of Minneapolis College are scheduled as follows: ')
    print(f'Route      Time        Bus Description')  # placed outside of loop, so it will only print once while the
    # function is called.
    for bus_info in departures:
        route = bus_info['route_id']
        time = bus_info['departure_text']
        description = bus_info['description']
        print(f'{route:<10} {time:<11} {description}')  # format strings and string spacing editors to make the tables
        # more visually appealing


main()  # main() must be placed at end to call main function
