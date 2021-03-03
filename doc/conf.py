"""Sphinx configuration file for an LSST stack package.
This configuration only affects single-package Sphinx documentation builds.
"""
from documenteer.conf.pipelinespkg import *
import lsst.ts.ddsconfig
project = "ts_ddsconfig"
html_theme_options["logotext"] = project
html_title = project
html_short_title = project
doxylink = {}  # Avoid warning: Could not find tag file _doxygen/doxygen.tag
intersphinx_mapping["ts_xml"] = ("https://ts-xml.lsst.io", None)
