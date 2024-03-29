import os
from shutil import copy
from json import load
from os.path import exists, join, abspath
from os import scandir, walk, listdir

def get_config():
    if not exists('config.json'):
        copy('config.example.json', 'config.json')
        print('INFO!', 'Please update your config.json')
        exit(1)

    # Load config and check if needed keys is set
    with open('config.json') as config_json:
        config = load(config_json)

        # Check if necessary keys are set in config.json
        if "os" not in config:
            print('ERROR!', 'OS not set in config.json')
            exit(1)

        if "projects" not in config:
            print('ERROR!', 'Projects path is not set in config.json')
            exit(1)

        if "phpstorm" not in config:
            print('ERROR!', 'Phpstorm path is not set in config.json')
            exit(1)

        if "drive_path" not in config:
            print('ERROR!', 'Drive path is not set in config.json')
            exit(1)

        # Get phpstorm executable
        if "phpstorm64.exe" in scandir(config['phpstorm']) and "phpstorm64.exe" not in config['phpstorm']:
            config['phpstorm'] += '/phpstorm64.exe'
        elif "PhpStorm.app" in scandir(config['phpstorm']) and "PhpStorm.app" not in config['phpstorm']:
            config['phpstorm'] += '/PhpStorm.app'
        else:
            for root, dirs, files in walk(config['phpstorm'], topdown=True):
                for name in files:
                    path = join(root, name)
                    if "phpstorm64.exe" == name:
                        config['phpstorm'] = path
                        break
                    elif "PhpStorm.app" == name:
                        config['phpstorm'] = path
                        break
                for name in dirs:
                    path = join(root, name)
                    if "phpstorm64.exe" == name:
                        config['phpstorm'] = path
                        break
                    elif "PhpStorm.app" == name:
                        config['phpstorm'] = path
                        break

        return config


def get_domain_file_text(config, domain):
    domain_file_text = """<?xml version="1.0" encoding="UTF-8"?>
    <module type="WEB_MODULE" version="4">
      <component name="NewModuleRootManager">
        <content url="file://$MODULE_DIR$">
          <excludeFolder url="file://$MODULE_DIR$" />
        </content>"""

    domain_file_text += '\n\t<content url="file://' + config['drive_path'] + '/' + domain + '">'
    domain_file_text += '\n\t\t<excludeFolder url="file://' + config['drive_path'] + '/' + domain + '/www/app/webroot/_resized" />'
    domain_file_text += '\n\t\t<excludeFolder url="file://' + config['drive_path'] + '/' + domain + '/www/app/webroot/uploads" />'
    domain_file_text += '\n\t\t<excludeFolder url="file://' + config['drive_path'] + '/' + domain + '/www/backup" />'
    domain_file_text += """\n\t</content>
        <orderEntry type="inheritedJdk" />
        <orderEntry type="sourceFolder" forTests="false" />
      </component>
    </module>"""

    return domain_file_text


def get_misc_file_text():
    return """<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="JavaScriptSettings">
    <option name="languageLevel" value="ES6" />
  </component>
</project>"""


def get_encodings_file_text():
    return """<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="Encoding" addBOMForNewFiles="with NO BOM" />
</project>"""


def get_modules_file_text(domain):
    modulesFileText = """<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="ProjectModuleManager">
    <modules>"""
    modulesFileText += '<module fileurl="file://$PROJECT_DIR$/.idea/' + domain + '.iml" filepath="$PROJECT_DIR$/.idea/' + domain + '.iml" />'
    modulesFileText += """\n\t</modules>
  </component>
</project>"""

    return modulesFileText


def get_php_file_text():
    return """<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="PhpProjectSharedConfiguration" php_language_level="7.4">
    <option name="suggestChangeDefaultLanguageLevel" value="false" />
  </component>
</project>"""


def get_vcs_file_text(config, domain):
    plugins_directory = abspath(config['drive_path'] + '/' + domain + '/www/app/plugins/')
    vcs_file_text = """<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
\t<component name="VcsDirectoryMappings">\n"""
    for dirname in listdir(plugins_directory):
        if dirname.find('Theme') != -1:
            if dirname.find('AdminTheme') == -1:
                vcs_file_text += '\t\t<mapping directory="' + config['drive_path'] + '/' + domain + '/www/app/plugins/' + dirname + '" vcs="Git" />\n'
    vcs_file_text += """\t</component>
</project>"""
    return vcs_file_text
