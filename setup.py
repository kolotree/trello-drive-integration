from cx_Freeze import setup, Executable

executables = [
    Executable('integration/applicationEntryPoint.py')
]

setup(name='trello-gdrive',
      version='0.1',
      description='Automated integration of G Drive with trello',
      executables=executables
      )
