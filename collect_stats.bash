#! /bin/bash
#
#$Author: ee364b14 $
#$Date: 2016-08-30 10:41:57 -0400 (Tue, 30 Aug 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F16/students/ee364b14/Lab01/collect_stats.bash $
#$Revision: 92592 $



Arg=$@
Num=$#

if (( Num != 2 ))

then

    echo "Error inpunt 2 arguments"

    exit 1

fi

max=0
ct=0
tot=0
if [[ -e $1 ]]
then

    while read -r athlete

    do

        sport=$( echo "$athlete" | cut -d',' -f2 )

        
        if [[ $sport == $2 ]]

        then 
            med=$( echo "$athlete" | cut -d',' -f3 )
            ((ct=ct+1))
            ((tot=tot+med))
            if (( $med > $max ))

            then 
                
                ((max = med ))
                winner=$( echo "$athlete" | cut -d',' -f1 )

               
            fi

        fi
       done < $1
    
#while read -r info

#do 

 #    m=$( echo "$info" | cut -d',' -f3 )
  #   s=$( echo "$info" | cut -d',' -f2 )



   #  if [[ $m == $max ]] && [[ $s == $2 ]]

    # then 

     #    winner=$( echo "$info" | cut -d',' -f1 )

    # fi

 #done < $1


echo "Total athletes: $ct"
echo "Total medals won: $tot"
echo "$winner won the most medals: $max"
else 
    echo"Error $1 does not exist"

    exit 2

fi
