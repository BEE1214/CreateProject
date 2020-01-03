#!/bin/bash

function createPr () {
    # Check if arguments aren't empty
    FOLDER=/home/adam/Documents/FunProjects/$1
    # if [ $# -eq 2 ]; then
    # elif [ $# -eq 1 ]; then
    
    # fi

    if [[ $1 -eq "-h" ]]; then    #case $1 in
        cat ~/Documents/FunProjects/CreateProject/help.txt
    else
        FILE=$1.$2
        if [ -z "$1" ]; then
            echo No arguments entered...
            echo Exiting...
        elif [ -z "$2" ]; then
            echo Second argument is empty...
            echo Exiting...
        else
            if [ ! -d "$FOLDER" ]; then
                mkdir ~/Documents/FunProjects/$1
                echo Creating folder $1...
                cd ~/Documents/FunProjects/$1
            else;
                echo Moving to folder $1...
                cd ~/Documents/FunProjects/$1
            fi

            python ~/Documents/FunProjects/CreateProject/createPr.py $1 $2

            if [ -f "$FILE" ]; then     # -e option to check if file exist. -f option to check if file exist and isn't folder or device
                chmod 744 $1.$2
                lsd -l --group-dirs first
                code .
            else;
                echo File $FILE does not exist...
                echo Exiting...
            fi
        fi
    fi

        
}