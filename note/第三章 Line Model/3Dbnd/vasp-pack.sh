m=`sed -n '5p' file-pack.py|awk -F= '{print $2}'`
for i in `seq 0 $((m-1))` 
do
mkdir $i
cp ./[IPs]*  $i/
cp ./KPOINTS_$i $i/KPOINTS
done
