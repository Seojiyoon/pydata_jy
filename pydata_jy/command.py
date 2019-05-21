
from argparse import ArgumentParser

parsers = ArgumentParser(
    usage = 'pydata [-l]',
    description = "Location list PyData"
    )

parsers.add_argument(
    "-l",
    action="store_true",
    default=False,
    help="You can see lists of all PyData location."
    )

