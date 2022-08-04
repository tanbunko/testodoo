# -*- coding: utf-8 -*-

import odoo

import argparse
import os
import sys


from odoo.cli.command import Command

_VERSION = odoo.modules.load_information_from_description_file("auto_update")["version"]


class AutoUpdate(Command):
    """Generates an Odoo module skeleton."""

    def run(self, cmdargs):
        parser = argparse.ArgumentParser(
            prog="%s auto-update" % sys.argv[0].split(os.path.sep)[-1],
            description=self.__doc__,
            epilog=self.epilog(),
        )
        parser.add_argument("name", help="Name of the module to create")
        parser.add_argument(
            "dest",
            default=".",
            nargs="?",
            help="Directory to create the module in (default: %(default)s)",
        )

        if not cmdargs:
            sys.exit(parser.print_help())
        args = parser.parse_args(args=cmdargs)
        print(args)

    def epilog(self):
        return f"Version: {_VERSION}"
