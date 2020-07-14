# -*- coding: utf-8 -*-
import typer
from yakutils import random_string

app = typer.Typer()


def callback_passwd(value: int = 8) -> str:
    """Function that return random strings."""
    if value < 8 and value > 64:
        raise typer.BadParameter(
            "Password length must between eight(8) to sixtyfour(64) greater!",
        )
    else:
        return random_string(value)


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
