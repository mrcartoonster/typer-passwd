# -*- coding: utf-8 -*-
import secrets
import string
from typing import Optional, Sequence

import colorful as cf
import typer

app = typer.Typer()

__version__ = "0.1.0"


def version_callback(value: bool) -> str:
    """Returning versin of typer-passwd."""
    ver_num = cf.bold_green(__version__)
    if value:
        typer.echo(f"typer-passwd version: {ver_num}")
        raise typer.Exit()


def colorizer(rstr: Sequence[str]) -> str:
    """Helper function that'll colorize the output password."""
    for _ in rstr:
        if _.isalpha():
            print(cf.white(_), end="")
        elif _.isnumeric():
            print(cf.red(_), end="")
        else:
            print(cf.blue(_), end="")


def rstring(num: int) -> str:
    """Helper function to create a colorcoded random string."""
    return colorizer(
        "".join([secrets.choice(string.printable[:94]) for _ in range(num)]),
    )


def callback_passwd(value: int = 8) -> str:
    """Typer callback function to generate random string."""
    if value < 8 or value > 64:
        raise typer.BadParameter(
            "Password length must be between eight(8) to sixty-four(64)!",
        )
    else:
        return rstring(value)


@app.command()
def main(
    amount: int = typer.Argument(
        8,
        callback=callback_passwd,
        help="Takes integer for the length of random password.",
    ),
    version: Optional[bool] = typer.Option(
        None, "--version", "-v", callback=version_callback,
    ),
):
    """Outputs random password with the length given or eight(8) characters
    long by default."""
    typer.echo(amount)


# Placing main while developing
if __name__ == "__main__":
    app()
    # typer.run(main)
