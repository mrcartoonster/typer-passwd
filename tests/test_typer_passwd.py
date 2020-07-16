# -*- coding: utf-8 -*-
import colorful as cf
import pytest
from typer.testing import CliRunner

from typer_passwd import __version__
from typer_passwd.main import app

runner = CliRunner()


def test_version():
    """Checking version is set correclty."""
    ver_num = cf.bold_green(__version__)
    result = runner.invoke(app, ["--version"], color=True)
    assert result.exit_code == 0
    assert f"typer-passwd version: {ver_num}"
    assert __version__ == "0.1.0"


@pytest.mark.first
def test_amount():
    """Check length of password."""
    result = runner.invoke(app, ["10"])
    assert result.exit_code == 0
    assert 11 == len(result.stdout)
