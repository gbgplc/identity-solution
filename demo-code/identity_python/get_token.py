#!/usr/bin/python3

import requests
import json
import pickle

fname='token_store.pkl'

# ********** configuration ******************
with open('config.txt') as json_file:
  cfg=json.load(json_file)
  gbg_url=cfg['gbg_url']
with open('auth.txt') as json_file:
  cfg=json.load(json_file)
  auth_url=cfg['auth_url']
  auth_ep=cfg['auth_ep']
  app_client_id=cfg['app_client_id']
  app_pw_client_secret=cfg['app_pw_client_secret']
  scope="api://"+app_client_id+cfg['scope_append']

gbg_auth_ep="/authenticate/v1/connect/token"

# ********* get IDP access token ************
form_data={"grant_type": "client_credentials",
           "client_id": app_client_id,
           "client_secret": app_pw_client_secret,
           "scope": scope,
           "state": "12345"}
r=requests.post(url=auth_url+auth_ep, data=form_data)
auth_resp=json.loads(r.text)
idp_access_token=auth_resp['access_token']
print("idp_access_token is %s"%idp_access_token)

# ******** get GBG access token *************
form_data={"grant_type": "id_auth",
           "client_id": "ro.client",
           "client_secret": "secret",
           "id_token": idp_access_token}
r=requests.post(url=gbg_url+gbg_auth_ep, data=form_data)
gbg_auth_resp=json.loads(r.text)
gbg_access_token=gbg_auth_resp['access_token']
print("gbg_access_token is %s"%gbg_access_token)

# ******* save the GBG access token *********
with open(fname, 'wb') as f:
  pickle.dump([idp_access_token, gbg_access_token], f)
print("saved access token to %s"%fname)



