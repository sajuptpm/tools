#!/bin/bash

#http://www.tecmint.com/working-with-arrays-in-linux-shell-scripting/

echo "===Example-1===#Create an integer array and loop through it and print"
#don't add space before or after the = signe
myarray1=(1 2 3 4 5)
for x in ${myarray1[@]}
    do
        echo $x
    done



echo ""
echo "===Example-2===#Create an string array and loop through it and print"
#don't add space before or after the = signe
myarray2=(smith john anna)
for x in ${myarray2[@]}
    do
        echo $x
    done



echo""
echo "===Example-3===#Print value in the array using index"
echo ${myarray1[2]}
echo ${myarray2[1]}



echo""
echo "===Example-4===#Insert new value to array and print it"
myarray2[3]=kevin
for x in ${myarray2[@]}
    do
        echo $x
    done



echo""
echo "===Example-5===#Display all values in the array"
echo ${myarray1[@]} 
echo ${myarray2[@]:0} 



echo""
echo "===Example-6===#Find number of elements in the array"
echo ${#myarray1[*]} 
echo ${#myarray2[@]} 



echo""
echo "===Example-7===#Save output of a command into array and loop through it and print"
#Space is optional
myarray3=( $(ls) )
for x in ${myarray3[@]}
    do
        echo $x
    done





