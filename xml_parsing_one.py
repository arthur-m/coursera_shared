import xml.etree.ElementTree as ET

data = '''<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
 </person>'''

tree = ET.fromstring(data)                  # xml to python data structure
print('Name:', tree.find('name').text)      # retrieve text from tag with .text
print('Attr:', tree.find('email').get('hide')) # retrieve attribute from tag with .get

print(type(tree))
