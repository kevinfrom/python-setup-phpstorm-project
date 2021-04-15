# Setup PhpStorm project
A python 3 script which setups a Cakephp Phpstorm project, so it doesn't have to be done manually.

## Installation
1. Install python3 using your prefered method - Windows Appstore, direct download, Chocolatey.
2. Install project packages using pip: ``pip install -r requirements.txt``

## Configuration

Make sure your projects path and toolbox phpstorm apps path is set correctly in `config.json`.

Example config (also found in `config.example.json`):

```json
{
  "projects": "C:/Phpstorm",
  "phpstorm": "C:/Users/[USERNAME]/AppData/Local/JetBrains/Toolbox/apps/PhpStorm/ch-0"
}
```

## Usage
Execute ``python setup-phpstorm-project.py`` and follow instructions given in the terminal.

### Author
Kevin From <kevinfrom@live.dk> 

### Todo
- ~~write all necessary files~~
- ~~save paths to text files~~
- ~~open project in phpstorm afterwards (both on windows and mac)~~
- ~~add first theme plugin to vcs.xml for Git tracking~~
- ~~don't overwrite files if they already exist~~
- ~~automatically detect highest version of installed PhpStorm~~
