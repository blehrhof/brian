
import re

def find(pat,text):
    match = re.search(pat,text)
    if match:
        print(match.group())
    else:
        print('no match')


find('igs','called piiig')
find('ig','called piiig')
# dot is wildcard
find('...g','called piiig') 
# search is left to right, first hit is a true
# escape a period 
# r is raw mode
find(r'c\.l','c.lled piig   much better: xyzgs')
# pattern match with periods that substitute
find(r'..gs','c.lled piig   much better: xyzgs')
# backslash w is a word character
find(r':\w\w\w', 'blah :cat blah blah')
find(r':\w\w\w\w', 'blah :cat blah blah')
# backslash d is a digit
find(r'\d\d\d','blah :123xxx')
# backslash s is whitespace
find(r'\d\s\d\s\d','1 2 3')
# + one or more  * zero or more
find(r'\d\s+\d\s+\d','1             2              3')
find(r':\w+','blah blah :kitten asdf asdf')
find(r':.+','blah blah :kitten asdf asdf')
#
find(r':\S+','blah blah :kittenasdfasdfasdf asdf asdf')
# email ...
find(r'\w+@\w+','blah blah bsl@yahoo.com asdf asdf')
find(r'[\w.]+@[\w.]+','blah blah bsl@yahoo.com asdf asdf')
find(r'\w[\w.]*@[\w.]+','blah blah bsl@yahoo.com asdf asdf')
m=re.search(r'([\w.]+)@([\w.]+)','blah blah bsl@yahoo.com asdf asdf')
#whole group
m.group()
# user name
m.group(1)
# host name
m.group(2)
re.findall(r'([\w.]+)@([\w.]+)','blah blah bsl@yahoo.com asdf asdf  foo@bar')
re.findall(r'[\w.]+@[\w.]+','blah blah bsl@yahoo.com asdf asdf  foo@bar')
# findall (pattern, what to search, options)
# dir(re) returns options ... IGNORECASE, etc
re.findall(r'[\w.]+@[\w.]+','blah blah bsl@yahoo.com asdf asdf  foo@bar', re.IGNORECASE)



