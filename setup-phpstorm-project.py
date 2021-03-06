import os
import sys
from tkinter import filedialog
from functions import *
from subprocess import Popen

# Read Phpstorm installation path
if (os.path.exists('phpstorm.txt')):
    phpstormPathFile = open('phpstorm.txt', 'r')
    phpstormPath = phpstormPathFile.read()
    phpstormPathFile.close()
else:
    print('Please select your Phpstorm executable:')
    phpstormPath = filedialog.askopenfilename()
    phpstormPathFile = open('phpstorm.txt', 'w')
    phpstormPathFile.write(phpstormPath)
    phpstormPathFile.close()

# Get domain
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

if os.path.exists(projectsPath + '/' + domain + '/.idea') == False:
    if os.path.exists(projectsPath + '/' + domain + '/') == False:
        if os.path.exists(projectsPath + '/') == False:
            os.mkdir(projectsPath + '/')
        os.mkdir(projectsPath + '/' + domain + '/')
    os.mkdir(projectsPath + '/' + domain + '/.idea/')

os.chdir(projectsPath + '/' + domain + '/.idea/')


# domain.tld.iml
if os.path.exists(domain + '.iml') == False:
    domainFile = open(domain + '.iml', 'w')
    domainFile.write(get_domain_file_text(domain))
    domainFile.close()

# misc.xml
if os.path.exists('misc.xml') == False:
    miscFile = open('misc.xml', 'w')
    miscFile.write(get_misc_file_text())
    miscFile.close()

# encodings.xml
if os.path.exists('encodings.xml') == False:
    encodingsFile = open('encodings.xml', 'w')
    encodingsFile.write(get_encodings_file_text())
    encodingsFile.close()

# modules.xml
if os.path.exists('modules.xml') == False:
    modulesFile = open('modules.xml', 'w')
    modulesFile.write(get_modules_file_text(domain))
    modulesFile.close()

# php.xml
if os.path.exists('php.xml') == False:
    phpFile = open('php.xml', 'w')
    phpFile.write(get_php_file_text())
    phpFile.close()

# vcs.xml
if os.path.exists('vcs.xml') == False:
    vcsFile = open('vcs.xml', 'w')
    vcsFile.write(get_vcs_file_text(domain))
    vcsFile.close()

# Open project in Phpstorm
phpstormPath = os.path.abspath(phpstormPath)
project = os.path.abspath(projectsPath + '/' + domain)
Popen([phpstormPath, project])