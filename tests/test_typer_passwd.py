# -*- coding: utf-8 -*-
import pytest
from typer.testing import CliRunner
from wasabi import color as c

from typer_passwd import __version__
from typer_passwd.main import app

runner = CliRunner()
#   app = typer.Typer()
#   app.command()(coloring)


@pytest.mark.parametrize("v", ["-v", "--version"])
@pytest.mark.version
def test_version(v):
    """Checking version is set correclty."""
    ver_num = c(__version__, fg="green", bold=True)
    result = runner.invoke(app, [v], color=True)
    assert result.exit_code == 0
    assert f"typer-passwd version: {ver_num}"
    assert __version__ == "0.1.3"


@pytest.mark.first
def test_amount():
    """Check length of password."""
    result = runner.invoke(app, ["coloring", "10"])
    assert result.exit_code == 0
    assert 11 == len(result.stdout)


@pytest.mark.parametrize("gtlt", [7, 65])
@pytest.mark.second
def test_badparameter(gtlt):
    """Assure Error occurs when a number is entered that's less than eight and
    greater than sixty-four."""
    err_msg = (
        "Usage: main coloring [OPTIONS] [COLOR]\n\nError: Invalid value"
        + " for '[COLOR]': Password length must be between eight(8)"
        + " to sixty-four(64)!\n"
    )
    result = runner.invoke(app, ["coloring", str(gtlt)])
    result.output
    assert result.exit_code == 2
    assert err_msg == result.stdout
