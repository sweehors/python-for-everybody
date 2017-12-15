import json
import sqlite3

#create connection object
conn = sqlite3.connect('15_rosterdb.sqlite')

#create cursor object
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

#read filename from cmdline
fname = input('Enter file name: ')

#use default if filename not entered
if len(fname) < 1:
    fname = 'roster_data.json' #modified to read the correct sample filename

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

#open and load json data
str_data = open(fname).read()
json_data = json.loads(str_data)


for entry in json_data:

    name = entry[0];
    title = entry[1];
    role = entry[2]; # store the role column
    #print((name, title, role)) #modified to include role

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) ) #modified to include role

    conn.commit()

#show results from query
sqlstr = '''SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1''' #modified the original query so that only first result shown 

for row in cur.execute(sqlstr):
    print(str(row[0]))

#close cursor
cur.close()