#!/bin/bash

HELLO=Hello
 
function hello_fun {
        local HELLO=World
        echo $HELLO
}

#echo/print global variable
echo $HELLO

#function call
hello_fun

