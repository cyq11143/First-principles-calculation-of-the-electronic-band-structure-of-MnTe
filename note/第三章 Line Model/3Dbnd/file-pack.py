n=301      
nb=2          
nb1=9        
nb2=10      
m=10
Ef=0.3682
totbnd=16
Lb=[0.0, 0.0, 0.0] 
Lt=[0.0, 0.5, 0.0] 
Rb=[0.5, 0.0, 0.0] 
Rt=[0.5, 0.5, 0.0] 

import numpy as np
head = "k-points along high symmetry lines\n" + str(n) + "\nLine-mode\nrec \n"

#wirte the K-path to the file "KFILE"
d13=[Rb[i]-Lb[i] for i in range(3)]
d24=[Rt[i]-Lt[i] for i in range(3)]
n=int(n)
Kf=open("KFILE",'w+')
for i in range(n):
 A=[Lb[j]+i*d13[j]/(n-1) for j in range(3)]
 B=[Lt[j]+i*d24[j]/(n-1) for j in range(3)]
 Kf.writelines(str(A[0])+' '+ str(A[1])+' '+ str(A[2])+"\n")
 Kf.writelines(str(B[0])+' '+ str(B[1])+' '+ str(B[2])+"\n")
 Kf.writelines("\n")
Kf.close()

Kf=open("KFILE",'r+')

kp_num = n//m
lastline_num = n % m
mm = kp_num * 3
lm = lastline_num * 3
for kk in range(m):
 f=open("KPOINTS_"+str(kk),'w+')
 f.writelines(head) 
 for k in range(mm):
  line=Kf.readline()
  f.writelines(line) 
 f.close()

f=open("KPOINTS_"+str(m-1),'a+')
f.writelines(head) 
for kk in range(lm):  
  line=Kf.readline()
  f.writelines(line) 
f.close()
Kf.close()

#prepare for data-export.sh
f=open("data-export.sh",'w+')
f.writelines("n="+str(n)+"\n" \
+"nb="+str(nb)+"\n" \
+"nb1="+str(nb1)+"\n" \
+"nb2="+str(nb2)+"\n" \
+"m="+str(m)+"\n" \
+"Ef="+str(Ef)+"\n" \
+"totbnd="+str(totbnd)+"\n" \
+"d=$((m-1))\n \
Ef=`grep E-fermi OUTCAR |awk '{print $3}'|cut -d- -f 2`\n \
for z in `seq 0 $d`  \n \
do    \n \
grep ^band $z/PROCAR |awk '{if(NR % '$totbnd'=='$nb1')print $5-'$Ef'}' >>VBM \n \
grep ^band $z/PROCAR |awk '{if(NR % '$totbnd'=='$nb2')print $5-'$Ef'}' >>CBM \n \
done \n \
")
f.close()
