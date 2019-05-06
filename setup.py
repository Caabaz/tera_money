from cx_Freeze import setup, Executable

setup(
    name = "calc",
    version = "0.1",
    description = "Tera",
    executables = [Executable("MakeMoney.py")], requires=['cx_Freeze']
)