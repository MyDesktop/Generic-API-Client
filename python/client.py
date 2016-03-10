#!/usr/bin/env python
import requests, json, sys

#------------------------------------------------------------

def get_contacts(conf):

    url = conf['baseurl'] + '/contacts'

    headers = {'Content-type': 'application/json'}

    payload = {'api_key':conf['api_key']}

    r = requests.get(url, params=payload, headers=headers, auth=(conf['token'], ''))

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

conf = dict(access_token=access_token, api_key=api_key, baseurl='https://integrations.mydesktop.com.au/api/v1.1')

if not access_token:
   print "Invalid credentials"
   sys.exit()

conf['token']=access_token

get_contacts(conf)
