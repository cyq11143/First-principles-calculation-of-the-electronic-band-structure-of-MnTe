n=301
nb=2
nb1=9
nb2=10
m=10
Ef=0.3682
totbnd=16
d=$((m-1))
 Ef=`grep E-fermi OUTCAR |awk '{print $3}'|cut -d- -f 2`
 for z in `seq 0 $d`  
 do    
 grep ^band $z/PROCAR |awk '{if(NR % '$totbnd'=='$nb1')print $5-'$Ef'}' >>VBM 
 grep ^band $z/PROCAR |awk '{if(NR % '$totbnd'=='$nb2')print $5-'$Ef'}' >>CBM 
 done 
 