#!/usr/bin/env python3

from lazydata import track
from hunspell import HunSpell


h = HunSpell(track('./data/en.dic', 'https://cgit.freedesktop.org/libreoffice/dictionaries/plain/en/en_US.dic'),
             track('./data/en.aff', 'https://cgit.freedesktop.org/libreoffice/dictionaries/plain/en/en_US.aff'))
print([x.encode(h.get_dic_encoding()) for x in h.suggest('hollo')])
