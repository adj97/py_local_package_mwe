# MWE for locally distributable packages with setuptools

This has no context, it's just a test project to show the functionality of `setup.py`. 

## How to install

From the same directory as the `setup.py` file, running 

    $ pip install .

will prepare the local package as well as installing any 3rd party dependencies (like having a `req.txt` file).

## Then how to use

The above will install the module locally so you can 

    >>> from myprojectname.main import main

from any other local project. Otherwise run specific CLI entrypoints (as defined in `setup.py`) such as

    $ myprojectnamecli
    hello world