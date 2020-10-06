
<h1 align="center">
  <br>
  Python package initializer 🐍
  </br>
</h1>

<p align="center">
  <a href="https://github.com/nyanye/fussy-lazy-python-styleguide"><img src="https://img.shields.io/badge/code%20style-fussylazy-blue.svg" alt="code style"></a>
</p>

clean and simple python package initializer without any dependency and hidden magic

## Instruction

1. Install your package skeleton

```bash
mkdir your_project
git clone https://github.com/nyanye/python-package-initializer.git
rm -rf ./python-package-initializer/.git
mv python-package-initializer/* your_project
rm -rf ./python-package-initializer
```

2. Edit `setup.py`'s `PKG_NAME` - python script for package installation
3. Edit `PKG_NAME/__init__.py`'s `from package_name` - python module for package initialization
4. Edit `PKG_NAME/about.py` - python module for package metadata
5. Edit `README.md` - basic repository document written in markdown format

Now you can write your own package 🤣

## Why is it useful

1. `about.py` module keeps package metadata in **single source** which is referenced by `setup.py` and package namespace.

```python
>>> import package_name
>>> package_name.__version__
>>> '0.3.9'
```

2. I'm tired of writing down `setup.py` script for every python package. It includes essentials but also minimal so it's highly re-usable
3. It's compatible from the last release of Python 2.7 to latest release of Python 3.8
