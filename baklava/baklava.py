#!/usr/bin/env python
# -*- coding: utf-8 -*-

from providers import SearchFactory
import bitmath
from providers.utils import string_to_byte

sf = SearchFactory('cpasbien')
for item in sf.search('batman').sortBy('size').get():
    print item
