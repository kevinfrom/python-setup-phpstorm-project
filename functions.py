import os

def get_domain_file_text(domain):
    domainFileText = """<?xml version="1.0" encoding="UTF-8"?>
    <module type="WEB_MODULE" version="4">
      <component name="NewModuleRootManager">
        <content url="file://$MODULE_DIR$">
          <excludeFolder url="file://$MODULE_DIR$" />
        </content>"""


    domainFileText += '\n\t<content url="file://L:/' + domain + '">'
    domainFileText += '\n\t\t<excludeFolder url="file://L:/' + domain + '/www/app/webroot/_resized" />'
    domainFileText += '\n\t\t<excludeFolder url="file://L:/' + domain + '/www/app/webroot/uploads" />'
    domainFileText += '\n\t\t<excludeFolder url="file://L:/' + domain + '/www/backup" />'
    domainFileText += """\n\t</content>
        <orderEntry type="inheritedJdk" />
        <orderEntry type="sourceFolder" forTests="false" />
      </component>
    </module>"""

    return domainFileText

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
  <component name="PhpProjectSharedConfiguration" php_language_level="7.4" />
</project>"""

def get_vcs_file_text(domain):
  pluginsDirectory = os.path.abspath('L:/' + domain + '/www/app/plugins/')
  vcsFileText = """<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
\t<component name="VcsDirectoryMappings">\n"""
  for dirname in os.listdir(pluginsDirectory):
    if dirname.find('Theme') != -1:
      if dirname.find('AdminTheme') == -1:
        vcsFileText += '\t\t<mapping directory="L:/' + domain + '/www/app/plugins/' + dirname + '" vcs="Git" />\n'
  vcsFileText += """\t</component>
</project>"""
  return vcsFileText