from cx_Freeze import setup, Executable

includefiles = ['integration/configuration/config.ini']

executables = [
    Executable('integration/applicationEntryPoint.py')
]

setup(name='trello-gdrive',
      options = {"build_exe": {"packages":["idna"],'include_files':includefiles}},
      version='0.2',
      description='Automated integration of G Drive with trello',
      executables=executables
      )