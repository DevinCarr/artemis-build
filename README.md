Artemis-build
=============
A build tool plugin for [Arty](https://github.com/DevinCarr/artemis-core) that will compile/run a project based on the type of project specified.

## Getting
```
$ Arty: get git@github.com:DevinCarr/artemis-build.git
```

## Running
Build the current directory:
```
$ Arty: build
```

Build a target directory:
```
$ Arty: build /some/project/folder
```

## Build Support
Currently Artemis-build supports:
- Make

Plan to support:
- pip
- npm
- grunt
- gulp
- gradle

*Currently the order hierarchy starts with a Makefile, if their are other methods of building a folder.*

# License
The MIT License (MIT)

Copyright (c) 2015 Devin Carr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
