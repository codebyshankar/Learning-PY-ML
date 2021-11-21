import json

people_string = '''
{
    "people": [
    {
        "name": "Shankar",
        "phone": "999-888-777",
        "emails": ["shan@email.com", "kar@email.com"],
        "has_license": false
    },
    {
        "name": "Niru",
        "phone": "888-777-666",
        "emails": null,
        "has_license": true
    }
    ]
}
'''

data = json.loads(people_string)
# print(data)
# print(type(data))
for person in data["people"]:
    del person["phone"]

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)