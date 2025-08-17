import os
import sys
import numpy as np
import matplotlib.pyplot as plt

import matplotlib 
plt.rcParams['font.family']=['Times New Roman']
min=-5.0 
max=3.0
step = 1
fonts = 20
#kp = [r'$\Gamma$','H','N',r'$\Gamma$','P','H','P','N']
kp = [r'$\Gamma$','M','K', r'$\Gamma$']
m=open("note-bnd",'r+')
ml=m.readlines()
ml=[ml[i].strip().split() for i in range(len(ml))]
knum=int(ml[0][0])
bnum=int(ml[0][1])

base=[ml[1],ml[2],ml[3]]
base=np.array(base)
dkvec=[]
for k in range(4,len(ml)-1):
 ml[k]=[float(ml[k][j]) for j in range(3)]
for k in range(5,len(ml)-1): 
 dkvec.append((np.array(ml[k])-np.array(ml[k-1])).tolist())
def r(m,n):
 global rfinal
 global r1
 global r2
 global r3
 r1=0
 r2=0
 r3=0
 r1=[float(m[0])*float(n[0][i]) for i in range(3)]
 r2=[float(m[1])*float(n[1][i]) for i in range(3)]
 r3=[float(m[2])*float(n[2][i]) for i in range(3)]
 x=r1[0]+r2[0]+r3[0]
 y=r1[1]+r2[1]+r3[1]
 z=r1[2]+r2[2]+r3[2]
 rfinal=np.sqrt(x**2+y**2+z**2)
sum=0
k=[0 for i in range(len(ml)-6)]
for i in range(len(ml)-6):
 r(dkvec[i],base)
 k[i]=rfinal
 sum=k[i]+sum
mesh=int(ml[len(ml)-1][0])
x=[0]
a0=0
for i in range(len(ml)-6):
 for j in range(mesh):
  a0=a0+k[i]/(mesh+0.0)
  x.append(a0)


plt.figure(figsize=(5,10))
#######up###########
file=open("bnd-up.dat",'r+')
lines=file.readlines()
a=[float(lines[i].strip()) for i in range(len(lines))]
a=np.array(a)
a.resize(knum,bnum)
b=np.transpose(a)
#plt.title("Band Structures",fontsize= fonts)
plt.ylim(min, max)
plt.xlim(0,sum)
plt.plot([0,sum],[0,0],'r-.',linewidth=1 )
hline=0
xlab_val = [0]
for i in range(len(ml)-6):
 hline=hline+k[i]
 xlab_val.append(hline)
hline=0
for i in range(len(ml)-7):
 hline=hline+k[i]
 xlab_val.append(hline)
 plt.plot([hline,hline],[min,max],'b-.', linewidth=1)
for i in range(bnum):
 plt.plot(x,b[i],'k',linewidth = 2)
 
file=open("bnd-dn.dat",'r+')
lines=file.readlines()
a=[float(lines[i].strip()) for i in range(len(lines))]
a=np.array(a)
a.resize(knum,bnum)
b=np.transpose(a)
for i in range(bnum):
 plt.plot(x,b[i],'r-.', linewidth=2)
 
#####################
########dn###########
plt.ylabel('Energy(eV)', fontsize = fonts)

#plt.xticks(xlab_val,[r'$\Gamma$','A','H','L','M','K',r'$\Gamma$'])
plt.xticks(xlab_val, kp)

plt.tight_layout()
plt.yticks(np.arange(min,max+step,step))
ax = plt.gca()
ax.tick_params(labelsize = fonts)
plt.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.1)
##plt.title(sys.argv[1],x=0.5,y=1.02)
plt.savefig("bnd.eps",format='eps', transparent=True,bbox_inches='tight', dpi=300)
#plt.savefig("bnd.png",format='png', transparent=True,bbox_inches='tight', dpi=600)