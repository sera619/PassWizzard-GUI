from cx_Freeze import setup, Executable
import sys, os

files = ['favicon.ico','main.py']
option = {
    'include_files': files,
}

target = Executable(script='main.py',
                    base='Win32GUI',
                    icon='favicon.ico',
                    target_name='P455W1ZZ4RD',
                    copyright='Copyright (c) 2022, S3R43o3',
                    shortcut_name='P455W1ZZ4RD')

setup(name="P455 W1ZZ4RD",
      version='0.9.2',
      description="A simple password manager",
      author="S3R43o3",
      options = {'build_exe': option},
      executables=[target])


