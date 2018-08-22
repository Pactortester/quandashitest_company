import random

from idna import unichr


def Unicode():
    val1 = random.randint(0x4e00, 0x4f63)
    val2 = random.randint(0x5200, 0x5777)
    return chr(val1)+chr(val2)



#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# def my_get_letter_list():
#     import re
#
#     fonts_range = []
#     for lines in file('Chinese_Range', 'r'):
#         fonts_range.extend(map(lambda x: int(x, 16), \
#             re.split(',',lines.strip().strip(','))))
#
#     letter_list = ''.join(unichr(yf) for yf in fonts_range)
#     return letter_list
