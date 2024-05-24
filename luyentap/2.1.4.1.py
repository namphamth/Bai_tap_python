import xml.etree.ElementTree as ET #Bước 1

tree = ET.parse('employee.xml') #Bước 2

root = tree.getroot()
name = root.find('fname') #Bước 3
print(name.text)

expertise = root.find('expertise') #Bước 4
print(expertise.attrib['name'])

city = root.find('city') #Bước 5

print(city.text)
newexpertise = ET.Element('expertise')

newexpertise.attrib['name'] = 'XML' #Bước 6
root.append(newexpertise)
tree.write('updated.xml')
