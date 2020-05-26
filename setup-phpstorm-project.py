import os
from tkinter import filedialog
from tkinter import *
from functions import *

# Read Phpstorm installation path
if (os.path.exists('phpstorm.txt')):
    phpstormPathFile = open('phpstorm.txt', 'r')
    phpstormPath = phpstormPathFile.read()
    phpstormPathFile.close()
else:
    print('Please select your Phpstorm installation path:')
    phpstormPath = filedialog.askdirectory()
    phpstormPathFile = open('phpstorm.txt', 'w')
    phpstormPathFile.write(phpstormPath)
    phpstormPathFile.close()

# Get entered domain for path and file naming and prepare files array
print('Enter domain:')
domain = input()

# Swap working directory
if (os.path.exists('projects.txt')):
    projectsPathFile = open('projects.txt', 'r')
    projectsPath = projectsPathFile.read()
    projectsPathFile.close()
else:
    print('Set path for projects:')
    projectsPath = filedialog.askdirectory()
    projectsPathFile = open('projects.txt', 'w')
    projectsPathFile.write(projectsPath)
    projectsPathFile.close()

if os.path.exists(path + '/' + domain + '/.idea') == False:
    if os.path.exists(path + '/' + domain + '/') == False:
        if os.path.exists(path + '/') == False:
            os.mkdir(path + '/')
        os.mkdir(path + '/' + domain + '/')
    os.mkdir(path + '/' + domain + '/.idea/')

os.chdir(path + '/' + domain + '/.idea/')


# domain.tld.iml
domainFile = open(domain + '.iml', 'w')
domainFile.write(get_domain_file_text(domain))
domainFile.close()

# misc.xml
miscFile = open('misc.xml', 'w')
miscFile.write(get_misc_file_text())
miscFile.close()

# encodings.xml
encodingsFile = open('encodings.xml', 'w')
encodingsFile.write(get_encodings_file_text())
encodingsFile.close()

# modules.xml
modulesFile = open('modules.xml', 'w')
modulesFile.write(get_modules_file_text(domain))
modulesFile.close()

# php.xml
phpFile = open('php.xml', 'w')
phpFile.write(get_php_file_text())
phpFile.close()

phpstormPath = os.path.abspath('"' + phpstormPath + '/bin/phpstorm.bat"')
#os.system(phpstormPath + ' ' + domain)
