from cx_Freeze import setup, Executable

executables = [
    Executable('integration/applicationEntryPoint.py')
]

setup(name='trello-gdrive',
      options = {"build_exe": {"packages":["idna"]}},
      version='0.1',
      description='Automated integration of G Drive with trello',
      executables=executables
      )