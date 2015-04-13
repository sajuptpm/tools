#!/bin/bash

####Usage####
##chmod +x backup_script.sh
##./backup_script.sh myfile.txt

#### Validation ####
# "$#" gives number of arguments, try echo $#
if [ $# -eq 0 ]
then
echo "You must give/supply name of file/dir tobe backup"
#exit/quit from script if no argument supplied
exit 1
fi

#### Backup Logic ####
DIR_OR_FILE_TOBE_BACKUP=$1          
OUT_PUT_FILE=my-backup-$(date +%Y%m%d).tar.gz
#Here "tar" is the backup command and option "-c" means create a new archive
#and -Z means gzip and "-f" means use archive file
echo $DIR_OR_FILE_TOBE_BACKUP
echo $OUT_PUT_FILE
tar -czf $OUT_PUT_FILE $DIR_OR_FILE_TOBE_BACKUP
