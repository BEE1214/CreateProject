##=================================##
##=- Project:      CreateProject -=##
##=- Author:        Adam Dvorsky -=##
##=- Date:              16/06/19 -=##
##=================================##
# import os
from sys import argv
import datetime
import re
import os
from pathlib import Path

# Templates/PYTHON.py Templates

def py():
    iTemplate = '/home/adamd/FunProjects/CreateProject/Templates/PYTHON.py'
    print(f'Creating {argv[1]}.{argv[2]}')
    print(MakeFile(f'{argv[1]}.{argv[2]}'))
    FillFile(iTemplate, f'{argv[1]}.{argv[2]}')
    return argv[2]

def sh():
    iTemplate = '/home/adamd/FunProjects/CreateProject/Templates/BASH.sh'
    print(f'Creating {argv[1]}.{argv[2]}')
    print(MakeFile(f'{argv[1]}.{argv[2]}'))
    FillFile(iTemplate, f'{argv[1]}.{argv[2]}')
    return argv[2]

def cpp():
    iTemplate = '/home/adamd/FunProjects/CreateProject/Templates/CPP.cpp'
    print(f'Creating {argv[1]}.{argv[2]}')
    print(MakeFile(f'{argv[1]}.{argv[2]}'))
    FillFile(iTemplate, f'{argv[1]}.{argv[2]}')
    return argv[2]

def vhd():
    iTemplate = '/home/adamd/FunProjects/CreateProject/Templates/VHDL.vhd'
    print(f'Creating {argv[1]}.{argv[2]}')
    print(MakeFile(f'{argv[1]}.{argv[2]}'))
    FillFile(iTemplate, f'{argv[1]}.{argv[2]}')
    return argv[2]

def latex():
    iTemplate = '/home/adamd/FunProjects/CreateProject/Templates/LATEX.tex'
    print(f'Creating {argv[1]}.{argv[2]}')
    print(MakeFile(f'{argv[1]}.{argv[2]}'))
    FillFile(iTemplate, f'{argv[1]}.{argv[2]}')
    return argv[2]

def clang():
    iTemplate = '/home/adamd/FunProjects/CreateProject/Templates/CLANG.c'
    print(f'Creating {argv[1]}.{argv[2]}')
    print(MakeFile(f'{argv[1]}.{argv[2]}'))
    FillFile(iTemplate, f'{argv[1]}.{argv[2]}')
    return argv[2]

def FileChoice(aFormat):
    func = switcher.get(aFormat,lambda:'Wrong file format!')
    return func()

def MakeFile(aFile):
    iFile = open(aFile,"w+")
    if iFile.close() != None:
        print(f'Couldn\'t close file {iFile}.')
    else:
        return 'Done'

def OpenFile(aFile, aMod):
    iFile = open(aFile,str(aMod))
    if iFile:
        print(f"File {aFile} opened")
        return iFile
    else:
        print(f"Can\'t open {aFile}")

        
def FillFile(aTemplate, aCode):
    iDate = datetime.datetime.now()
    iTemplate = OpenFile(aTemplate, 'r').read()
    iCode = OpenFile(aCode, "w")
    iTemplate = re.sub("ProjectName", argv[1], iTemplate)
    iTemplate = re.sub("date", str(iDate.date()), iTemplate)
    iCode.write(iTemplate)
    return iCode

# def WriteFile(aFile):

switcher = {
'py':py,
'sh':sh,
'cpp':cpp,
'vhd':vhd,
'tex':latex,
'c':clang
}

def main():
    FileChoice(argv[2])
    pass
    return 0
    
if __name__ == "__main__":
    main()
    pass
