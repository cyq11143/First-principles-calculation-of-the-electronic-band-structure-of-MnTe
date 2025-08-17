a=open("k-points",'r+')
a=a.readlines()
line=len(a)
mesh=50
print("k-points along high symmetry lines")
print((line - 1 )* mesh + 1)
print("Reciprocal")

for i in range(line):
  a[i]=a[i].strip().split()
  a[i][0]=float(a[i][0])
  a[i][1]=float(a[i][1])
  a[i][2]=float(a[i][2])
for i in range(line-1):
  for j in range(mesh):
    for k in range(3):
      print a[i][k]+(a[i+1][k]-a[i][k])*j/(mesh+0.0),         
    print 1.0 
print a[line-1][0], a[line-1][1], a[line-1][2], "1.0" 
  
