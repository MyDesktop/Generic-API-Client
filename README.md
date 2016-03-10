Generic-API-Client
==================

Sample cURL commands, Python code and PHP code for connecting to MyDesktop's Generic API

Only approved integration partners can access this API. To find out more, please email api@mydesktop.com.au.

Changes to the API are published on Twitter - https://twitter.com/MyDesktopAPI

Authentication Flow
==================

Once you've become an approved integration partner, MyDesktop will supply you with a unique *API Key*. Every request must include a query string parameter `api_key` with your API Key. This is how we identify you as the partner accessing the API.

The MyDesktop user will also need to allow you API access to their MyDesktop database. They will supply you with a unique *Access Token*. This token never changes for that user, unless they revoke and re-create the token.

Now, you can use the *Access Token* to access the user's data. For example, you would call the `/contacts` endpoint, using the *Access Token* as the HTTP Basic Authentication username.

We recommend building logic in to your application to handle a 401 error.
