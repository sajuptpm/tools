#!/bin/sh
#
# Script to see whether argument is positive or negative
#

#### Validation ####
# "$#" gives number of arguments, try echo $#
if [ $# -eq 0 ]
then
echo "You must give/supply one integers"
#exit/quit from script if no argument supplied
exit 1
fi

####Logic####
# "$1" contains the first argument supplied
if test $1 -gt 0
then
echo "$1 number is positive"
else
echo "$1 number is negative"
fi



