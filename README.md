# Python package initializer 🐍
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
