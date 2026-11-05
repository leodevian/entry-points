__all__ = ("app",)

import typer

app = typer.Typer(no_args_is_help=True)


@app.command()
def release() -> None:
    """Release."""
    print("Releasing...")


if __name__ == "__main__":
    app()
