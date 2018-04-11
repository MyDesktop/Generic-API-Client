# Sample cURL commands

## Retrieve a list of contacts:

```
curl -X GET 'https://integrations.mydesktop.com.au/api/v1.2/contacts?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':''
```

## Retrieve a list of contact categories:

```
curl -X GET 'https://integrations.mydesktop.com.au/api/v1.2/categories?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':''
```

## Retrieve a list of contacts filtered by category "Current Buyers" with ID 2, ordered by first name:

```
curl -X GET 'https://integrations.mydesktop.com.au/api/v1.2/contacts?api_key=<YOUR_API_KEY_HERE>&category=2&orderby=firstname' \
    -u '<YOUR_ACCESS_TOKEN>':''
```

## Add a new contact and assign the category "Current Buyers" with ID 2:

```
curl -X POST 'https://integrations.mydesktop.com.au/api/v1.2/contacts?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':'' \
    -H "Content-Type: application/json" \
    -d '{"firstname":"Matt","lastname":"Healy","categories":[{"id": 2}]}'
```

## Update an existing contact to add a mobile phone number:

```
curl -X PUT 'https://integrations.mydesktop.com.au/api/v1.2/contacts/<CONTACTID>?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':'' \
    -H "Content-Type: application/json" \
    -d '{"mobile":"0400000000"}'
```

## Update an existing contact to unsubscribe them from SMS messages

First, get the valid values for unsubscribe options:

```
curl -X GET 'https://integrations.mydesktop.com.au/api/v1.2/unsubscribetypes?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':''
```

Then, get the contact's existing unsubscribe options:

```
curl -X GET 'https://integrations.mydesktop.com.au/api/v1.2/contacts/<CONTACTID>?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':''

<snip>
    "unsubscribeoptions": [{"id": 5}]
</snip>

```

Now update the contact's unsubscribe options, including the option for SMS (4)

```
curl -X PUT 'https://integrations.mydesktop.com.au/api/v1.2/contacts/<CONTACTID>?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':'' \
    -H "Content-Type: application/json" \
    -d '{"unsubscribeoptions": [{"id": 5},{"id": 4}]}'
```

## Add a Residential Buy/Rent Requirement to the contact:

```
curl -X POST 'https://integrations.mydesktop.com.au/api/v1.2/contacts/<CONTACTID>/buyrent?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':'' \
    -H "Content-Type: application/json" \
    -d '{"type":"residential","fromprice":200000,"toprice":400000,"residential":{"carspaces":0,"bathrooms":1,"bedrooms":3,"propertytype":{"id":1}}}'
```

## Add a Commercial Buy/Rent Requirement to the contact:
###### Note: "type" value accepts (default) "residential", "commercial", "business", "rural", "livestock", "clearing sale"

```
curl -X POST 'https://integrations.mydesktop.com.au/api/v1.2/contacts/<CONTACTID>/buyrent?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':'' \
    -H "Content-Type: application/json" \
    -d '{"type":"commercial","fromprice":1000000,"toprice":1500000,"commercial":{"fromland":1000,"toland":5000,"frombuild":2000,"propertytype":{"id":3}}}'
```

## Create a Property Alert for that Buy/Rent Requirement:

```
curl -X POST 'https://integrations.mydesktop.com.au/api/v1.2/propertyalerts?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':'' \
    -H "Content-Type: application/json" \
    -d '{"contact":{"id":<CONTACTID>},"requirement":{"id":<REQUIREMENTID>},"sender":{"id":<AGENTID>},"name":"My First Property Alert","pricechanges":true,"insertdate":"2016-09-19 09:00:00","subject":"Your Property Alert","sendingpattern":{"frequency":"Daily","day":"Every"}}'
```

## Add a Contact Note linked to the Property
###### Note: To link the Contact Note to the Property use the Note Classification ID 26 "Email Feedback" or ID 4 "Home Open/Inspection Feedback (listings)"
```
curl -X POST 'https://integrations.mydesktop.com.au/api/v1.2/contacts/<CONTACTID>/notes?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':'' \
    -H "Content-Type: application/json" \
    -d '{"property":{"id":<PROPERTYID>},"note":"Loves the kitchen size","classification":{"id":26},"inspectiondate":"2016-08-22 10:11:12"}'
```

## Delete an existing contact:

```
curl -X DELETE 'https://integrations.mydesktop.com.au/api/v1.2/contacts/<CONTACTID>?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':''
```

## Attach a property to a contact (as an owner):

```
curl -X POST 'https://integrations.mydesktop.com.au/api/v1.2/contacts/<CONTACTID>/properties?api_key=<YOUR_API_KEY_HERE>' \
    -u '<YOUR_ACCESS_TOKEN>':'' \
    -H "Content-Type: application/json" \
    -d '{"property": {"id":<PROPERTYID>}, "type":"owner"}'
```

# Adding an image from your local directory
```
curl -X POST \
  'https://integrations.mydesktop.com.au/api/v1.2/images?api_key=<APIKEY>' \
  -H 'Authorization: Basic <AUTHTOKEN>' \
  -H 'Cache-Control: no-cache' \
  -H 'content-type: multipart/form-data' \
  -F file=@"/Users/user1/Desktop/pics/user1.jpg"
```

# Adding an image from a link
```
curl -X POST \
  'https://integrations.mydesktop.com.au:443/api/v1.2/images?api_key=API-KEY' \
  -H 'authorization: Basic TOKEN' \
  -H 'content-type: application/json' \
  -d '{"url":"<imageurl>","hiresurl":"<imageurl>"}'

curl -X PUT \
  'https://integrations.mydesktop.com.au:443/api/v1.2/properties/<propertyid>?api_key=API-KEY' \
  -H 'authorization: Basic TOKEN' \
  -H 'content-type: application/json' \
  -d '{"images":
	[
		{
			"imageid":<imageid>,
			"order":1
			
		}
	]
	
}'
```
