__all__ = ("app",)

lazy import importlib.metadata

import typer

app = typer.Typer(no_args_is_help=True)


def add_apps() -> None:
    discovered_apps = importlib.metadata.entry_points(group="entrypoints.apps")
    for discovered_app in discovered_apps:
        app.add_typer(discovered_app.load())


@app.callback()
def main() -> None:
    """Add commands from plugins."""
    return


add_apps()


if __name__ == "__main__":
    app()
