# -*- coding: utf-8 -*-
import typer
from yakutils import random_string

app = typer.Typer()


def callback_passwd(value: int) -> str:
    """Function that return random strings."""
    return random_string(value)


@app.command()
def main(amount: int = typer.Argument(..., callback=callback_passwd)):
    """Option that returns the password."""
    typer.echo(amount)


# Placing main while developing
if __name__ == "__main__":
    app()
    # typer.run(main)
