'''
geocoder
Address To Lat/Lng Single Thread Version
2018/3/20 
'''

import os
import geocoder

AddrSource = []
AddrLists = []


with open('address.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n') 
        '''readline and remove \n '''
        AddrSource.append(line)

def addrquery(address):
    g = geocoder.google(address)
    if g.ok == True:
        return g.latlng
    else:
        pass

for address in AddrSource:
    result = addrquery(address)
    print(address,result)
    AddrLists.append([address,result])
    with open('output.txt', 'w') as z:
        for var in AddrLists:
            z.writelines(str(var)+'\n') 
        '''convert var to str and add \n'''