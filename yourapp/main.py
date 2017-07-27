#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Usage:
  yourapp --config=<config> <stdin>

Options:
  --config = <config>   Config file path
  <stdin> = <stdin>     Standard input
"""

import os, sys

from docopt import docopt
from fn import _
from owlmixin import TList, TDict

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(PROJECT_ROOT)
from yourapp import __version__

from yourapp.models.core import *


def main():
    args: Args = Args.from_dict(docopt(__doc__, version=__version__))
    config: Config = Config.from_yamlf(args.config)

    print(f'Hello!: {config.hello_list}')
    print(f'Standard input: {args.stdin}')


if __name__ == '__main__':
    main()

