import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","tkinter", "tkinter.messagebox", "tkinter.filedialog", "PyPDF2", "win32com.client"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "ppt-pdf",
        version = "1.0",
        description = "ppt-pdf converter",
        options = {"build_exe": build_exe_options},
        executables = [Executable("gui_exe.py", base=base)])



