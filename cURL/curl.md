# Sample cURL commands

## Retrieve a list of contacts:

```
curl -X GET 'https://integrations.mydesktop.com.au/api/v1.1/contacts?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':''
```

## Retrieve a list of contact categories:

```
curl -X GET 'https://integrations.mydesktop.com.au/api/v1.1/categories?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':''
```

## Retrieve a list of contacts filtered by category "Current Buyers" with ID 2, ordered by first name:

```
curl -X GET 'https://integrations.mydesktop.com.au/api/v1.1/contacts?api_key=<YOUR_API_KEY_HERE>&category=2&orderby=firstname' \
    -u '<YOUR_ACCESS_TOKEN>':''
```

## Add a new contact and assign the category "Current Buyers" with ID 2:

```
curl -X POST 'https://integrations.mydesktop.com.au/api/v1.1/contacts?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':'' \
    -H "Content-Type: application/json" \
    -d '{"firstname":"Matt","lastname":"Healy","categories:[{"id": 2}]}'
```

## Update an existing contact to add a mobile phone number:

```
curl -X PUT 'https://integrations.mydesktop.com.au/api/v1.1/contacts/<CONTACTID>?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':'' \
    -H "Content-Type: application/json" \
    -d '{"mobile":"0400000000"}'
```

## Delete an existing contact:

```
curl -X DELETE 'https://integrations.mydesktop.com.au/api/v1.1/contacts/<CONTACTID>?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':''
```
