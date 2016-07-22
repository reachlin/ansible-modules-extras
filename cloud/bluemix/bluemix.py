#!/usr/bin/python

import argparse
import requests
# some issue with stage1 api
# http://stackoverflow.com/questions/32650984/why-does-python-requests-ignore-the-verify-parameter

parser = argparse.ArgumentParser(description='Bluemix connection test')
parser.add_argument('-t', dest='target', required=True, help='Bluemix Zone: us, eu, stage', choices=['us', 'eu', 'stage'], default='us')
parser.add_argument('-u', dest='username', required=True, help='Bluemix user name', default='lincai@cn.ibm.com')
parser.add_argument('-p', dest='password', required=True, help='Bluemix user password')
parser.add_argument('-o', dest='org', required=True, help='Bluemix organization name', default='lincai.cn.ibm.com')
parser.add_argument('-s', dest='space', required=True, help='Bluemix space name', default='dev')
parser.add_argument('-d', dest='debug', help='print debug information', action='store_true')

args = parser.parse_args()


username = args.username
password = args.password
org = args.org
space = args.space

blumix_host = "ng.bluemix.net"
if args.target == 'eu':
  blumix_host = "eu-gb.bluemix.net"
elif args.target == 'stage':
  blumix_host = "stage1.ng.bluemix.net"

url = 'https://login.%s/UAALoginServerWAR/oauth/token' % blumix_host
headers = {'authorization': 'Basic Y2Y6',
          'accept': 'application/json;charset=utf-8',
          'content-type': 'application/x-www-form-urlencoded;charset=utf-8'}
payload = {'username': username,
          'password': password,
          'grant_type': 'password'}
r = requests.post(url, headers=headers, data=payload)

if r.status_code == 200:
  token = r.json()['access_token']
  url = 'https://api.%s/v2/organizations' % blumix_host
  params = {'q': 'name:'+org}
  headers = {'authorization': 'Bearer '+token,
          'accept': 'application/json;charset=utf-8'}
  r = requests.get(url, headers=headers, params=params)

  if r.status_code == 200:
    rtn = r.json()
    if rtn['total_results'] == 1:
      rtn = rtn['resources'][0]['metadata']
      org_guid = rtn['guid']
      print 'org guid: %s' % org_guid
      url = 'https://api.%s/v2/organizations/%s/spaces' % (blumix_host, org_guid)
      params = {'q': 'name:'+space}
      r = requests.get(url, headers=headers, params=params)
      if r.status_code == 200:
        rtn = r.json()
        if rtn['total_results'] == 1:
          space_guid = rtn['resources'][0]['metadata']['guid']
          print 'space guid: %s' % space_guid
          url = 'https://containers-api.%s/v3/containers/json' % blumix_host
          headers = {'X-Auth-Token': token,
                    'accept': 'application/json;charset=utf-8',
                    'X-Auth-Project-Id': space_guid}
          r = requests.get(url, headers=headers)
          if r.status_code == 200:
            print 'containers:'
            print r.json()
          else:
            print r.text
        else:
          print rtn
      else:
        print r.text
    else:
      print rtn.json()
  else:
    print r.text
else:
  print r.text