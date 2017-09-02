# -*- coding:utf-8 -*-
"""
@author: Gordon Han
@contact: Gordon-Han@hotmail.com
"""
import random

import config


def get_header():
    header = config.HEADER.copy()
    header['user-agent'] = random.choice(config.USER_AGENTS)
    return header
