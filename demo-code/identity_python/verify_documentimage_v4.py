#!/usr/bin/python3

import requests
import json
import pickle
import sys

fname='token_store.pkl'
fname2='id_store.pkl'
docfolder='images/'

# ********** configuration ******************
with open('config.txt') as json_file:
  cfg=json.load(json_file)
  gbg_url=cfg['gbg_url']
  pathroot=cfg['pathroot']
  journey_id=cfg['journey_id']
  journey_version=cfg['journey_version']
  docname=cfg['docname']

customer_reference="44820bbd-8b4d-4645-b8e3-4d2c3b9ba5d0"
verify_document_ep = pathroot + "/person/documentImage"
verify_document_id_append = "/documentImage"

# ********* local variables *****************
use_stored_person_id=0

# ********* read stored GBG access token ************
with open(fname, 'rb') as f:
  idp_access_token, gbg_access_token = pickle.load(f)


# ************** verify document **************
# tolerance can be DEFAULT, MEDIUM or STRICT

headers={
         "tolerance" : "DEFAULT",
         "journey-id": journey_id,
         "journey-version": journey_version,
         "customer-reference": customer_reference,
         "file": "image/jpg",
         "Authorization": "Bearer "+gbg_access_token}

if (len(sys.argv)>1):
  # we have a person-id parameter
  use_stored_person_id=1
  with open(fname2, 'rb') as f:
    person_id = pickle.load(f).pop()
    headers["person-id"]=person_id

files={'file': (docname, open(docfolder+docname, 'rb'), 'image/jpeg', {'action': (None, 'store')})}

if (use_stored_person_id==0):
  r=requests.post(url=gbg_url+verify_document_ep, headers=headers, files=files)
else:
  r=requests.post(url=gbg_url+pathroot+"/"+person_id+verify_document_id_append, headers=headers, files=files)

print("headers:")
print(json.dumps(dict(r.headers), indent=2))

print("body:")
api_resp=json.loads(r.text)
print(json.dumps(api_resp, indent=2))

verification_id=api_resp['verificationID']
print("verificationID is", verification_id)

print("score is ", api_resp['score'])

decision=api_resp['decision']
print("current decision is ", decision['current'])

print("combined decision is ", decision['combined'])

# **** save the person-id and verificationID ******
person_id=r.headers['person-id']
with open(fname2, 'wb') as f:
  pickle.dump([person_id, verification_id], f)
print("saved person-id and verificationID to %s"%fname2)

print("#********************************************************************")

