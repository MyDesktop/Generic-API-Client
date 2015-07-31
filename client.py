#!/usr/bin/env python
import requests, json, sys

#------------------------------------------------------------

def get_new_token(conf):

    tokenurl = conf['baseurl'] + '/token'

    headers = {'Content-type': 'application/json'}

    payload = {'api_key':conf['api_key']}

    r = requests.get(tokenurl, params=payload, headers=headers, auth=(conf['username'], conf['password']))

    status = r.status_code

    if (status == 403):
        print "403 Forbidden"
        return None,None
    elif (status == 401):
        print "401 Unauthorized"
        return None,None

    json = r.json()

    token = json['token']
    refresh_token = json['refresh_token']

    print token

    return token,refresh_token

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
   username = sys.argv[1]
   password = sys.argv[2]
   api_key = sys.argv[3]
except:
   print "Usage: client.py <username> <password> <api_key>"
   sys.exit()

conf = dict(username=username, password=password, api_key=api_key, baseurl='https://integrations.mydesktop.com.au/api/v1.0')

token,refresh_token = get_new_token(conf)

if not token:
   print "Invalid credentials"
   sys.exit()

conf['token']=token
conf['refresh_token']=refresh_token

get_contacts(conf)

