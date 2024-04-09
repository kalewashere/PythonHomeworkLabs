"""this was a test program - used to dump ideas and practice code to not overwhelm myself in lab"""

import requests

url1 = 'https://svc.metrotransit.org/NexTrip/17940?format=json'
url2 = 'http://svc.metrotransit.org/NexTrip/17928?format=json'

nb_response = requests.get(url1).json()
sb_response = requests.get(url2).json()

departures = nb_response['departures'] and sb_response['departures']

# sb_departures = sb_response['departures']

for bus_info in departures:
    route = bus_info['route_id']
    time = bus_info['departure_text']
    direction = bus_info['direction_text']
    description = bus_info['description']
    if nb_response in departures:
        print('North')
    elif sb_response in departures:
        print('South')
    print(f'{route:<10} {time:<11} {description}')


#    print('Northbound buses')
#   print(f'Route      Time        Bus Description')

#   print('Southbound buses')
#   print(f'Route      Time        Bus Description')
