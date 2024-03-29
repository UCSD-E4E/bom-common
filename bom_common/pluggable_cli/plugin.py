"""
Base class for cli plugins which allows for adding additional arguments to the cli.
"""

from abc import abstractmethod
from argparse import ArgumentParser, Namespace


class Plugin:
    """
    Base class for cli plugins which allows for adding additional arguments to the cli.
    """

    def __init__(self, parser: ArgumentParser):
        pass

    @abstractmethod
    def __call__(self, args: Namespace):
        """
        In a child class, this method is executed by a CLI plugin.
        """
        raise NotImplementedError
