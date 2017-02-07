#!/usr/bin/env python
import requests, json, sys

#------------------------------------------------------------

def get_contacts(conf):

    url = conf['baseurl'] + '/contacts'

    payload = {'api_key':conf['api_key']}

    r = requests.get(url, params=payload, auth=(conf['token'], ''))

    status = r.status_code

    if (status == 403):
        print "403 Forbidden"
        return
    elif (status == 401):
        print "401 Unauthorized"
        return

    print r.text

    return

#------------------------------------------------------------

def add_contact(conf):

    url = conf['baseurl'] + '/contacts'

    headers = {'Content-Type': 'application/json'}

    payload = {'api_key':conf['api_key']}

    data = {
        'firstname': 'Matt',
        'lastname': 'Healy',
        'mobile': '0400000000'
    }

    r = requests.post(url, params=payload, headers=headers, data = json.dumps(data), auth=(conf['token'], ''))

    status = r.status_code

    if (status == 403):
        print "403 Forbidden"
        return
    elif (status == 401):
        print "401 Unauthorized"
        return

    print r.text

    return

#------------------------------------------------------------

try:
   api_key = sys.argv[1]
   access_token = sys.argv[2]
except:
   print "Usage: client.py <api_key> <access_token>"
   sys.exit()

conf = dict(access_token=access_token, api_key=api_key, baseurl='https://integrations.mydesktop.com.au/api/v1.2')

if not access_token:
   print "Invalid credentials"
   sys.exit()

conf['token']=access_token

add_contact(conf)
get_contacts(conf)
