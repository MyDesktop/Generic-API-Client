# Sample cURL commands

## Retrieve a list of contacts:

```
curl -X GET 'https://integrations.mydesktop.com.au/api/v1.1/contacts?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':''
```

## Add a new contact:

```
curl -X POST 'https://integrations.mydesktop.com.au/api/v1.1/contacts?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':'' \
    -H "Content-Type: application/json" \
    -d '{"firstname":"Matt","lastname":"Healy"}'
```

## Update an existing contact:

```
curl -X PUT 'https://integrations.mydesktop.com.au/api/v1.1/contacts/<CONTACTID>?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':'' \
    -H "Content-Type: application/json" \
    -d '{"firstname":"Matt","lastname":"Healy"}'
```

## Delete an existing contact:

```
curl -X DELETE 'https://integrations.mydesktop.com.au/api/v1.1/contacts/<CONTACTID>?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':''
```
