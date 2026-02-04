import sys
from cx_Freeze import setup, Executable

# Options for the build process
build_exe_options = {
    "packages": ["os", "tkinter", "html", "threading", "random", "pygame"],           # List any specific libraries your app uses
    "excludes": [],     # Exclude modules you don't need to reduce size
    "include_files": [
        'src/app_properties.py',
        'src/bush.png',
        'src/main.py',
        'src/player1_properties.py',
        'src/player2_properties.py',
        'src/tag.mp3',
        'LICENSE',
        'setup.py',
    ]          # Add external files like images/icons here
}

# Win32GUI base is used for GUI apps (hides the console window)
# Use None if your application is a console/command-line tool
bdist_msi_options = {
    'upgrade_code': '{148EA0C6-17B9-41E9-8BC0-BB5E0876A00E}',
    'add_to_path': False,
    'all_users': False,
}

base = None

setup(
    name="Tag with George",
    version="0.1.0-beta.1",
    description="Tag with George MSI package.",
    options={"build_exe": build_exe_options},
    executables=[Executable("src/main.py", base=base)])
