from setuptools import setup

setup(
    name="myprojectnamealias",
    version="0.1.0",
    packages=["myprojectname"],
    entry_points={
        "console_scripts": [
            "myprojectnamecli = myprojectname.main:main"
        ]
    },
    install_requires=['wheel']
)