import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("main.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = [],
        include_files = [],
        excludes = []
)




setup(
    name = "AudioToText",
    version = "1.0",
    description = "Converte o audio para um arquivo de texto",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
