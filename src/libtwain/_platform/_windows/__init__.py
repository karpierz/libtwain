# Copyright (c) 2016 Adam Karpierz
# SPDX-License-Identifier: Zlib

import sys
import os
import ctypes as ct

this_dir = os.path.dirname(os.path.abspath(__file__))
is_32bit = (sys.maxsize <= 2**32)
arch     = "x86" if is_32bit else "x64"
arch_dir = os.path.join(this_dir, arch)

try:
    from ...__config__ import config
    DLL_PATH = config.get("LIBTWAIN", None)
    del config
    if DLL_PATH is None or DLL_PATH in ("", "None"):
        raise ImportError()
except ImportError:
    DLL_PATH = os.path.join(arch_dir, "TWAINDSM.dll")
    # from ctypes.util import find_library
    # DLL_PATH = find_library("twain_32.dll")
    # if not DLL_PATH:
    #     raise OSError("Cannot find twain_32.dll library") from None

from ctypes import WinDLL as DLL  # noqa: E402,N814
try:
    from _ctypes import FreeLibrary as dlclose  # noqa: E402,N813
except ImportError:
    dlclose = lambda handle: 0
from ctypes import WINFUNCTYPE as CFUNC  # noqa: E402

time_t = ct.c_uint64

# Winsock doesn't have this POSIX type; it's used for the
# tv_usec value of struct timeval.
suseconds_t = ct.c_long

# Taken from the file <winsock.h>
#
# struct timeval {
#     long tv_sec;   /* seconds */
#     long tv_usec;  /* and microseconds */
# };

class timeval(ct.Structure):
    _fields_ = [
    ("tv_sec",  ct.c_long),    # seconds
    ("tv_usec", suseconds_t),  # microseconds
]
