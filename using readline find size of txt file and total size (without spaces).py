fobj=open("opensource.txt","r")
str=" "
size=0
tsize=0
while str:
    str=fobj.readline()
    size=size+len(str)
    tsize=tsize+len(str.strip())
print(size)
print(tsize)
