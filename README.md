Generic-API-Client
==================

Sample cURL commands, Python code and PHP code for connecting to MyDesktop's Generic API

Only approved integration partners can access this API. To find out more, please email api@mydesktop.com.au.

Changes to the API are published on Twitter - https://twitter.com/MyDesktopAPI

Authentication Flow
==================

Once you've become an approved integration partner, MyDesktop will supply you with a unique *API Key*. Every request must include a query string parameter `api_key` with your API Key. This is how we identify you as the partner accessing the API.

Office Based Authentication
------

> Using a token from this authentication method will return the office's full data set

A System Administrator in the MyDesktop office will also need to allow you API access to their MyDesktop database. They will supply you with a unique *Access Token*. This token never changes for that office, unless they revoke and re-create the token.

User Based Authentication
------

> Using a token from this authentication method will return a subset of the office's data, only what is accessible by this user

Any MyDesktop user can provide their username and password to be used as HTTP Basic Authentication details for the `/login` endpoint, which returns a unique *Access Token*.

If the user has Two Factor Authentication enabled:
* The *Access Token* will not be returned by this initial connection
* A message will be returned (to display for the user) stating an SMS has been sent to the user with the 2FA PIN
* Make another `/login` call with the same username, and the entered 2FA PIN as the password
* Assuming a correct PIN was entered, the user's *Access Token* will now be returned

> Due to this flow, *currently* the User Based Authentication should only be used in instances where the user logs themselves in

This token will remain valid until the user changes their password, in which case it will be invalidated and need to be reauthenticated.

The Access Token
------

Now, you can use the *Access Token* to access the office or user's data. For example, you would call the `/contacts` endpoint, using the *Access Token* as the HTTP Basic Authentication username.

We recommend building logic in to your application to handle a 401 error.

Date/Time Format
==================

Generally, the API returns the following format for Date objects:

`YYYY-MM-DD`

e.g. `2016-04-28`

and the following format for DateTime objects:

`YYYY-MM-DDThh:mm:ss`

e.g. `2016-04-28T14:49:05`

When sending date/datetime data to the API, you have the option to submit in these formats:

Date: `YYYY-MM-DD`

DateTime: `YYYY-MM-DDThh:mm:ss`, `YYYY-MM-DD hh:mm:ss`

Please note that all times are 24-hour.
