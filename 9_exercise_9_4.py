"""
Exercise 9.4

9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
emails = {}
for line in handle:
    if "From:" in line: continue
    elif "From" in line:
        line = line.split("From")
        line = (str(line[1]).strip()).split( )
        if line[0] not in emails.keys():
            emails[line[0]] = 1
        else:
            emails[line[0]] = emails.get(line[0],0) + 1        
    else: continue
freq = [(value,key) for key,value in emails.items()]
print(max(freq)[1],max(freq)[0])