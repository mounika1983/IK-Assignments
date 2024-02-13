# From Python to JSON (Serialization, Encode)

import json

# dict
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# convert into JSON:
person_json = json.dumps(person)
# use different formatting style
person_json2 = json.dumps(person, indent=4)

# person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)

# the result is a JSON string:
#print(person_json)
print(person_json2)