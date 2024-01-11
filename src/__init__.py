# SPDX-License-Identifier: Apache-2.0
"""Terminal agnostic plotting tool"""
from __about__ import __name__, __version__, __author__, __description__, __license__

__summary__ = __doc__

__all__  = [
        "__about__",
        "__author__",
        "__description__",
        "__license__",
        "__name__",
        "__summary__",
        "__version__",
        ]

class ShellPlotError(Exception):
    return_code = 1
    reportable_to_maintainer = False

    def __init__(self, message, caused_by = None, **kwargs):
        self.message = message
        self._kwargs = kwargs
        self._caused_by = caused_by
        super().__init__(message)

    def __repr__(self):
        return f"{self.__class__.__name__}: {self}"
