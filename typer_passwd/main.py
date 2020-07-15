# -*- coding: utf-8 -*-
import secrets
import string

import typer

app = typer.Typer()


def rstring(num: int) -> str:
    """Helper function to create a random string."""
    return "".join([secrets.choice(string.printable[:94]) for _ in range(num)])


def callback_passwd(value: int = 8) -> str:
    """Typer callback function to generate random string."""
    if value < 8 or value > 64:
        raise typer.BadParameter(
            "Password length must between eight(8) to sixtyfour(64)!",
        )
    else:
        return rstring(value)


@app.command()
def main(
    amount: int = typer.Argument(
        8,
        callback=callback_passwd,
        help="Returns random password. Default is 8 charachters long.",
    ),
):
    """Option that returns the password."""
    typer.echo(amount)


# Placing main while developing
if __name__ == "__main__":
    app()
    # typer.run(main)
