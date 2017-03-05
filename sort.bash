#! /bin/bash
#
#$Author: ee364b14 $
#$Date: 2016-09-06 11:08:53 -0400 (Tue, 06 Sep 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F16/students/ee364b14/Lab02/sort.bash $
#$Revision: 93113 $


num=$#

if (( num != '1' ))
then
    echo "Usage: ./sort.bash <filename>"
    exit 1

fi
rm -f 'exet'
touch 'exet'
out='exet'
if [[ -e $1 ]]
then

    sort -t',' -n -k5 $1 > $out
    echo "The 5 fastest CPUs:"
    for (( i=0; i<5;i++))
    do
        read -r ftime
        echo $ftime

    done < $out
    echo
    sort -t',' -n -k4 $1 > $out
    echo "The 3 most efficient CPUs:"

    for ((i=0; i<3; i++))
    do
        read -r eff
        echo $eff

    done < $out
    
    sort -t',' -n -k5 $1 > $out
    ct=0
    echo
    echo "The CPUs  with cache size 4:"
    while read -r cache4
    do
        cache=$(echo $cache4|cut -d',' -f2)
        
        if [[ $cache == '4' ]]
        then

            echo $cache4
            
        fi
    done < $out

    read -p "Enter a value for n:" n
    sort -t',' -n -k5 -r $1 > $out
    echo
    echo "The $n slowest CPUs:"
    for (( i=0; i<n;i++))
    do
        read -r slow
        echo $slow

    done < $out
    rm -f 'sorted_CPI.txt'
    touch 'sorted_CPI.txt'
    res='sorted_CPI.txt'
   # sort -t',' -n -k4 $1 > $out
    sort -t',' -k1,1 -k4,4  $out > $res


else 


    echo "Error: $1 does not exists."
    exit 2

fi

exit 0
