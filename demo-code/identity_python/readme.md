
# Using the Identity Solution Python Files

## Introduction
The bundle called identity_python provides an easy way to test out API calls for the GBG Identity Solution. This document describes how to use the programs or modify them to suit your needs. No Python programming knowledge is needed.

## What’s in the Bundle?
Currently, the bundle contains these configuration files which are used by the Python programs. These configuration files should be manually edited prior to running the programs. 

Name: **auth.txt**

Description: This file contains the credentials to connect to the GBG Identity Solution

Name: **config.txt**

Description: This file contains an identifier labelled journey_id which is supplied when you register for the GBG Identity Solution. You can also populate the name of any document you wish to use for verification in this file too.

The bundle contains the following Python programs:

Name: **get_token.py**

Description: When executed, this program will connect to the identity provider service (such as Microsoft Azure or Amazon AWS) to retrieve an identity provider access token, and then connect to the GBG Identity Solution service to exchange that for a GBG access token.

Name: **verify_person_v4.py**

Description: When executed, this program will connect to the identity provider service (such as Microsoft Azure or Amazon AWS) to retrieve an identity provider access token, and then connect to the GBG Identity Solution service to exchange that for a GBG access token.

Name: **verify_person_v4.py**

Description: This program will call the Identity Solution API in order to verify person details. Today, the person details you wish to specify can be directly edited within the verify_person_v4.py program before running it. How to do this is described further below.

Name: **verify_documentimage_v4.py**

Description: This program will call the Identity Solution API in order to verify a document. The document name is specified in the config.txt file today. Place the document image file (for example in JPG format) in the images sub-folder prior to running this program.

Name: **face_match.py**

Description: This program will call the Identity Solution’s Face Match service. Prior to running this program, place the image file in the images sub-folder, and populate the filename in the config.txt file.

Name: **verify_person.py** [deprecated]

Description: This program performs tasks similar to verify_person_v4.py, but uses an older API. This program will be removed in later releases.

Name: **verify_document.py** [deprecated]

Description: This program is similar to verify_documentimage_v4.py but using an older API. This program will be removed in later releases.

## Setting up the Configuration Files
### auth.txt
Example content is shown here. This example uses Microsoft Azure as the identity provider.
Please note that the Machine-to-Machine (M2M) Client Secret authentication method is used for this example code bundle.

	{
	  "auth_url": "https://login.microsoftonline.com",
	  "auth_ep": "/d343dc04-2abd-95b3-1047-2f6afc760ed8/oauth2/v2.0/token",
	  "app_client_id": "56ead310-af1e-aff7-944e-dbaf7b0c3a7d",
	  "app_pw_client_secret": "xDWXq7@=?MEgj:u5DqE3mJ40PoQjw73P",
	  "scope_append": "/.default"
	}

### config.txt
Here is example content for the config.txt file. You can modify this to suit your needs.

	{
	  "gbg_url": "https://api.gbgplc.com",
	  "pathroot": "/verify/people/v4",
	  "journey_id": "04c7efc6-83b7-a7e8-b423-6cde8fa924a2",
	  "journey_version": "1",
	  "docname": "demo_doc_passport.jpeg",
	  "facefilename": "bobselfie.jpg"
	}

## Running the Code
These current instructions assume that you’re using Linux or a Mac. If you’re running Windows, you may need to modify some of these instructions. 

Ensure that your computer has Python 3.x.x installed. You can test this by typing the following:

	/usr/bin/python3 --version
It should return a version number such as 3.6.8.

Next, ensure the programs have ‘execute’ permission by typing: 

	chmod 755 *.py *.sh
You can now run any of the Python programs by typing ./ followed by the program name. For instance:

	./get_token.py
No additional command line parameters are used, except when person identifiers need to be chained.

For instance, if you wish to execute verify_person_v4.py followed by verify_documentimage_v4.py then you can specify the text with-person-id on the command line for the second command:

	./verify_person_v4.py
	./verify_documentimage_v4.py with-person-id

## Creating Scripts
You can automatically execute multiple Python programs in sequence by creating scripts. There is an example script in the bundle, called data_first.sh. The script is executed in the same manner:

	./data_first.sh
You can use scripts to automatically first run get_token.py followed by any other Python programs.

## How do the Python programs communicate with each other?
_Note: this information is unnecessary for running the programs, but the information is useful if you wish to copy and edit the programs to suit your needs._

When  get_token.py is executed, it will automatically same the GBG access token into a file called token_store.pkl and the other Python programs will automatically read from that file.

When any of the other programs are executed, the programs will extract the Person Identifier field (it is in the response header named ‘person-id’) and save it to a file called id_store.pkl. Programs will read the file and make use of that field if the command line has with-person-id appended.

## What do the programs display?
When the programs are executed, the output will display the response to the API call. The response headers are displayed, along with the response body. After that, a summary is displayed showing the decision and score.

Here is the example output for verify_person_v4.py:

	Linux-pc:~/development/identity_python$ ./verify_person_v4.py 
	headers:
	{
	  "Date": "Wed, 04 Dec 2019 00:12:23 GMT",
	  "Content-Type": "application/json; charset=utf-8",
	  "Connection": "keep-alive",
	  "customer-reference": "41120bbd-8b4d-4645-b8e3-4d2c3b9ba5d0",
	  "person-id": "735ce73a-e048-4533-962d-a803842e2d93",
	  "Referrer-Policy": "origin, origin",
	  "Server": "nginx",
	  "Strict-Transport-Security": "max-age=15768000, max-age=15768000",
	  "verification-id": "fc5ea09f-199f-4e3b-b457-6decceb82ce3",
	  "X-Content-Type-Options": "nosniff, nosniff",
	  "X-Download-Options": "noopen, noopen",
	  "X-Frame-Options": "SAMEORIGIN, SAMEORIGIN",
	  "X-Permitted-Cross-Domain-Policies": "none, none",
	  "X-Robots-Tag": "none, none",
	  "Set-Cookie": "visid_incap_1956318=NLwUezXF4dINqSm6uLZS+d755l0AAAUIPAAAAAQAAACLI9UOcK0lwqyOyVE7XX2i; expires=Wed, 02 Dec 2020 06:17:37 GMT; path=/; Domain=.gbgplc.com, nlbi_1156238=ro1NUR7r4z/wABECBhYrs3j27mTI7sCpnjabRC8I4IYXI96T; path=/; Domain=.gbgplc.com, abcde_ses_267_1948238=scaNQ6jQIDODTwGCAArTUf55l0Aa0NAUW0CIngbjbMU89lPg==; path=/; Domain=.gbgplc.com",
	  "X-CDN": "Abcdefg",
	  "Content-Encoding": "gzip",
	  "Transfer-Encoding": "chunked",
	  "X-Iinfo": "4-123344117-15624518 NNYN CT(11 26 0) RT(157287350492 22) q(0 0 0 0) r(25 25) U6"
	}
	body:
	{
	  "verificationID": "fbeeab9f-194f-42fb-b457-6dc35ce72253",
	  "timestamp": "2019-12-04T00:12:22Z",
	  "verificationURL": "https:// gbgplc.com/verify/history/v3/people/7323ef3a-e998-4126-962d-a808251e2d93/verifications/fb23909f-1aef-415b-b827-6dcd43cca253/response",
	  "score": 10,
	  "decision": {
	    "current": "PASS: Passed",
	    "combined": "UNDETERMINED"
	  },
	  "action": ""
	}
	score is  10
	current decision is  PASS: Passed
	combined decision is  UNDETERMINED
	saved person-id to id_store.pkl
	#********************************************************************


