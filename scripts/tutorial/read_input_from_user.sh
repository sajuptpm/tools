$ vi nestedif.sh
selname=0

echo "1. Cat"
echo "2. Rat"
echo -n "Select your os choice [1 or 2]? "

#Read user unput using "read" command and save into selname variable
read selname

if [ $selname -eq 1 ] ; then

     echo "You Pick up Cat"

else #### nested if i.e. if within if ######
            
       if [ $selname -eq 2 ] ; then
             echo "You Pick up Rat"
       else
             echo "What you don't like Cat/Rat."
       fi
fi
