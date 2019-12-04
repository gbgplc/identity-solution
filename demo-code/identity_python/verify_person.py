#!/usr/bin/python3

import requests
import json
import pickle
import sys

fname='token_store.pkl'
fname2='id_store.pkl'

# ********** configuration ******************
with open('config.txt') as json_file:
  cfg=json.load(json_file)
  gbg_url=cfg['gbg_url']
  pathroot=cfg['pathroot']
  journey_id=cfg['journey_id']
  journey_version=cfg['journey_version']
customer_reference="44820bbd-8b4d-4645-b8e3-4d2c3b9ba5d0"
verify_person_ep="/verify/people/v3/person"
verify_person_id_ep="/verify/people/v3/"

# ****** verify person terms to query ********
title="Mr"
firstName="TED"
middlename1="JIM"
lastname1="KIRK"
gender="MALE"
birthdate="1989-02-19"
addressline1="22 BAKER STREET, LONDON, SE1 2TJ"
residentfrom="2012-1-01"
residentto="2016-04-22"
phonetype1="HOME"
phonenumber1="+447123456999"


# ********* read stored GBG access token ************
with open(fname, 'rb') as f:
  idp_access_token, gbg_access_token = pickle.load(f)


# ************** verify person **************
headers={"Content-Type": "application/json",
         "journey-id": journey_id,
         "journey-version": journey_version,
         "customer-reference": customer_reference,
         "cleanse-address": "false",
         "Authorization": "Bearer "+gbg_access_token}
payload={
         "title": title,
         "firstName": firstName,
         "middlenames": [middlename1],
         "lastnames": [lastname1],
         "gender": gender,
         "birthdate": birthdate,
         "addresses": [
            {"type": "CURRENT",
             "address": {"lines": [addressline1]},
             "resident":{"from": residentfrom, "to": residentto},
             "enrichments": {} }
         ],
         "phones":[
            {"type": phonetype1, "number": phonenumber1}
         ]
        }

if (len(sys.argv)>1):
  # we have a person-id parameter
  with open(fname2, 'rb') as f:
    person_id = pickle.load(f)
  #print("person-id is "+person_id[0])
  r=requests.post(url=gbg_url+verify_person_id_ep+person_id[0], data=json.dumps(payload), headers=headers)
else:
  r=requests.post(url=gbg_url+verify_person_ep, data=json.dumps(payload), headers=headers)

print("headers:")
print(json.dumps(dict(r.headers), indent=2))

print("body:")
api_resp=json.loads(r.text)
print(json.dumps(api_resp, indent=2))

verification=api_resp['verification']
print("verification result is ", verification['result']['state'], "score: ", verification['result']['score'])

combined=api_resp['combined']
print("combined is ", combined['decision'])

# ******* save the person-id *************
person_id=r.headers['person-id']
with open(fname2, 'wb') as f:
  pickle.dump([person_id], f)
print("saved person-id to %s"%fname2)

