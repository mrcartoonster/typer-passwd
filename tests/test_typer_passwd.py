# -*- coding: utf-8 -*-
from typer_passwd import __version__


def test_version():
    """Checking version is set correclty."""
    assert __version__ == "0.1.0"
