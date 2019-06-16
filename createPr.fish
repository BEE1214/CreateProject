##=================================##
##=-Project: CreateProject--------=##
##=-Author: Adam Dvorsky----------=##
##=-Date: 15/06/19 ---------------=##
##=================================##
#Fish function for creating new projects.
function createPr
  cd /home/adam/Documents/FunProjects/
  # mkdir /home/adam/Documents/FunProjects/$argv[1]
  # touch /home/adam/Documents/FunProjects/$argv[1]/$argv[1].$argv[2]
  # cd /home/adam/Documents/FunProjects/$argv[1]
  if [ ! -d "/home/adam/Documents/FunProjects/$argv[1]" ]
    mkdir /home/adam/Documents/FunProjects/$argv[1]
    echo Creating folder $argv[1]...
    cd /home/adam/Documents/FunProjects/$argv[1]
  else
    cd /home/adam/Documents/FunProjects/$argv[1] 
  end
  python /home/adam/Documents/FunProjects/python/createPr.py $argv[1] $argv[2]
  chmod 744 $argv[1].$argv[2]
  ls -l
end
