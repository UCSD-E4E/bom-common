import importlib
from argparse import ArgumentParser
from pathlib import Path
from typing import Dict

import yaml

from bom_common.pluggable_cli.plugin import Plugin


class Cli:
    def __init__(self, plugins_yaml_path: str or Path, description: str = None):
        plugins_yaml_path = Path(plugins_yaml_path)
        self.parser = ArgumentParser(description=description)

        subparsers = self.parser.add_subparsers(dest="command")
        subparsers.required = True

        with plugins_yaml_path.open("r", encoding="utf8") as f:
            plugins_dict: Dict[str, Dict] = yaml.safe_load(f)

        # Plugins are loaded dynamically from plugins_yaml
        for _, plugin in plugins_dict.items():
            for subcommand in plugin["subcommands"]:
                subparser = subparsers.add_parser(
                    subcommand, description=plugin["description"]
                )

                module = importlib.import_module(
                    f".{plugin['module']}", plugin["package"]
                )

                class_type = getattr(module, plugin["class"])

                cli_plugin: Plugin = class_type(subparser)
                subparser.set_defaults(run_plugin=cli_plugin.execute)

    def __call__(self):
        args = self.parser.parse_args()
        args.run_plugin(args)
