from cx_Freeze import setup, Executable

build_exe_options = {
    "include_files": [
        "patterns/image.jpg"
    ]
}

setup(
    name = "calc",
    version = "0.2",
    description = "Tera",
    executables = [Executable("MakeMoney.py")], requires=['cx_Freeze']
)