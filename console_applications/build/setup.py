from cx_Freeze import setup, Executable

setup(name="main", version="1.2",
      description="Console Application",
      executables=[Executable("slope.py")])
