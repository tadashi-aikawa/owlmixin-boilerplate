#!/usr/bin/env python
# -*- coding: utf-8 -*-

from owlmixin import OwlMixin


class Repository(OwlMixin):
    id: int
    name: str
    stargazers_count: int
