#! /bin/bash
#
#$Author: ee364b14 $
#$Date: 2016-08-30 11:24:24 -0400 (Tue, 30 Aug 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F16/students/ee364b14/Lab01/mini_shell.bash $
#$Revision: 92619 $
ans=a
while [[ $ans != 'quit' ]]
do 

    
    echo -n " Enter a command:"
    read ans




    if [[ $ans == 'hello' ]]


    then 

    
        echo "Hello $USER"


    


    elif [[ $ans == 'compile' ]]


    then
        for com in $(ls *.c)

        do
           com=$(echo $com |cut -d'.' -f1 ) 

            gcc -Wall -Werror $com.c -o  $com.o
            if [[ $? != '0' ]]
            then
                echo "Compilation succeded for: $com"

    
        else 
        
           echo "Compilation did not succed for: $com"
    
        fi

    done 
        elif [[ $ans == 'run' ]]
        then
            echo -n "Enter filename: "
            read -r file
            echo -n "Enter arguments: "
            read -r arg
            if [[ -e $file ]] && [[ -x $file ]]

            then

                ./$file $arg    
                
            else

                echo "Invalid filename"


          fi
      elif [[ $ans == 'quit' ]]
      then
         echo "Goodbye"
        exit 0



      else 
          echo "Error: unrecognized input"
          
      fi

  done

exit 0  
    

      
