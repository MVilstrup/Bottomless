"""Command-line interface."""
from uuid import uuid4

import click

RUNTIME_ID = uuid4()

@click.command()
@click.version_option()
def main() -> None:
    """Bottomless."""


if __name__ == "__main__":
    main(prog_name="bottomless")  # pragma: no cover
