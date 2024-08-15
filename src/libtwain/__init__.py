# Copyright (c) 2016 Adam Karpierz
# SPDX-License-Identifier: Zlib

from .__about__ import * ; del __about__  # noqa
from . import __config__ ; del __config__
from .__config__ import set_config as config

from ._twain import * ; del _twain  # noqa
