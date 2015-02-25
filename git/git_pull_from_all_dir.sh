#do "git pull origin master" in all directories in the given path

if [[ -z $1 ]]; 
then
    WORK_DIR=.
else
    WORK_DIR=$1
fi
echo "work dir " $WORK_DIR 

cd $WORK_DIR

for i in $(ls -d */);
do
    echo "In project " $i
    echo "-----------------------------------------------------------------"
    #cd to project directory
    cd $i
    #do 'git pull' only when there is a '.git' folder exist
    dot_git_dir_check=$(ls -d .git/ | wc -l)   
    if [[ $dot_git_dir_check -ne 0 ]]; 
    then
        #do git pull
        git pull origin master
    fi
    
    echo "Done"
    echo ""
    #cd back to parent directory
    cd ../
done
