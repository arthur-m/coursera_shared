import xml.etree.ElementTree as ET

# tag with child example
data = '''<person>
   <name>Chuck</name>
   <phone type='intl'>
      +1 734 303 4456
    </phone>
    <email hide="yes"/>
  </person>'''

# re: the person tag - xml must have a main outer tag

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)       # extract text from name tag
print('Attr:', tree.find('email').get('hide')) # get attribute named 'hide'

# find() retrieves teh tag, then .text() or .get() retrieve the text or
# attribute of the tag, respectively.

# the email example is just to get the email tag, and then print the status
# of the 'hide' attribute (there is no actual email address being parsed).

# tag with multiple children example

input = '''<stuff>
   <users>
       <user x="2">
           <id>001</id>
           <name>Chuck</name>
       </user>
       <user x="7">
           <id>009</id>
           <name>Brent</name>
       </user>
    </users>
</stuff>'''

# stuff is the main outer tag that is required

stuff = ET.fromstring(input)
lst = stuff.findall('users/user') #find all the 'user' tags in the users branch
# lst is a list of tags, specifically 'user' tags
print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('ID', item.find('id').text)
    print('Attribute', item.get("x"))









