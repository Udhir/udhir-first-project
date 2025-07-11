filename='a.txt'
new_file=[]
f=open(filename,'w+')
f.seek(0)
print(f.read())
f.write('program')
f.close()


