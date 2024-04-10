"""Starting from a clean slate - comments got overwhelming in first attempt. Going to try some functions here to see
if those will help in this process - ok so couldnt get a function to work - need to review"""
import requests

url1 = 'https://svc.metrotransit.org/NexTrip/17940?format=json'
url2 = 'http://svc.metrotransit.org/NexTrip/17928?format=json' # when i tried to list urls together it caused issues - not sure if i am setting that up correctly or if that only works for image urls

nb_response = requests.get(url1).json() # variables might be a little to simple for urls
sb_response = requests.get(url2).json()

nb_departures = nb_response['departures']
sb_departures = sb_response['departures'] # accessing list of dictionaries to gather data needed for variables

print('Northbound buses buses arriving outside of Minneapolis College are scheduled as follows: ') # placed these before loop so they would show up first
print('')
print(f'Route      Time        Bus Description')

for nb_bus_info in nb_departures: # this code is bulky - I tried to do a function so i wouldn't have to write code twice, but i need review on functions because i do not think i grasp it fully
    nb_route = nb_bus_info['route_id']
    nb_time = nb_bus_info['departure_text']
    nb_direction = nb_bus_info['direction_text']
    nb_description = nb_bus_info['description']
    print(f'{nb_route:<10} {nb_time:<11} {nb_description}') # used ':<10' etc for spacing
print('') # print blank lines to separate, printed globally to print outside of loop
print('Southbound buses arriving outside of Minneapolis College are scheduled as follows: ')
print('')
print(f'Route      Time        Bus Description') # format string to align in table
for sb_bus_info in sb_departures:
    sb_route = sb_bus_info['route_id']
    sb_time = sb_bus_info['departure_text']
    sb_direction = sb_bus_info['direction_text']
    sb_description = sb_bus_info['description']
    print(f'{sb_route:<10} {sb_time:<11} {sb_description}')
# todo guessing a while loop would be best here - brb - nope def cant get that to work either
# def northbound(direction):  lines 35 - 41 are left over practice code for functions - need more review
#   if direction in nb_departures and sb_departures == 'NB':
#        print('Northbound')
#    else:
#        print('South')

# def main():
