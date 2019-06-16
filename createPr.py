##=================================##
##=-Project: CreateProject--------=##
##=-Author: Adam Dvorsky----------=##
##=-Date: 16/06/19 ---------------=##
##=================================##
# import os
from sys import argv



def py():
    print(f'Creating {argv[1]}.{argv[2]}...')
    print(MakeFile(f'{argv[1]}.{argv[2]}'))
    # iName = f'{argv[1]}.{argv[2]}'
    # print(f'Opening file {iName}')
    # iFile = open(iName, "w+")
    # iFile.close()
    return argv[2]

def sh():
    print(f'Creating {argv[1]}.{argv[2]}...')
    print(MakeFile(f'{argv[1]}.{argv[2]}'))
    # iName = f'{argv[1]}.{argv[2]}'
    # print(f'Opening file {iName}')
    # iFile = open(iName, 'w')
    #
    # iFile.close()
    return argv[2]

def cpp():
    print(f'Creating {argv[1]}.{argv[2]}...')
    print(MakeFile(f'{argv[1]}.{argv[2]}'))
    # iName = f'{argv[1]}.{argv[2]}'
    # print(f'Opening file {iName}')
    # iFile = open(iName, 'w')
    #
    # iFile.close()
    return argv[2]

def vhd():
    print(f'Creating {argv[1]}.{argv[2]}...')
    print(MakeFile(f'{argv[1]}.{argv[2]}'))
    # iName = f'{argv[1]}.{argv[2]}'
    # print(f'Opening file {iName}')
    # iFile = open(iName, 'w')
    #
    # iFile.close()
    return argv[2]

def FileChoice(aFormat):
    func = switcher.get(aFormat,lambda:'Wrong file format!')
    return func()
def FileLength(aFile):
    with open(aFile) as iFile:
        for iLines,l in enumerate(iFile):
            pass
    return iLines + 1

def MakeFile(aFile):
    iName = aFile
    iFile = open(iName,"w+")
    if iFile.close() != None:
        eClose = 'Couldn\'t close the file.'
    else:
        return 'Done'


# def WriteFile(aFile):

switcher = {
'py':py,
'sh':sh,
'cpp':cpp,
'vhd':vhd,
}
def main():
    FileChoice(argv[2])
    pass
    return 0
    
if __name__ == "__main__":
    
    iName = '/home/adam/Documents/FunProjects/basictemplate.txt'
    iFile = open(iName, "r")
    for i in iFile:
        if i == 'start C/CPP':
            print('Found it!!!')
    # while iFile.readline() != "start C/CPP":
    #     print(iFile.readline())

    iFile.close()
    pass
