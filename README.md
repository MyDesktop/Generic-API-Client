Generic-API-Client
==================

Sample cURL commands, Python code and PHP code for connecting to MyDesktop's Generic API

Only approved integration partners can access this API. To find out more, please email api@mydesktop.com.au.

Changes to the API are published on Twitter - https://twitter.com/MyDesktopAPI

Authentication Flow
==================

Once you've become an approved integration partner, MyDesktop will supply you with a unique *API Key*. Every request must include a query string parameter `api_key` with your API Key. This is how we identify you as the partner accessing the API.

The MyDesktop user will also need to allow you API access to their MyDesktop database. They will supply you with a unique *Refresh Token*. This token never changes for that user, unless they revoke and re-create the token.

Once you have the *Refresh Token*, you'll need to obtain an *Access Token*. To do so, simply call the `/token` endpoint, using the *Refresh Token* as the HTTP Basic Authentication username. This will generate an *Access Token* which expires in 1 hour. 

Now, you can use the *Access Token* to access the user's data. For example, you would call the `/contacts` endpoint, using the *Access Token* as the HTTP Basic Authentication username.

When the *Access Token* expires, simply call `/token` to get another one. We recommend building logic in to your application so that it can detect a 401 error and get a new *Access Token* automatically.
