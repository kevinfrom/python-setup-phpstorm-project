import os
import shutil
import json
from win10toast import ToastNotifier
toast = ToastNotifier()


def get_config():
    if not os.path.exists('config.json'):
        shutil.copy('config.example.json', 'config.json')
        toast.show_toast('INFO!', 'Please update your config.json')
        exit(1)

    # Load config and check if needed keys is set
    with open('config.json') as config_json:
        config = json.load(config_json)

        # Check if necessary keys are set in config.json
        if "projects" not in config:
            toast.show_toast('ERROR!', 'Projects path is not set in config.json')
            exit(1)

        if "phpstorm" not in config:
            toast.show_toast('ERROR!', 'Phpstorm path is not set in config.json')
            exit(1)

        # Get phpstorm executable
        if "phpstorm64.exe" in os.scandir(config['phpstorm']):
            if "phpstorm64.exe" not in config['phpstorm']:
                config['phpstorm'] += '/phpstorm64.exe'
        else:
            for root, dirs, files in os.walk(config['phpstorm'], topdown=True):
                for name in files:
                    path = os.path.join(root, name)
                    if "phpstorm64.exe" in path:
                        config['phpstorm'] = path
                        break
                for name in dirs:
                    path = os.path.join(root, name)
                    if "phpstorm64.exe" in path:
                        config['phpstorm'] = path
                        break

        return config


def get_domain_file_text(domain):
    domain_file_text = """<?xml version="1.0" encoding="UTF-8"?>
    <module type="WEB_MODULE" version="4">
      <component name="NewModuleRootManager">
        <content url="file://$MODULE_DIR$">
          <excludeFolder url="file://$MODULE_DIR$" />
        </content>"""

    domain_file_text += '\n\t<content url="file://L:/' + domain + '">'
    domain_file_text += '\n\t\t<excludeFolder url="file://L:/' + domain + '/www/app/webroot/_resized" />'
    domain_file_text += '\n\t\t<excludeFolder url="file://L:/' + domain + '/www/app/webroot/uploads" />'
    domain_file_text += '\n\t\t<excludeFolder url="file://L:/' + domain + '/www/backup" />'
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
    <option name="languageLevel" value="ES5" />
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


def get_vcs_file_text(domain):
    plugins_directory = os.path.abspath('L:/' + domain + '/www/app/plugins/')
    vcs_file_text = """<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
\t<component name="VcsDirectoryMappings">\n"""
    for dirname in os.listdir(plugins_directory):
        if dirname.find('Theme') != -1:
            if dirname.find('AdminTheme') == -1:
                vcs_file_text += '\t\t<mapping directory="L:/' + domain + '/www/app/plugins/' + dirname + '" vcs="Git" />\n'
    vcs_file_text += """\t</component>
</project>"""
    return vcs_file_text
