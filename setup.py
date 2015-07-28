#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys

from setuptools import setup


try:
    from jupyterpip import cmdclass
except:
    import pip
    import importlib

    pip.main(["install", "jupyter-pip"])
    cmdclass = importlib.import_module("jupyterpip").cmdclass


with open("setup.json") as f:
    setup_data = json.load(f)

if sys.version_info[0] < 3:
    # insidious! http://bugs.python.org/issue13943
    setup_data["packages"] = [s.encode("utf-8")
                              for s in setup_data["packages"]]

with open("README.rst") as f:
    setup_data.update(
        long_description=f.read()
    )

setup_data.update(
    cmdclass=cmdclass(
        path="{}/static/{}".format(
            setup_data["packages"][0],
            setup_data["name"],
        )
    )
)

setup(**setup_data)
