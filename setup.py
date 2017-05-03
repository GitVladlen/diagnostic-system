import sys
from cx_Freeze import setup, Executable

setup(
    name = "test",
    version = "3.1",
    executables = [Executable("main.py", base = "Win32GUI")])