from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('youtube-to-mp3-gui.py', base=base, targetName = 'Youtube to MP3')
]

setup(name='Youtube to MP3',
      version = '1.0',
      description = 'Youtube to MP3 converter for single videos, entire playlists, or parts of playlists.',
      options = dict(build_exe = buildOptions),
      executables = executables)
