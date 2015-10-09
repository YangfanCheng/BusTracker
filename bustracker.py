import urllib
import sys
import webbrowser
from xml.etree.ElementTree import parse

njit_latitute = 40.7420
njit_longitude = -74.178078

def distance (lat1, lat2):
    return 69*abs(lat1 - lat2)

def monitor():
    dis_list = []
    bus_list = {}
    target_id = ""
    target_lat = ""
    target_lon = ""
    bus = sys.argv[1]
    u = urllib.urlopen( 'http://mybusnow.njtransit.com/bustime/map/getBusesForRoute.jsp?route=%s'%bus)
    doc = parse(u)
    json = '{"buses":['
    for bus in doc.findall('bus'):
        route = bus.findtext('fs')
        busid = bus.findtext('id')
        lat = float(bus.findtext('lat'))
        d = bus.findtext('dd')
        dis = distance(lat, njit_latitute)
        #append to the dictionary
        bus_list[busid] = dis
        dis_list.append(dis)
        json = json + '{"id":' + str(busid) + ',"distance":' + str(dis) + ',"des":"' + d +'","route":"' + route + '"},'
    json = json.rstrip(',') + '],'
    min_dis = min(dis_list);
    for busid in bus_list:
        if bus_list[busid] == min_dis:
            target_id = busid
            break
    for bus in doc.findall('bus'):
        if bus.findtext('id') == target_id:
            target_lat = float(bus.findtext('lat'))
            target_lon = float(bus.findtext('lon'))
    json += '"target":{"lat":' + str(target_lat) + ',"busid":' + str(target_id) + ',"lon":' + str(target_lon) + '}}'
    print json
            
        
monitor()
