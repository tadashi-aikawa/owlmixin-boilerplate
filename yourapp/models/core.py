#!/usr/bin/env python
# -*- coding: utf-8 -*-

from owlmixin import OwlMixin, TOption


class Args(OwlMixin):
    config: str
    word: str


class Config(OwlMixin):
    lower_star_count: int = 10
    head: TOption[int]
