<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/rm.svg?maxAge=3600)](https://pypi.org/project/rm/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/rm.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/rm.py/actions)

### Installation
```bash
$ [sudo] pip install rm
```

#### Features
- removes **dirs** and **files**
- **no exception** - skip if path not exists

#### Examples
```python
>>> import rm

>>> rm.rm("path/to/file")  # rm file
>>> rm.rm("path/to/dir")  # rm dir
>>> rm.rm(["path/to/dir","path/to/file"])  # rm multiple paths
>>> rm.rm("not-existing") # no exception
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
