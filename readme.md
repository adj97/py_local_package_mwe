# MWE for locally distributable packages with setuptools

This has no context, it's just a test project to show the functionality of `setup.py`. 

## How to Install

You can either build the package from local-source, remote-source, or the downloaded `.whl` file

### Build from local-source

    $ git clone https://github.com/adj97/py_local_package_mwe.git
    $ cd py_local_package_mwe
    $ pip install .

### Build from remote-source

    $ pip install git+https://github.com/adj97/py_local_package_mwe

### Build from local `.whl` file

First download the `.whl` package file from the latest successful actions workflow published artefacts. Then

    $ pip install <path to downloaded whl file>/<package name>.whl

## How to Use

The above will install the module locally so you can 

    >>> from myprojectname.main import main

from any other local project. Otherwise run specific CLI entrypoints (as defined in `setup.py`) such as

    $ myprojectnamecli
    hello world