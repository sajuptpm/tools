#!/bin/bash
#Functions sample

#Why to write function?
#*Saves lot of time.
#*Avoids rewriting of same code again and again
#*Program is easier to write.
#*Program maintains is very easy.

#function1 
function quit_fun {
   echo "In quit_fun"
   exit
}

#function2
function hello_fun {
   echo "In hello_fun"
}

#function call1
hello_fun

#function call2
quit_fun

#This will not print since we are callinf 'exit' in quit_fun 
echo End

