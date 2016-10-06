#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys

name = "nb-mermaid"

# Minimal Python version sanity check

import sys

v = sys.version_info
if v[:2] < (2, 7) or (v[0] >= 3 and v[:2] < (3, 4)):
    error = "ERROR: %s requires Python version 2.7 or 3.4 or above." % name
    print(error, file=sys.stderr)
    sys.exit(1)

# Main

import os
from setuptools import setup

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))
pkg_root = pjoin(here, name)

packages = []
for d, _, _ in os.walk(pkg_root):
    if os.path.exists(pjoin(d, "__init__.py")):
        packages.append(d[len(here)+1:].replace(os.path.sep, "."))

version_ns = {}
with open(pjoin(here, name, '_version.py')) as f:
    exec(f.read(), {}, version_ns)

with open("README.rst") as f:
    README = f.read()

setup_args = dict(
    name=name,
    version=version_ns['__version__'],
    packages=packages,
    include_package_data=True,
    description="Mermaid diagrams in the IPython Notebook",
    long_description=README,
    author="Nicholas Bollweg",
    author_email="nick.bollweg@gmail.com",
    url="http://github.com/bollwyvl/nb-mermaid",
    license="BSD",
    platforms="Linux, Mac OS X, Windows",
    keywords=["jupyter", "ipython", "mermaid", "diagram" ],
    classifiers=[
        "Framework :: Jupyter",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: BSD License",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Scientific/Engineering :: Visualization"
      ],
    zip_safe=False
)

if 'develop' in sys.argv or any(bdist in sys.argv for bdist in ['bdist_wheel', 'bdist_egg']):
    import setuptools

setuptools_args = {}

install_requires = setuptools_args['install_requires'] = [
    'notebook>=4.2',
]

if 'setuptools' in sys.modules:
    setup_args.update(setuptools_args)

if __name__ == '__main__':
    setup(**setup_args)
