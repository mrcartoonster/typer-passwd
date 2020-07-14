import typer
from yakutils import random_string

app = typer.Typer()


@app.callback
def passwd(value: int):
    """Function that return random strings."""
    return random_string(value)


@app.command()
def main(amount: str = typer.Option(..., callback=passwd)):
    """Option that returns the password."""
    typer.echo(amount)
