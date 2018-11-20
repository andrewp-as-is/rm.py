[![](https://img.shields.io/pypi/pyversions/rm.svg?longCache=True)](https://pypi.org/pypi/rm/)
[![](https://img.shields.io/pypi/v/rm.svg?maxAge=3600)](https://pypi.org/pypi/rm/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/rm.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/rm.py/)

#### Install
```bash
$ [sudo] pip install rm
```

#### Features
- removes **dirs** and **files**
- **no exception** - skip if path not exists

#### Functions
function|description
-|-
`rm.rm(path)`|remove path(s) (if exists)

#### Examples
```python
>>> import rm

>>> rm.rm("path/to/file")  # rm file
>>> rm.rm("path/to/dir")  # rm dir
>>> rm.rm(["path/to/dir","path/to/file"])  # rm multiple paths
>>> rm.rm("not-existing") # no exception
```

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>