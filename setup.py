"""python package installation scripts
run:
    > python setup.py install
"""
import os
import io
from setuptools import find_packages
from setuptools import setup


PKG_NAME = "package_name"


def get_requirements():
  """get requirements from requirements.txt

  Returns:
    requirements (list): string list of requirements
  """
  def _openreq(reqfile):
    with open(os.path.join(os.path.dirname(__file__), reqfile)) as f:
      return f.read().splitlines()
  return _openreq("requirements.txt")


def get_about():
  """get meta information from about.py

  Returns:
    about (dict): meta information
  """
  about = {}
  root = os.path.abspath(os.path.dirname(__file__))
  with io.open(os.path.join(root, PKG_NAME, "about.py"), encoding="utf-8") as f:
    # pylint: disable=exec-used
    exec(f.read(), about)

  return about


def setup_package():
  """setup package using custom metadata """
  about = get_about()
  setup(
    name=PKG_NAME,
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    description=about["__description__"],
    license=about["__license__"],
    packages=find_packages(),
    install_requires=get_requirements(),
    include_package_data=True,
    entry_points={"console_scripts": []},
    requires=[],
  )


if __name__ == "__main__":
  setup_package()
