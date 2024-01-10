# SPDX-License-Identifier: Apache-2.0
"""Shellplot package information."""
import os
import toml
from pathlib import Path

# Pull module info from pyproject.toml
pyproject_path = Path(os.pardir, "pyproject.toml").resolve()
pyproject = toml.load(pyproject_path)['project']

__name__ = pyproject['name']
__version__ = pyproject['version']
__author__ = pyproject['authors']
__description__ = pyproject['description']
