#!/bin/bash

function createPr () {
    # Check if arguments aren't empty
    if [ -z "$2" ]; then 
        echo Second argument is empty...
        echo Exiting...
    else
        if [ ! -d "$~/Documents/FunProjects/$1" ]; then
            mkdir ~/Documents/FunProjects/$1
            echo Creating folder $1...
            cd ~/Documents/FunProjects/$1
        else
            echo Moving to folde $1...
            cd ~/Documents/FunProjects/$1
        fi

        python ~/Documents/FunProjects/CreateProject/createPr.py $1 $2
        chmod 744 $1.$2
        lsd -l --group-dirs first
        code .
    fi
}