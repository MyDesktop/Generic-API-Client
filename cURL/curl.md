# Sample cURL commands

## Obtain an access token using a refresh token

```
curl https://integrations.mydesktop.com.au/api/v1.0/token?api_key=<YOUR_API_KEY_HERE> -u '<YOUR_REFRESH_TOKEN>':''
```

## Retrieve a list of contacts:

```
curl https://integrations.mydesktop.com.au/api/v1.0/contacts?api_key=<YOUR_API_KEY_HERE> -u '<YOUR_ACCESS_TOKEN>':'' 
```

## Add a new contact:

```
curl -X POST https://integrations.mydesktop.com.au/api/v1.0/contacts?api_key=<YOUR_API_KEY_HERE> -u '<YOUR_ACCESS_TOKEN>':'' -H "Content-Type: application/json" -d '{"firstname":"Matt","lastname":"Healy"}'
```

## Update an existing contact:

```
curl -X PUT https://integrations.mydesktop.com.au/api/v1.0/contacts/<CONTACTID>?api_key=<YOUR_API_KEY_HERE> -u '<YOUR_ACCESS_TOKEN>':'' -H "Content-Type: application/json" -d '{"firstname":"Matt","lastname":"Healy"}'
```
