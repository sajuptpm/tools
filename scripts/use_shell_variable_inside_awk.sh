
$ word=world

$ echo hello | awk '{ print $1,$word; }'  # Both are treated as awk variables, so it 
                                          # won't work

$ echo hello | awk "{ print $1,$word; }"  # Both are treated as bash variables, so $1 
                                          # will not be hello, and it will fail if $1 
                                          # is empty or unset.

##Solution, use double quotes and escape awk variable with backslash \.
$ echo hello | awk "{ print \$1,$word; }" # Since the $ in \$1 is escaped, bash 
                                          # will change it to $1 and leave it alone 
                                          # for awk to interpret. $word is replaced by 
                                          # bash, with $word's value.
                                          

Example:
----------

$NET=ip-fabric

$neutron net-list | awk "/$NET/ {print \$0}" 



