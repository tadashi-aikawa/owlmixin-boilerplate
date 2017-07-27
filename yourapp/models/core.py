#!/usr/bin/env python
# -*- coding: utf-8 -*-

from owlmixin import OwlMixin, TList, TDict, TOption, OwlEnum, OwlObjectEnum


class Args(OwlMixin):
    config: str
    stdin: str


class Config(OwlMixin):
    hello_list: TList[str]

