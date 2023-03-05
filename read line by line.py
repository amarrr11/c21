fobj=open("opensource.txt","r")
str=" "
while str:
    str=fobj.readline()
    print(str)
fobj.close
