#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bitmath

french_units = {'Ko': 'Kb', 'Mo': 'Mb', 'Go': 'Gb', 'To': 'Tb',
                'kio': 'kiB', 'Mio': 'MiB', 'Gio': 'GiB', 'Tio': 'TiB'}


def string_to_byte(stringvar):
    encoded = stringvar.encode('ascii', errors='ignore')
    for k, v in french_units.iteritems():
        encoded = encoded.replace(k, v)
    dv = bitmath.parse_string(encoded)
    return int(dv.to_EB()._byte_value)
