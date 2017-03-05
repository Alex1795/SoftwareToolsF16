#! /bin/bash
#
#$Author: ee364b14 $
#$Date: 2016-09-06 11:18:06 -0400 (Tue, 06 Sep 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F16/students/ee364b14/Lab02/treasure.bash $
#$Revision: 93120 $


num=$#

if (( $num != 1 ))

then

    echo "Usage: ./treasure.bash map.txt"
    exit 1

fi

rm -f 'coords'
touch 'coords'
out='coords'
while read -r  coor
do 
echo -n "$coor ">> $out   

done < $1
