#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import pytest

from yourapp.clients.github import search_repositories
from yourapp.models.github.search import SearchRepositoryResult


@pytest.fixture()
def trick_requests(monkeypatch):
    class TrickResponse:
        def __init__(self, json_dict: dict):
            self.json_dict = json_dict

        def json(self):
            return self.json_dict

    def trick_get(url: str):
        return TrickResponse({
            'total_count': 10,
            'incomplete_results': False,
            'items': [
                {
                    'id': 1,
                    'name': 'repositoyr1',
                    'full_name': 'Repository 1',
                    'stargazers_count': 5,
                },
                {
                    'id': 2,
                    'name': 'repositoyr2',
                    'full_name': 'Repository 2',
                    'stargazers_count': 10,
                },
                {
                    'id': 3,
                    'name': 'repositoyr3',
                    'full_name': 'Repository 3',
                    'stargazers_count': 15,
                },
                {
                    'id': 4,
                    'name': 'repositoyr4',
                    'full_name': 'Repository 4',
                    'stargazers_count': 20,
                },
                {
                    'id': 5,
                    'name': 'repositoyr5',
                    'full_name': 'Repository 5',
                    'stargazers_count': 25,
                },
            ]
        })

    monkeypatch.setattr(requests, 'get', trick_get)


def test_search_repositories(trick_requests):
    actual: SearchRepositoryResult = search_repositories('owl')
    assert actual.to_dict() == {
        'total_count': 10,
        'items': [
            {
                'id': 1,
                'name': 'repositoyr1',
                'stargazers_count': 5,
            },
            {
                'id': 2,
                'name': 'repositoyr2',
                'stargazers_count': 10,
            },
            {
                'id': 3,
                'name': 'repositoyr3',
                'stargazers_count': 15,
            },
            {
                'id': 4,
                'name': 'repositoyr4',
                'stargazers_count': 20,
            },
            {
                'id': 5,
                'name': 'repositoyr5',
                'stargazers_count': 25,
            },
        ]
    }
