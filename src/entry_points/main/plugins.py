__all__ = ("add_apps_from_entry_points",)

from typing import TYPE_CHECKING
lazy import importlib.metadata

if TYPE_CHECKING:
    from typer import Typer


def add_apps_from_entry_points(app: Typer, group: str) -> None:
    """Add Typer apps from entry points."""
    discovered_apps = importlib.metadata.entry_points(group=group)
    for discovered_app in discovered_apps:
        app.add_typer(discovered_app.load())
