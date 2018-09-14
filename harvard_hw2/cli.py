# -*- coding: utf-8 -*-

"""Console script for harvard_hw2."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for harvard_hw2."""
    click.echo("Replace this message by putting your code into "
               "harvard_hw2.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
