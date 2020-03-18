# Identity Solution Web SDK Typescript Skeleton Project Example

This is a minimal skeleton project intended to show how to use Microsoft Visual Studio and WebPack in order to build a Typescript project using the GBG Identity Solution Web SDK.

Note: The project here requires additional files in an SDK to execute. The folders in this repository are empty and need populating with the GBG Identity Solution Web SDK files. Obtain the Web SDK from GBG.

This example project can be run by placing the SDK folders or files in the indicated locations, and then opening index.code-workspace with Microsoft Visual Code. Press Ctrl+Shift+B simultaneously and then select "Build (Development, Hosted, Watch)" in order to generate the web content and serve it locally. Navigate to https://localhost:8080/ in a web browser to run it.


Note that in order to run this project there are four pre-requisites:

1. Set up a GBG Identity Solution account by contacting GBG
2. Set up Delegated Authentication with an identity provider such as Microsoft, or alternatively request a Pre-generated token from GBG
3. Place the Web SDK (obtained from GBG) in the indicated locations
4. Edit the src/index.tsx file and either implement your chosen authentication method using an authentication library (such as Active Directory Authentication Library ADAL or a HTTP library such as Fetch API) or alternatively copy-and-paste an IDP Access Token from (say) Postman if you're using that for experimenting with HTTP requests, into the idToken value.

Use the Chrome Developer tools in order to examine the operation of the code.

