#!/usr/bin/env python
# -*- coding: utf-8 -*-

from providers import SearchFactory

sf = SearchFactory('strike')
for item in sf.search('scorpion', max=8).sortBy('size').get():
    print item
