for i in [0,1,2,3,4,5]:
    print i**2


for i in range(6):
    print i**2

for i in xrange(6):
    print i**2

colors = ['a','b','c','d']

for i in range(len(colors)):
    print(colors[i])

for color in colors:
    print color

for i in range(len(colors)-1,-1,-1):
    print colors[i]

for color in reversed(colors):
    print color

for i in range(len(colors)):
    print i, '-->', colors[i]

for i, color in enumerate(colors):
    print i, '-->', colors[i]

names=['x', 'y','z']


n=min(len(names), lencolors)):
    for i in range(n):
        print names[i], '--->', colors[i]

for name,color in zip(names, colors):
        print names[i], '--->', colors[i]

# iterator zip
for name,color in izip(names, colors):
        print names[i], '--->', colors[i]

# looping in sorted order

for color in sorrted(colors):
    print(colors)

for color in sorted(colors, reverse=True):
    print(colors)

# custom sort order

def compare_len(c1,c2):
    if len(c1) < len(c2):  
        return -1
    if len(c1) > len(c2):
        return 1
    return 0

print sorted(colors,cmp=compare_length)

print sorted(colors, key=len)

# call a function until a sentinel value

blocks=[]
while True:
    block=f.read(32)
    if block=='':
        break
    blocks.append(block)

blocks=[]
for block in iter(partial(f.read,32), ''):
    blocks.append(block)


# for loops are really foreach
# also makes block iterable

# distinguishing multiple exit points in loops

def find(seq,target):
    found=False
    for i,value in enumerate(seq):
        if value == tgt:
            found=True
            break
        if not found:
            return = -1
        return i

def find(seq,target):
    for i,value in enumerate(seq):
        if value == tgt:
           break
    else:
        return = -1
    return i


# looping over dict keys

d={"a":"1","b":"2","c":"3"}

for k in d:
    print k

for k in d.keys():  # makes copy of keys
    if k.startswith('r'):
        del d[k]

d={ k : d[k] for k in d if not k.startswith('r')}

for k in d:
    print k, '-->', d[k]
for k,v in d.items():
    print k, '-->', d[k]
for k,v in d.items():
    print k, '-->', d[k]
for k,v in d.iteritems():
    print k, '-->', d[k]

#build a dict from pairs


names=['w','x','y','z']
colors = ['a','b','c','d']

d=dict(izip(names,colors))

# counting with dicts
color['red','green','red','blue','gree','red']

d={}
for color in colors:
    if color not in d:
        d[color]=0
    d[color] +=1

('blue':1, 'green':2, 'red':3)
# square brackets are conditional, so it can fail

d={}
for color in colors:
    d[color] = d.get(color,0) +1

d=defaultdict(int)
for color in colors:
    d[color] +=1

# grouping with dicts

names = ['raymond','rachael','matthew', 'roger', 'betty','melissa','judith','charlie']
d={}
for name in names:
    key=len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)

    # list of names with len = 7
{5: ['roger', 'betty'], 6:['rachael','judith'],
7: ['raymond','matthew','melissa','charlie']}

d={}
for name in names:
    key=len(name)
    d.setdefault(key,[]).append(name)


# setdefault is the same as get but it inserts the missing key

d=defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)

d={'matthew':'blue','rachael':'green','raymond':'red'}

while d:
    key,value=d.popitem()
    print key,'--',value

# removes item

# linking dictionaries together
defaults={'color':'red','user':'guest'}
parser=argparser.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace=parser.parse_args({})
commane_line_args={k:v  for k,v in vars(namespace).items() if v}


d=defaults.copy()
d.update(os.environ)
d.update(command_line_args)

d=ChainMap(command_line_args, os.environ, defaults)

# clarity function calls

twitter_search('@obama',False,20,True)
twitter_search('@obama', retweets-False, numtweets=20,popular=True)

# claify multiple returns values with names tuples
doctest.testmod()
(0,4)

doctest.testmod()
TestResults(failed=0,attempted=4)

TestResults = namestuple('TestResults', ['failed','attempted'])

# unpacking sequences
p='Raymond','Hettinger',0x30,'python@example.com'
fname=p[0]
lname=p[1]
age=p[2]
email=p[3]
#tuple unpacking
fname,lname,age,email = p

# updating multiple state variables
def f(n):
    x=0
    y=1
    for i in range(n):
        print x
        t=y
        y=x+y
        x=t

def f(n):
    x,y=0,1
    for i in range(n)
    print x
    x,y = y,x+y 

#simultaneous state updates
tmp_x=x+dx*t
tmp_y=y+dy*t
tmp_dx=influence(m,x,y,dx,dy,partial='x')
tmp_dy=influence(m,x,y,dx,dy,partial='y')
x=tmp_x
y = tmp_y
dx=tmp_dx
dy=tmp_dy

x,y,dx,dy = (x + dx * t,
             y + dy * t,
                influence(m,x,y,dx,dy,partial='x')
                influence(m,x,y,dx,dy,partial='y'))
             
# concatenating strings
s=names[0]
for name in names[1:]:
    s += ', ' + name
    print s

print ', '.join(names)
                    
#updating sequences

del names[0]
names.pop(0)
names.insert(0,'mark')

names=deque(['raymond','rachael','matthew', 'roger', 'betty','melissa','judith','charlie'])

del names[0]
names.popleft()
names.appendleft('mark')

# with great power comes great responsibility

# opening and closing files
f=open('data.txt')
try:
    data=f.read()
finally
f.close()

with open('data.txt' as f:
    data=f.read()

#locks
lock=threading.Lock()

lock.acquire()
try:
    print 'critical section 1'
    print 'critical section 2'
finally:
    lock.relesae()


with lock:
    print 'critical section 1'
    print 'critical section 2'

try:
    os.remove('somefile.tmp')
except OSError:
    pass
    
with ignored(OSError):
    os.remove('somefile.tmp')


@contextmanager
def ignored(*Exceptions):
    try:
        yield
    except Exceptions:
        pass


