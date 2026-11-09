__all__ = ("app",)


import typer

lazy from .plugins import add_apps_from_entry_points

app = typer.Typer(no_args_is_help=True)


@app.callback()
def main() -> None:
    """Add commands from plugins."""
    return


add_apps_from_entry_points(app, group="entrypoints.apps")


if __name__ == "__main__":
    app()
