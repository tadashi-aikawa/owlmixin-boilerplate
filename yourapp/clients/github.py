#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

from yourapp.models.github.search import SearchRepositoryResult


def search_repositories(word: str) -> SearchRepositoryResult:
    return SearchRepositoryResult.from_dict(
        requests.get(f'https://api.github.com/search/repositories?q={word}').json(),
        restrict=False
    )
