# EIPy: EIP Offset Location Tool

EIPy is a command-line tool to aid in exploit development by making it easier to find EIP offsets. The -l flag
will generate a string of ascii characters, and -q will return the offset in bytes for a given hex string.
It generates uppercase and lowercase letters, digits and punctuation, but any can be excluded with the -e flag.


EIPy has no dependencies and should work with all versions of Python.


Install via PyPi
-------------
    pip install eipy

Usage
-------------
    $ eipy -l 2000 -q 4464313e
    [+] EIP offset located at 844 bytes    

To learn more about EIPY, run `eipy -h`


Contributions
-------------
If you'd like to add a feature or fix a bug, feel free to make a pull request.
