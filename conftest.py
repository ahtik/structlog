# -*- coding: utf-8 -*-

# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the MIT License.  See the LICENSE file in the root of this
# repository for complete details.

from __future__ import absolute_import, division, print_function

import sys

import pytest

from six.moves import cStringIO as StringIO

from structlog.stdlib import _NAME_TO_LEVEL


@pytest.fixture
def sio():
    """
    A StringIO instance.
    """
    return StringIO()


@pytest.fixture
def event_dict():
    """
    An example event dictionary with multiple value types w/o the event itself.
    """

    class A(object):
        def __repr__(self):
            return r"<A(\o/)>"

    return {"a": A(), "b": [3, 4], "x": 7, "y": "test", "z": (1, 2)}


@pytest.fixture(
    name="stdlib_log_method",
    params=[m for m in _NAME_TO_LEVEL if m != "notset"],
)
def fixture_stdlib_log_methods(request):
    return request.param


collect_ignore = []
if sys.version_info[:2] < (3, 7):
    collect_ignore.append("tests/test_contextvars.py")
