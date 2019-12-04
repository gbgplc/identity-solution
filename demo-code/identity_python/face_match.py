#!/usr/bin/python3

import requests
import json
import pickle

fname='token_store.pkl'
fname2='id_store.pkl'
docfolder='images/'

# ********** configuration ******************
with open('config.txt') as json_file:
  cfg=json.load(json_file)
  gbg_url=cfg['gbg_url']
customer_reference="44820bbd-8b4d-4645-b8e3-4d2c3b9ba5d0"
face_match_ep="/verify/facematch/v1/selfie"
with open('config.txt') as json_file:
  cfg=json.load(json_file)
  docname=cfg['facefilename']

# ********* read stored GBG access token ************
with open(fname, 'rb') as f:
  idp_access_token, gbg_access_token = pickle.load(f)


# ************** face match **************
with open(fname2, 'rb') as f:
  person_id, verification_id = pickle.load(f)

headers={
         "person-id": person_id,
         "document-verification-id": verification_id,
         "customer-reference": customer_reference,
         "Authorization": "Bearer "+gbg_access_token}

files={'file': (docname, open(docfolder+docname, 'rb'), 'image/jpeg', {'action': (None, 'store')})}

r=requests.post(url=gbg_url+face_match_ep, headers=headers, files=files)

print("headers:")
print(json.dumps(dict(r.headers), indent=2))

print("body:")
api_resp=json.loads(r.text)
print(json.dumps(api_resp, indent=2))

verification_id=api_resp['verificationID']
print("verificationID is", verification_id)

verification=api_resp['verification']
print("result is ", verification['result']['state'])

combined=api_resp['combined']
print("combined is ", combined['decision'])

# **** save the person-id and verificationID ******
#person_id=r.headers['person-id']
#with open(fname2, 'wb') as f:
#  pickle.dump([person_id, verification_id], f)
#print("saved person-id and verificationID to %s"%fname2)

