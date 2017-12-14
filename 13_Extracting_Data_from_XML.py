"""
Extracting Data from XML

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

    Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
    Actual data: http://py4e-data.dr-chuck.net/comments_57127.xml (Sum ends with 12)

You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis. 

"""
import urllib.request
import xml.etree.ElementTree as ET

result = 0

url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()    
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
print("Count:",len(counts))
for count in counts:
    value = count.text
    result = result + int(value)
print("Sum: ",result)