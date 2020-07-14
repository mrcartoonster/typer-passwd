# -*- coding: utf-8 -*-
import pytest
from typer.testing import CliRunner

from typer_passwd import __version__
from typer_passwd.main import app

runner = CliRunner()


def test_version():
    """Checking version is set correclty."""
    assert __version__ == "0.1.0"


@pytest.mark.first
def test_amount():
    """Check length of password."""
    result = runner.invoke(app, ["10"])
    assert result.exit_code == 0
    assert 11 == len(result.stdout)
