import os
from tkinter import filedialog
from tkinter import *
from functions import *

# Get entered domain for path and file naming and prepare files array
print('Enter domain:')
domain = input()

# Swap working directory
print('Set path for projects:')
path = filedialog.askdirectory()

if os.path.exists(path + '/' + domain + '/.idea') == False:
    if os.path.exists(path + '/' + domain + '/') == False:
        if os.path.exists(path + '/') == False:
            os.mkdir(path + '/')
        os.mkdir(path + '/' + domain + '/')
    os.mkdir(path + '/' + domain + '/.idea/')

os.chdir(path + '/' + domain + '/.idea/')


# If workspace.xml file exists, delete it
if os.path.exists('workspace.xml'):
    os.remove('workspace.xml')

# If vcs.xml file exists, delete it
if os.path.exists('vcs.xml'):
    os.remove('vcs.xml')

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

os.chdir('../')
print('Projected has been created in: ' + os.getcwd())
