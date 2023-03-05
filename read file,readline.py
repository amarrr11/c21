#only read
fobj=open("opensource.txt","r")
value=fobj.read()
print(value)
#read upto a particular binary or characters
fobj=open("opensource.txt","r")
value=fobj.read(23)
print(value)
#read a line: readline()
fobj=open("opensource.txt")
value=fobj.readline()
print(value)
fobj=open("opensource.txt")
value=fobj.readline()
print(value)

#readlines(): reads all the lines in list format
fobj=open("opensource.txt","r")
value=fobj.readlines()
print(value)
