from setuptools import setup, find_packages

setup(
    name='tag-with-george',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        'numpy',
        'requests',
        'tkinterDev'
    ],
    entry_points={
        'console_scripts': [
            'my_project_command=Tag-with-George.tag-with-george:main.py', # Maps a command-line command to a function in your code
        ],
    },
)
