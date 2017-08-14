#!/usr/bin/env python
# -*- coding: utf-8 -*-

from owlmixin import OwlMixin, TList

from yourapp.models.github.repository import Repository


# TODO: Should better abstract `Repository` when owlmixin supports for generics
class SearchRepositoryResult(OwlMixin):
    total_count: int
    items: TList[Repository]
