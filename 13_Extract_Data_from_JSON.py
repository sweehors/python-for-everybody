"""
 Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

    Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
    Actual data: http://py4e-data.dr-chuck.net/comments_57128.json (Sum ends with 10)

You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis. 

The closest sample code that shows how to parse JSON and extract a list is json2.py. You might also want to look at geoxml.py to see how to prompt for a URL and retrieve data from a URL. 


"""
import urllib.request, json

address = input('Enter location: ')
print('Retrieving', address)
with urllib.request.urlopen(address) as url:
    raw = json.loads(url.read().decode())

print('Retrieved', len(str(raw)), 'characters')
data = raw.get("comments")
#print(data)
num = total = 0
for i in range(len(data)):
    tmp = data[i]
    value = tmp.get("count")
    num = num + 1
    total = total + int(value)
print("Count:",num)
print("Sum:",total)