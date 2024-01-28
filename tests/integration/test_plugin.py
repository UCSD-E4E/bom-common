from argparse import Namespace

from bom_common.pluggable_cli.plugin import Plugin


class TestPlugin(Plugin):
    def execute(self, args: Namespace):
        print("Hello, World from TestPlugin!")
