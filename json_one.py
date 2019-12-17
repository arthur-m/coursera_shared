import json

# json is a serialization format, like xml. also: 'data interchange format'
# represents data as nested lists and dictionaries (technically, not
# python lists and dicts, but JSON lists and dicts)

# json has no start tag, no end tag, no attributes, no text area.
# (as compared to XML)

# less rich representation of data than xml, but much easier to use.

# in the below, both 'data' and 'input' -are- JSON format.

data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)     # loads() means 'load from string'
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])

print('\n', type(info))

# json data - two dictionaries inside a list
input = '''[
    { "id" : "001",
      "x" : "2",
      "name" : "Chuck"
    },
    { "id" : "009",
      "x" : "7",
      "name" : "Chuck"
    }
]'''

info = json.loads(input)  # turn the json formatted STRING into a python data strcuture / object
print('User count:', len(info))
for item in info:           # info is a list of dictionaries
    print('Name', item['name']) # access key-value pairs in the current dict
    print('Id', item['id'])
    print('Attribute', item['x'])











