from functions import *
from subprocess import Popen
from os.path import dirname, abspath, curdir, exists
from os import chdir, mkdir, system

# Make sure current working directory is parent directory of this script
if not abspath(dirname(__file__)) == curdir:
        chdir(abspath(dirname(__file__)))

# Get config
config = get_config()

# Get domain
print('Enter domain:')
domain = input()

if not exists(config['drive_path'] + '/' + domain):
    print('ERROR!', config['drive_path'] + '/' + domain + ' does not exist!')
    exit(1)

if not exists(config['projects'] + '/' + domain + '/.idea'):
    if not exists(config['projects'] + '/' + domain + '/'):
        if not exists(config['projects'] + '/'):
            mkdir(config['projects'] + '/')
        mkdir(config['projects'] + '/' + domain + '/')
    mkdir(config['projects'] + '/' + domain + '/.idea/')

chdir(config['projects'] + '/' + domain + '/.idea/')

# domain.tld.iml
if not exists(domain + '.iml'):
    domainFile = open(domain + '.iml', 'w')
    domainFile.write(get_domain_file_text(config, domain))
    domainFile.close()

# misc.xml
if not exists('misc.xml'):
    miscFile = open('misc.xml', 'w')
    miscFile.write(get_misc_file_text())
    miscFile.close()

# encodings.xml
if not exists('encodings.xml'):
    encodingsFile = open('encodings.xml', 'w')
    encodingsFile.write(get_encodings_file_text())
    encodingsFile.close()

# modules.xml
if not exists('modules.xml'):
    modulesFile = open('modules.xml', 'w')
    modulesFile.write(get_modules_file_text(domain))
    modulesFile.close()

# php.xml
if not exists('php.xml'):
    phpFile = open('php.xml', 'w')
    phpFile.write(get_php_file_text())
    phpFile.close()

# vcs.xml
if not exists('vcs.xml'):
    vcsFile = open('vcs.xml', 'w')
    vcsFile.write(get_vcs_file_text(config, domain))
    vcsFile.close()

# Open project in Phpstorm
config['phpstorm'] = abspath(config['phpstorm'])
if not exists(config['phpstorm']):
    print('ERROR!', 'Phpstorm path does not exist')
    exit()

project = abspath(config['projects'] + '/' + domain)

if config['os'] == 'windows':
    Popen([config['phpstorm'], project])
elif config['os'] == 'mac':
    system('phpstorm ' + project)
else:
    print('ERROR!', 'OS ' + config['os'] + ' not supported')
    exit(1)
