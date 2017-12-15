import sqlite3, re

#create connection object
conn = sqlite3.connect("15_orgdb.sqlite")

#create cursor object
cur = conn.cursor()

#delete table if exists
cur.execute('DROP TABLE IF EXISTS Counts')

#create table with attributes org and count
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

#read filename from cmdline
fname = input ("Enter filename:")

#assign default if none entered in cmdline
if (len(fname) < 1): fname = "mbox.txt"

#create handle to open filename entered
fh = open(fname)

#loop through to filter for email, then filter for org
for line in fh:
    if not line.startswith("From: "): continue
    pieces = line.split() 
    email = pieces[1] #filter for email
    pieces = email.split("@")
    org = pieces[1] #filer for org from email
    #org = re.sub(r'(.edu|.net|.ac|.uk|media.|.za|.com|.cam|.nl|.pt|et.|.ca)','',org) #substitude to get only org name but this is not the required answer
    #retrieve existing data
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    
    #query database
    row = cur.fetchone()
    
    #if dont exists, insert, else update 
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?,1)',(org,))
    else: 
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    #commit changes to db
    conn.commit()

#show count
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

#close cursor
cur.close()
