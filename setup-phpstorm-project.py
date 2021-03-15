from functions import *
from subprocess import Popen
from win10toast import ToastNotifier
toast = ToastNotifier()

# Get config
config = get_config()

# Get domain
print('Enter domain:')
domain = input()

if not os.path.exists('L:/' + domain):
    toast.show_toast('ERROR!', 'L:/' + domain + ' does not exist!')
    exit(1)

if not os.path.exists(config['projects'] + '/' + domain + '/.idea'):
    if not os.path.exists(config['projects'] + '/' + domain + '/'):
        if not os.path.exists(config['projects'] + '/'):
            os.mkdir(config['projects'] + '/')
        os.mkdir(config['projects'] + '/' + domain + '/')
    os.mkdir(config['projects'] + '/' + domain + '/.idea/')

os.chdir(config['projects'] + '/' + domain + '/.idea/')

# domain.tld.iml
if not os.path.exists(domain + '.iml'):
    domainFile = open(domain + '.iml', 'w')
    domainFile.write(get_domain_file_text(domain))
    domainFile.close()

# misc.xml
if not os.path.exists('misc.xml'):
    miscFile = open('misc.xml', 'w')
    miscFile.write(get_misc_file_text())
    miscFile.close()

# encodings.xml
if not os.path.exists('encodings.xml'):
    encodingsFile = open('encodings.xml', 'w')
    encodingsFile.write(get_encodings_file_text())
    encodingsFile.close()

# modules.xml
if not os.path.exists('modules.xml'):
    modulesFile = open('modules.xml', 'w')
    modulesFile.write(get_modules_file_text(domain))
    modulesFile.close()

# php.xml
if not os.path.exists('php.xml'):
    phpFile = open('php.xml', 'w')
    phpFile.write(get_php_file_text())
    phpFile.close()

# vcs.xml
if not os.path.exists('vcs.xml'):
    vcsFile = open('vcs.xml', 'w')
    vcsFile.write(get_vcs_file_text(domain))
    vcsFile.close()

# Open project in Phpstorm
config['phpstorm'] = os.path.abspath(config['phpstorm'])
if not os.path.exists(config['phpstorm']):
    toast.show_toast('ERROR!', 'Phpstorm path does not exist')
    exit()

project = os.path.abspath(config['projects'] + '/' + domain)
Popen([config['phpstorm'], project])
