# -*- coding: utf-8 -*-
import pytest
import typer
from typer.testing import CliRunner
from wasabi import color as c

from typer_passwd import __version__
from typer_passwd.main import app

runner = CliRunner()


@pytest.mark.parametrize("v", ["-v", "--version"])
def test_version(v):
    """Checking version is set correclty."""
    ver_num = c(__version__, fg="green", bold=True)
    result = runner.invoke(app, [v], color=True)
    assert result.exit_code == 0
    assert f"typer-passwd version: {ver_num}"
    assert __version__ == "0.1.0"


@pytest.mark.first
def test_amount():
    """Check length of password."""
    result = runner.invoke(app, ["10"])
    assert result.exit_code == 0
    assert 11 == len(result.stdout)


@pytest.mark.parametrize("gtlt", [7, 65])
@pytest.mark.second
def test_badparameter(gtlt):
    """Assure Error occurs when a number is entered that's less than eight and
    greater than sixty-four."""
    err_msg = (
        "Usage: main [OPTIONS] [AMOUNT]\n\nError: Invalid value for '[AMOUNT]'"
        + ": Password length must be between eight(8) to sixty-four(64)!\n"
    )
    result = runner.invoke(app, [str(gtlt)])
    result.output
    assert result.exit_code == 2
    assert err_msg == result.stdout


@pytest.mark.parametrize("gtlt", [7, 65])
@pytest.mark.third
def test_badparameter_with(gtlt):
    """Assure Error occurs when a number is entered that's less than eight and
    greater than sixty-four."""
    err_msg = (
        "Usage: main [OPTIONS] [AMOUNT]\n\nError: Invalid value for '[AMOUNT]'"
        + ": Password length must be between eight(8) to sixty-four(64)!\n"
    )
    with pytest.raises(typer.BadParameter, match=err_msg) as e:
        result = runner.invoke(app, [str(gtlt)])
        result.output
        assert result.exit_code == 2
        # assert err_msg == result.stdout
        assert e.type is typer.BadParameter
