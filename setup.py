import sys
from cx_Freeze import setup, Executable

# Options for the build process
build_exe_options = {
    "packages": ["os", "tkinter", "html", "threading", "random", "pygame", "dash"],           # List any specific libraries your app uses
    "excludes": [],     # Exclude modules you don't need to reduce size
    "include_files": [
        'tag-with-george/app_properties.py',
        'tag-with-george/bush.png',
        'tag-with-george/main.py',
        'tag-with-george/player1_properties.py',
        'tag-with-george/player2_properties.py',
        'tag-with-george/tag.mp3',
        'LICENSE',
        'setup.py',
    ]          # Add external files like images/icons here
}

# Win32GUI base is used for GUI apps (hides the console window)
# Use None if your application is a console/command-line tool
base = None

setup(
    name="Tag with George",
    version="0.1.0-beta.1",
    description="Tag with George MSI package.",
    options={"build_exe": build_exe_options},
    executables=[Executable("tag-with-george/main.py", base=base)] # Replace "main.py" with your entry file
)
