#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Usage:
  yourapp --config=<config> <word>

Options:
  --config = <config>   Config file path
  <word> = <word>       search word(Standard input)
"""

import os
import sys

from docopt import docopt
from fn import _

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(PROJECT_ROOT)
from yourapp import __version__

from yourapp.clients.github import search_repositories
from yourapp.models.core import *
from yourapp.models.github.search import *


def main():
    args: Args = Args.from_dict(docopt(__doc__, version=__version__))
    config: Config = Config.from_yamlf(args.config)

    r: SearchRepositoryResult = search_repositories(args.word)

    print(
        r.items
            .filter(_.stargazers_count > config.lower_star_count)
            .order_by(_.stargazers_count, reverse=True)
            .head(config.head.get_or(3))
            .to_table(['id', 'name', 'stargazers_count'])
    )


if __name__ == '__main__':
    main()
