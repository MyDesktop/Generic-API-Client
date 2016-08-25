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
    -d '{"firstname":"Matt","lastname":"Healy","categories":[{"id": 2}]}'
```

## Update an existing contact to add a mobile phone number:

```
curl -X PUT 'https://integrations.mydesktop.com.au/api/v1.1/contacts/<CONTACTID>?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':'' \
    -H "Content-Type: application/json" \
    -d '{"mobile":"0400000000"}'
```

## Update an existing contact to unsubscribe them from SMS messages

First, get the valid values for unsubscribe options:

```
curl -X GET 'https://integrations.mydesktop.com.au/api/v1.1/unsubscribetypes?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':''
```

Then, get the contact's existing unsubscribe options:

```
curl -X GET 'https://integrations.mydesktop.com.au/api/v1.1/contacts/<CONTACTID>?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':''

<snip>
    "unsubscribeoptions": [{"id": 5}]
</snip>

```

Now update the contact's unsubscribe options, including the option for SMS (4)

```
curl -X PUT 'https://integrations.mydesktop.com.au/api/v1.1/contacts/<CONTACTID>?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':'' \
    -H "Content-Type: application/json" \
    -d '{"unsubscribeoptions": [{"id": 5},{"id": 4}]}'
```

## Add a Buy/Rent Requirement to the contact:

```
curl -X POST 'https://integrations.mydesktop.com.au/api/v1.1/contacts/<CONTACTID>/buyrent?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':'' \
    -H "Content-Type: application/json" \
    -d '{"type":"residential","fromprice":200000,"toprice":400000,"residential":{"carspaces":0,"bathrooms":1,"bedrooms":3,"propertytype":{"id":1}}}'
```

## Create a Property Alert for that Buy/Rent Requirement:

```
curl -X POST 'https://integrations.mydesktop.com.au/api/v1.1/propertyalerts?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':'' \
    -H "Content-Type: application/json" \
    -d '{"contact":{"id":<CONTACTID>},"requirement":{"id":<REQUIREMENTID>},"sender":{"id":<AGENTID>},"name":"My First Property Alert","pricechanges":true,"insertdate":"2016-09-19 09:00:00","subject":"Your Property Alert","sendingpattern":{"frequency":"Daily","day":"Every"}}'
```

## Add a Contact Note linked to the Property
###### Note: To link the Contact Note to the Property use the Note Classification ID 26 "Email Feedback" or ID 4 "Home Open/Inspection Feedback (listings)"
```
curl -X POST 'https://integrations.mydesktop.com.au/api/v1.1/contacts/<CONTACTID>/notes?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':'' \
    -H "Content-Type: application/json" \
    -d '{{"property":{"id":<PROPERTYID>},"note":"Loves the kitchen size","classification":{"id":26},"inspectiondate":"2016-08-22 10:11:12"}'
```

## Delete an existing contact:

```
curl -X DELETE 'https://integrations.mydesktop.com.au/api/v1.1/contacts/<CONTACTID>?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':''
```
