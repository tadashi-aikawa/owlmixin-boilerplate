#!/usr/bin/env python
# -*- coding: utf-8 -*-

from yourapp.models.github.search import SearchRepositoryResult


def search_repositories(word: str) -> SearchRepositoryResult:
    return SearchRepositoryResult.from_json_url(f'https://api.github.com/search/repositories?q={word}')

