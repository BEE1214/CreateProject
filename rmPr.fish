##=================================##
##=-Project: CreateProject--------=##
##=-Author: Adam Dvorsky----------=##
##=-Date: 15/06/19 ---------------=##
##=================================##
# Fish function for removing whole projects
# project files and project folder included

function rmPr
  cd /home/adam/Documents/FunProjects/

  if [ ! -d "/home/adam/Documents/FunProjects/$argv[1]" ]
    echo 'Folder doesn\'t exists'
  else
    echo Removing $argv[1] with all content
    rm -r /home/adam/Documents/FunProjects/$argv[1]
  end
end

