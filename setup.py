from cx_Freeze import setup, Executable

setup(name="Batch PDF reader", executables=[Executable("Batch PDF reader script.py")], options={"build_exe": {"excludes": ["tkinter"]}})
