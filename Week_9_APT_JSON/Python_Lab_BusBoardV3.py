"""Starting from a clean slate - comments got overwhelming in first attempt. Going to try some functions here to see
if those will help in this process - ok so couldnt get a function to work - need to review"""
import requests

url1 = 'https://svc.metrotransit.org/NexTrip/17940?format=json'
url2 = 'http://svc.metrotransit.org/NexTrip/17928?format=json'

nb_response = requests.get(url1).json()
sb_response = requests.get(url2).json()

nb_departures = nb_response['departures']
sb_departures = sb_response['departures']

print('Northbound buses buses arriving outside of Minneapolis College are scheduled as follows: ')
print('')
print(f'Route      Time        Bus Description')

for nb_bus_info in nb_departures:
    nb_route = nb_bus_info['route_id']
    nb_time = nb_bus_info['departure_text']
    nb_direction = nb_bus_info['direction_text']
    nb_description = nb_bus_info['description']
    print(f'{nb_route:<10} {nb_time:<11} {nb_description}')
print('')
print('Southbound buses arriving outside of Minneapolis College are scheduled as follows: ')
print('')
print(f'Route      Time        Bus Description')
for sb_bus_info in sb_departures:
    sb_route = sb_bus_info['route_id']
    sb_time = sb_bus_info['departure_text']
    sb_direction = sb_bus_info['direction_text']
    sb_description = sb_bus_info['description']
    print(f'{sb_route:<10} {sb_time:<11} {sb_description}')
# todo guessing a while loop would be best here - brb - nope def cant get that to work either
# def northbound(direction):
#   if direction in nb_departures and sb_departures == 'NB':
#        print('Northbound')
#    else:
#        print('South')

# def main():
