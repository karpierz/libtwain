# Copyright (c) 2016 Adam Karpierz
# SPDX-License-Identifier: Zlib

# ========================================================================= #
#
# Copyright (C) 2007 TWAIN Working Group: Adobe Systems Incorporated,
# AnyDoc Software Inc., Eastman Kodak Company, Fujitsu Computer Products
# of America, JFL Peripheral Solutions Inc., Ricoh Corporation, and
# Xerox Corporation.  All rights reserved.
#
# Copyright (C) 1991, 1992 TWAIN Working Group: Aldus, Caere, Eastman-Kodak,
# Hewlett-Packard and Logitech Corporations.  All rights reserved.
#
# Copyright (C) 1997 TWAIN Working Group: Bell+Howell, Canon, DocuMagix,
# Fujitsu, Genoa Technology, Hewlett-Packard, Kofax Imaging Products, and
# Ricoh Corporation.  All rights reserved.
#
# Copyright (C) 1998 TWAIN Working Group: Adobe Systems Incorporated,
# Canon Information Systems, Eastman Kodak Company,
# Fujitsu Computer Products of America, Genoa Technology,
# Hewlett-Packard Company, Intel Corporation, Kofax Image Products,
# JFL Peripheral Solutions Inc., Ricoh Corporation, and Xerox Corporation.
# All rights reserved.
#
# Copyright (C) 2000 TWAIN Working Group: Adobe Systems Incorporated,
# Canon Information Systems, Digimarc Corporation, Eastman Kodak Company,
# Fujitsu Computer Products of America, Hewlett-Packard Company,
# JFL Peripheral Solutions Inc., Ricoh Corporation, and Xerox Corporation.
# All rights reserved.
#
# TWAIN.h -  This is the definitive include file for applications and
#         data sources written to the TWAIN specification.
#         It defines constants, data structures, messages etc.
#         for the public interface to TWAIN.
#
# Revision History:
#   version 1.0, March 6, 1992.  TWAIN 1.0.
#   version 1.1, January 1993.   Tech Notes 1.1
#   version 1.5, June 1993.      Specification Update 1.5
#                                Change DC to TW
#                                Change filename from DC.H to TWAIN.H
#   version 1.5, July 1993.      Remove spaces from country identifiers
#
#   version 1.7, July 1997       Added Capabilities and data structure for
#                                document imaging and digital cameras.
#                                KHL.
#   version 1.7, July 1997       Inserted Borland compatibile structure packing
#                                directives provided by Mentor.  JMH
#   version 1.7, Aug 1997        Expanded file tabs to spaces.
#                                NOTE: future authors should be sure to have
#                                their editors set to automatically expand tabs
#                                to spaces (original tab setting was 4 spaces).
#   version 1.7, Sept 1997       Added job control values
#                                Added return codes
#   version 1.7, Sept 1997       changed definition of pRGBRESPONSE to
#                                pTW_RGBRESPONSE
#   version 1.7  Aug 1998        Added missing TWEI_BARCODEROTATION values
#                                TWBCOR_ types JMH
#   version 1.8  August 1998     Added new types and definitions required
#                                for 1.8 Specification JMH
#   version 1.8  January 1999    Changed search mode from SRCH_ to TWBD_ as
#                                in 1.8 Specification, added TWBT_MAXICODE JMH
#   version 1.8  January 1999    Removed undocumented duplicate AUTO<cap> JMH
#   version 1.8  March 1999      Removed undocumented 1.8 caps:
#                                CAP_FILESYSTEM
#                                CAP_PAPERBINDING
#                                CAP_PASSTHRU
#                                CAP_POWERDOWNTIME
#                                ICAP_AUTODISCARDBLANKPAGES
#                                * CAP_PAGEMULTIPLEACQUIRE - is CAP_REACQUIREALLOWED,
#                                requires spec change.  JMH
#                                Added Mac structure packing modifications JMH
#   version 1.9  March 2000      Added new types and definations required
#                                for 1.9 Specification MLM
#   version 1.9  March 2000      Added ICAP_JPEGQUALITY, TWJQ_ values,
#                                updated TWON_PROTOCOLMINOR for Release v1.9 MN
#   version 1.91 August 2007     Added new types and definitions required
#                                for 1.91 Specification MLM
#   version 2.0  Sept 2007       Added new types and definitions required
#                                for 2.0 Specification FHH
#   version 2.0  Mar 2008        Depreciated ICAP_PIXELTYPEs TWPT_SRGB64, TWPT_BGR,
#                                TWPT_CIELAB, TWPT_CIELUV, and TWPT_YCBCR  JMW
#   version 2.0  Mar 2008        Added missing new 2.0 CAP_ definitions JMW
#   version 2.0  Dec 2008        Updated TW_INFO structure for 64bit JMW
#   version 2.1  Mar 2009        Added new types and definitions required
#                                for 2.1 Specification JMW
#   version 2.2  Nov 2010        Added new types and definitions required
#                                for 2.2 Specification MSM
#   version 2.3  Feb 2013        Added new types and definitions required
#                                for 2.3 Specification MLM
#   version 2.3a Apr 2015        Errata fixes to TWCY_ANDORRA and TWCY_CUBA
#   version 2.4  Aug 2015        Added new types and definitions required
#                                for 2.4 Specification MLM
#   version 2.4a June 2016       Added TW_INT32 and TW_UINT32 fixes for Linux,
#                                (I just added this comment today)
#   version 2.4b March 2017      Missing changeset from 2.3 verion (2013/06/20)
#   version 2.5  Jan 2021        Added new types and definitions required
#                                for 2.5 Specification MLM
#
# ========================================================================= #

import ctypes as ct

from ._platform import is_windows, is_linux, is_macos
from ._platform import is_32bit
from ._platform import defined
from ._platform import CFUNC
from ._platform import timeval
from ._dll      import dll

#***************************************************************************#
# TWAIN Version                                                             #
#***************************************************************************#

TWON_PROTOCOLMAJOR = 2
TWON_PROTOCOLMINOR = 5  # Changed for Version 2.5

#***************************************************************************#
# Platform Dependent Definitions and Typedefs                               #
#***************************************************************************#

if is_windows:
    # Microsoft C/C++ Compiler
    TWH_CMP_MSC = True
elif is_linux:
    # GNU C/C++ Compiler
    TWH_CMP_GNU = True
elif is_macos:
    # Apple Compiler (which is GNU now)
    TWH_CMP_GNU = True
    TWH_CMP_XCODE = True
else:
    # Unrecognized
    import platform
    raise RuntimeError("Unsupported platform: %s-%s" %
                       (platform.platform(), platform.machine()))
if is_32bit:
    TWH_32BIT = True
else:
    TWH_64BIT = True

# Win32 and Win64 systems
if defined("TWH_CMP_MSC"):
    from ctypes import wintypes
    TW_HANDLE  = wintypes.HANDLE
    TW_MEMREF  = wintypes.LPVOID
    BYTE       = wintypes.BYTE
    TW_UINTPTR = ct.c_uint if defined("TWH_32BIT") else ct.c_uint64
    del wintypes
    _pack = 2  # Set the packing: this occurs before any structures are defined
# MacOS/X...
elif defined("TWH_CMP_XCODE"):
    TW_HANDLE  = Handle  # !!!
    TW_MEMREF  = ct.POINTER(ct.c_byte)
    BYTE       = ct.c_ubyte
    TW_UINTPTR = ct.c_ulong if defined("TWH_32BIT") else ct.c_ulonglong
    # cf: Mac version of TWAIN.h
    #pragma options align = power
    _pack = 0 # ???  # Set the packing: this occurs before any structures are defined
# Everything else (Linux etc)...
else:
    TW_HANDLE  = ct.c_void_p
    TW_MEMREF  = ct.c_void_p
    BYTE       = ct.c_ubyte
    TW_UINTPTR = ct.c_ulong if defined("TWH_32BIT") else ct.c_ulonglong
    _pack = 2  # Set the packing: this occurs before any structures are defined

#***************************************************************************#
# Type Definitions                                                          #
#***************************************************************************#

# String types. These include room for the strings and a NULL char,
# or, on the Mac, a length byte followed by the string.
# TW_STR255 must hold less than 256 chars so length fits in first byte.
str_char = ct.c_ubyte if is_macos else ct.c_char
TW_STR32  = str_char * 34  ; pTW_STR32  = ct.POINTER(TW_STR32)
TW_STR64  = str_char * 66  ; pTW_STR64  = ct.POINTER(TW_STR64)
TW_STR128 = str_char * 130 ; pTW_STR128 = ct.POINTER(TW_STR128)
TW_STR255 = str_char * 256 ; pTW_STR255 = ct.POINTER(TW_STR255)
del str_char

# Numeric types.
TW_INT8   = ct.c_int8   ; pTW_INT8   = ct.POINTER(TW_INT8)
TW_INT16  = ct.c_int16  ; pTW_INT16  = ct.POINTER(TW_INT16)
TW_INT32  = ct.c_int32  ; pTW_INT32  = ct.POINTER(TW_INT32)
TW_UINT8  = ct.c_uint8  ; pTW_UINT8  = ct.POINTER(TW_UINT8)
TW_UINT16 = ct.c_uint16 ; pTW_UINT16 = ct.POINTER(TW_UINT16)
TW_UINT32 = ct.c_uint32 ; pTW_UINT32 = ct.POINTER(TW_UINT32)
TW_BOOL   = ct.c_ushort ; pTW_BOOL   = ct.POINTER(TW_BOOL)

#***************************************************************************#
# Structure Definitions                                                     #
#***************************************************************************#

# Fixed point structure type.
class TW_FIX32(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("Whole", TW_INT16),
    ("Frac",  TW_UINT16),
]
pTW_FIX32 = ct.POINTER(TW_FIX32)

# Defines a frame rectangle in ICAP_UNITS coordinates.
class TW_FRAME(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("Left",   TW_FIX32),
    ("Top",    TW_FIX32),
    ("Right",  TW_FIX32),
    ("Bottom", TW_FIX32),
]
pTW_FRAME = ct.POINTER(TW_FRAME)

# Defines the parameters used for channel-specific transformation.
class TW_DECODEFUNCTION(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("StartIn",     TW_FIX32),
    ("BreakIn",     TW_FIX32),
    ("EndIn",       TW_FIX32),
    ("StartOut",    TW_FIX32),
    ("BreakOut",    TW_FIX32),
    ("EndOut",      TW_FIX32),
    ("Gamma",       TW_FIX32),
    ("SampleCount", TW_FIX32),
]
pTW_DECODEFUNCTION = ct.POINTER(TW_DECODEFUNCTION)

# Stores a Fixed point number in two parts, a whole and a fractional part.
class TW_TRANSFORMSTAGE(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("Decode", TW_DECODEFUNCTION * 3),
    ("Mix",    (TW_FIX32 * 3) * 3),
]
pTW_TRANSFORMSTAGE = ct.POINTER(TW_TRANSFORMSTAGE)

# Container for array of values
class TW_ARRAY(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("ItemType", TW_UINT16),
    ("NumItems", TW_UINT32),
    ("ItemList", TW_UINT8 * 1),
]
pTW_ARRAY = ct.POINTER(TW_ARRAY)

# Information about audio data
class TW_AUDIOINFO(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("Name",     TW_STR255),
    ("Reserved", TW_UINT32),
]
pTW_AUDIOINFO = ct.POINTER(TW_AUDIOINFO)

# Used to register callbacks.
class TW_CALLBACK(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("CallBackProc", TW_MEMREF),
    ("RefCon",       TW_MEMREF if is_macos else TW_UINT32),
    ("Message",      TW_INT16),
]
pTW_CALLBACK = ct.POINTER(TW_CALLBACK)

# Used to register callbacks.
class TW_CALLBACK2(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("CallBackProc", TW_MEMREF),
    ("RefCon",       TW_UINTPTR),
    ("Message",      TW_INT16),
]
pTW_CALLBACK2 = ct.POINTER(TW_CALLBACK2)

# Used by application to get/set capability from/in a data source.
class TW_CAPABILITY(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("Cap",        TW_UINT16),
    ("ConType",    TW_UINT16),
    ("hContainer", TW_HANDLE),
]
pTW_CAPABILITY = ct.POINTER(TW_CAPABILITY)

# Defines a CIE XYZ space tri-stimulus value.
class TW_CIEPOINT(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("X", TW_FIX32),
    ("Y", TW_FIX32),
    ("Z", TW_FIX32),
]
pTW_CIEPOINT = ct.POINTER(TW_CIEPOINT)

# Defines the mapping from an RGB color space device into CIE 1931 (XYZ)
# color space.
class TW_CIECOLOR(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("ColorSpace",      TW_UINT16),
    ("LowEndian",       TW_INT16),
    ("DeviceDependent", TW_INT16),
    ("VersionNumber",   TW_INT32),
    ("StageABC",        TW_TRANSFORMSTAGE),
    ("StageLMN",        TW_TRANSFORMSTAGE),
    ("WhitePoint",      TW_CIEPOINT),
    ("BlackPoint",      TW_CIEPOINT),
    ("WhitePaper",      TW_CIEPOINT),
    ("BlackInk",        TW_CIEPOINT),
    ("Samples",         TW_FIX32 * 1),
]
pTW_CIECOLOR = ct.POINTER(TW_CIECOLOR)

# Allows for a data source and application to pass custom data to each other.
class TW_CUSTOMDSDATA(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("InfoLength", TW_UINT32),
    ("hData",      TW_HANDLE),
]
pTW_CUSTOMDSDATA = ct.POINTER(TW_CUSTOMDSDATA)

# Provides information about the Event that was raised by the Source
class TW_DEVICEEVENT(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("Event",                  TW_UINT32),
    ("DeviceName",             TW_STR255),
    ("BatteryMinutes",         TW_UINT32),
    ("BatteryPercentage",      TW_INT16),
    ("PowerSupply",            TW_INT32),
    ("XResolution",            TW_FIX32),
    ("YResolution",            TW_FIX32),
    ("FlashUsed2",             TW_UINT32),
    ("AutomaticCapture",       TW_UINT32),
    ("TimeBeforeFirstCapture", TW_UINT32),
    ("TimeBetweenCaptures",    TW_UINT32),
]
pTW_DEVICEEVENT = ct.POINTER(TW_DEVICEEVENT)

# This structure holds the tri-stimulus color palette information for
# TW_PALETTE8 structures.
class TW_ELEMENT8(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("Index",    TW_UINT8),
    ("Channel1", TW_UINT8),
    ("Channel2", TW_UINT8),
    ("Channel3", TW_UINT8),
]
pTW_ELEMENT8 = ct.POINTER(TW_ELEMENT8)

# Stores a group of individual values describing a capability.
class TW_ENUMERATION(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("ItemType",     TW_UINT16),
    ("NumItems",     TW_UINT32),
    ("CurrentIndex", TW_UINT32),
    ("DefaultIndex", TW_UINT32),
    ("ItemList",     TW_UINT8 * 1),
]
pTW_ENUMERATION = ct.POINTER(TW_ENUMERATION)

# Used to pass application events/messages from the application to the
# Source.
class TW_EVENT(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("pEvent",    TW_MEMREF),
    ("TWMessage", TW_UINT16),
]
pTW_EVENT = ct.POINTER(TW_EVENT)

# This structure is used to pass specific information between the data source
# and the application.
class TW_INFO(ct.Structure):
    _pack_ = _pack
    class _U(ct.Union):
        _pack_ = _pack
        _fields_ = [
        ("ReturnCode", TW_UINT16),
        ("CondCode",   TW_UINT16),  # Deprecated, do not use
    ]
    _anonymous_ = ("_u",)
    _fields_ = [
    ("InfoID",   TW_UINT16),
    ("ItemType", TW_UINT16),
    ("NumItems", TW_UINT16),
    ("_u",       _U),
    ("Item",     TW_UINTPTR),
]
pTW_INFO = ct.POINTER(TW_INFO)

class TW_EXTIMAGEINFO(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("NumInfos", TW_UINT32),
    ("Info",     TW_INFO * 1),
]
pTW_EXTIMAGEINFO = ct.POINTER(TW_EXTIMAGEINFO)

# Provides information about the currently selected device
class TW_FILESYSTEM(ct.Structure):
    _pack_ = _pack
    class _U1(ct.Union):
        _pack_ = _pack
        _fields_ = [
        ("Recursive",      ct.c_int),
        ("Subdirectories", TW_BOOL),
    ]
    class _U2(ct.Union):
        _pack_ = _pack
        _fields_ = [
        ("FileType",       TW_INT32),
        ("FileSystemType", TW_UINT32),
    ]
    _anonymous_ = ("_u1", "_u2")
    _fields_ = [
    ("InputName",        TW_STR255),
    ("OutputName",       TW_STR255),
    ("Context",          TW_MEMREF),
    ("_u1",              _U1),
    ("_u2",              _U2),
    ("Size",             TW_UINT32),
    ("CreateTimeDate",   TW_STR32),
    ("ModifiedTimeDate", TW_STR32),
    ("FreeSpace",        TW_UINT32),
    ("NewImageSize",     TW_INT32),
    ("NumberOfFiles",    TW_UINT32),
    ("NumberOfSnippets", TW_UINT32),
    ("DeviceGroupMask",  TW_UINT32),
    ("Reserved",         TW_INT8 * 508),
]
pTW_FILESYSTEM = ct.POINTER(TW_FILESYSTEM)

# This structure is used by the application to specify a set of mapping
# values to be applied to grayscale data.
class TW_GRAYRESPONSE(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("Response", TW_ELEMENT8 * 1),
]
pTW_GRAYRESPONSE = ct.POINTER(TW_GRAYRESPONSE)

# A general way to describe the version of software that is running.
class TW_VERSION(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("MajorNum", TW_UINT16),
    ("MinorNum", TW_UINT16),
    ("Language", TW_UINT16),
    ("Country",  TW_UINT16),
    ("Info",     TW_STR32),
]
pTW_VERSION = ct.POINTER(TW_VERSION)

# Provides identification information about a TWAIN entity.
class TW_IDENTITY(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("Id",              TW_MEMREF if is_macos else TW_UINT32),
    ("Version",         TW_VERSION),
    ("ProtocolMajor",   TW_UINT16),
    ("ProtocolMinor",   TW_UINT16),
    ("SupportedGroups", TW_UINT32),
    ("Manufacturer",    TW_STR32),
    ("ProductFamily",   TW_STR32),
    ("ProductName",     TW_STR32),
]
pTW_IDENTITY = ct.POINTER(TW_IDENTITY)

# Describes the "real" image data, that is, the complete image being
# transferred between the Source and application.
class TW_IMAGEINFO(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("XResolution",     TW_FIX32),
    ("YResolution",     TW_FIX32),
    ("ImageWidth",      TW_INT32),
    ("ImageLength",     TW_INT32),
    ("SamplesPerPixel", TW_INT16),
    ("BitsPerSample",   TW_INT16 * 8),
    ("BitsPerPixel",    TW_INT16),
    ("Planar",          TW_BOOL),
    ("PixelType",       TW_INT16),
    ("Compression",     TW_UINT16),
]
pTW_IMAGEINFO = ct.POINTER(TW_IMAGEINFO)

# Involves information about the original size of the acquired image.
class TW_IMAGELAYOUT(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("Frame",          TW_FRAME),
    ("DocumentNumber", TW_UINT32),
    ("PageNumber",     TW_UINT32),
    ("FrameNumber",    TW_UINT32),
]
pTW_IMAGELAYOUT = ct.POINTER(TW_IMAGELAYOUT)

# Provides information for managing memory buffers.
class TW_MEMORY(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("Flags",  TW_UINT32),
    ("Length", TW_UINT32),
    ("TheMem", TW_MEMREF),
]
pTW_MEMORY = ct.POINTER(TW_MEMORY)

# Describes the form of the acquired data being passed from the Source to the
# application.
class TW_IMAGEMEMXFER(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("Compression",  TW_UINT16),
    ("BytesPerRow",  TW_UINT32),
    ("Columns",      TW_UINT32),
    ("Rows",         TW_UINT32),
    ("XOffset",      TW_UINT32),
    ("YOffset",      TW_UINT32),
    ("BytesWritten", TW_UINT32),
    ("Memory",       TW_MEMORY),
]
pTW_IMAGEMEMXFER = ct.POINTER(TW_IMAGEMEMXFER)

# Describes the information necessary to transfer a JPEG-compressed image.
class TW_JPEGCOMPRESSION(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("ColorSpace",       TW_UINT16),
    ("SubSampling",      TW_UINT32),
    ("NumComponents",    TW_UINT16),
    ("RestartFrequency", TW_UINT16),
    ("QuantMap",         TW_UINT16 * 4),
    ("QuantTable",       TW_MEMORY * 4),
    ("HuffmanMap",       TW_UINT16 * 4),
    ("HuffmanDC",        TW_MEMORY * 2),
    ("HuffmanAC",        TW_MEMORY * 2),
]
pTW_JPEGCOMPRESSION = ct.POINTER(TW_JPEGCOMPRESSION)

# Collects scanning metrics after returning to state 4
class TW_METRICS(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("SizeOf",     TW_UINT32),
    ("ImageCount", TW_UINT32),
    ("SheetCount", TW_UINT32),
]
pTW_METRICS = ct.POINTER(TW_METRICS)

# Stores a single value (item) which describes a capability.
class TW_ONEVALUE(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("ItemType", TW_UINT16),
    ("Item",     TW_UINT32),
]
pTW_ONEVALUE = ct.POINTER(TW_ONEVALUE)

# This structure holds the color palette information.
class TW_PALETTE8(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("NumColors",   TW_UINT16),
    ("PaletteType", TW_UINT16),
    ("Colors",      TW_ELEMENT8 * 256),
]
pTW_PALETTE8 = ct.POINTER(TW_PALETTE8)

# Used to bypass the TWAIN protocol when communicating with a device
class TW_PASSTHRU(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("pCommand",        TW_MEMREF),
    ("CommandBytes",    TW_UINT32),
    ("Direction",       TW_INT32),
    ("pData",           TW_MEMREF),
    ("DataBytes",       TW_UINT32),
    ("DataBytesXfered", TW_UINT32),
]
pTW_PASSTHRU = ct.POINTER(TW_PASSTHRU)

# This structure tells the application how many more complete transfers the
# Source currently has available.
class TW_PENDINGXFERS(ct.Structure):
    _pack_ = _pack
    class _U(ct.Union):
        _pack_ = _pack
        _fields_ = [
        ("EOJ",      TW_UINT32),
        ("Reserved", TW_UINT32),
    ]
    if is_macos:  # cf: Mac version of TWAIN.h
        class _U_TW_JOBCONTROL(ct.Union):
            _pack_ = _pack
            _fields_ = [
            ("EOJ",      TW_UINT32),
            ("Reserved", TW_UINT32),
        ]
        _U._fields_.append(
            ("TW_JOBCONTROL", _U_TW_JOBCONTROL)
        )
    _anonymous_ = ("_u",)
    _fields_ = [
    ("Count", TW_UINT16),
    ("_u",    _U),
]
pTW_PENDINGXFERS = ct.POINTER(TW_PENDINGXFERS)

# Stores a range of individual values describing a capability.
class TW_RANGE(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("ItemType",     TW_UINT16),
    ("MinValue",     TW_UINT32),
    ("MaxValue",     TW_UINT32),
    ("StepSize",     TW_UINT32),
    ("DefaultValue", TW_UINT32),
    ("CurrentValue", TW_UINT32),
]
pTW_RANGE = ct.POINTER(TW_RANGE)

# This structure is used by the application to specify a set of mapping
# values to be applied to RGB color data.
class TW_RGBRESPONSE(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("Response", TW_ELEMENT8 * 1),
]
pTW_RGBRESPONSE = ct.POINTER(TW_RGBRESPONSE)

# Describes the file format and file specification information for a transfer
# through a disk file.
class TW_SETUPFILEXFER(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("FileName", TW_STR255),
    ("Format",   TW_UINT16),
    ("VRefNum",  TW_INT16),
]
pTW_SETUPFILEXFER = ct.POINTER(TW_SETUPFILEXFER)

# Provides the application information about the Source's requirements and
# preferences regarding allocation of transfer buffer(s).
class TW_SETUPMEMXFER(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("MinBufSize", TW_UINT32),
    ("MaxBufSize", TW_UINT32),
    ("Preferred",  TW_UINT32),
]
pTW_SETUPMEMXFER = ct.POINTER(TW_SETUPMEMXFER)

# Describes the status of a source.
class TW_STATUS(ct.Structure):
    _pack_ = _pack
    class _U(ct.Union):
        _pack_ = _pack
        _fields_ = [
        ("Data",     TW_UINT16),
        ("Reserved", TW_UINT16),
    ]
    _anonymous_ = ("_u",)
    _fields_ = [
    ("ConditionCode", TW_UINT16),
    ("_u",            _U),
]
pTW_STATUS = ct.POINTER(TW_STATUS)

# Translates the contents of Status into a localized UTF8string.
class TW_STATUSUTF8(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("Status",     TW_STATUS),
    ("Size",       TW_UINT32),
    ("UTF8string", TW_HANDLE),
]
pTW_STATUSUTF8 = ct.POINTER(TW_STATUSUTF8)

class TW_TWAINDIRECT(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("SizeOf",               TW_UINT32),
    ("CommunicationManager", TW_UINT16),
    ("Send",                 TW_HANDLE),
    ("SendSize",             TW_UINT32),
    ("Receive",              TW_HANDLE),
    ("ReceiveSize",          TW_UINT32),
]
pTW_TWAINDIRECT = ct.POINTER(TW_TWAINDIRECT)

# This structure is used to handle the user interface coordination between
# an application and a Source.
class TW_USERINTERFACE(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("ShowUI",  TW_BOOL),
    ("ModalUI", TW_BOOL),
    ("hParent", TW_HANDLE),
]
pTW_USERINTERFACE = ct.POINTER(TW_USERINTERFACE)

#***************************************************************************#
# Generic Constants                                                         #
#***************************************************************************#

TWON_ARRAY       = 3
TWON_ENUMERATION = 4
TWON_ONEVALUE    = 5
TWON_RANGE       = 6

TWON_ICONID      = 962
TWON_DSMID       = 461
TWON_DSMCODEID   = 63

TWON_DONTCARE8   = 0xff
TWON_DONTCARE16  = 0xffff
TWON_DONTCARE32  = 0xffffffff

# Flags used in TW_MEMORY structure.
TWMF_APPOWNS = 0x0001
TWMF_DSMOWNS = 0x0002
TWMF_DSOWNS  = 0x0004
TWMF_POINTER = 0x0008
TWMF_HANDLE  = 0x0010

TWTY_INT8   = 0x0000
TWTY_INT16  = 0x0001
TWTY_INT32  = 0x0002

TWTY_UINT8  = 0x0003
TWTY_UINT16 = 0x0004
TWTY_UINT32 = 0x0005

TWTY_BOOL   = 0x0006

TWTY_FIX32  = 0x0007

TWTY_FRAME  = 0x0008

TWTY_STR32  = 0x0009
TWTY_STR64  = 0x000a
TWTY_STR128 = 0x000b
TWTY_STR255 = 0x000c
TWTY_HANDLE = 0x000f

#***************************************************************************#
# Capability Constants                                                      #
#***************************************************************************#

# CAP_ALARMS values
TWAL_ALARM         = 0
TWAL_FEEDERERROR   = 1
TWAL_FEEDERWARNING = 2
TWAL_BARCODE       = 3
TWAL_DOUBLEFEED    = 4
TWAL_JAM           = 5
TWAL_PATCHCODE     = 6
TWAL_POWER         = 7
TWAL_SKEW          = 8

# ICAP_AUTOSIZE values
TWAS_NONE    = 0
TWAS_AUTO    = 1
TWAS_CURRENT = 2

# TWEI_BARCODEROTATION values
TWBCOR_ROT0   = 0
TWBCOR_ROT90  = 1
TWBCOR_ROT180 = 2
TWBCOR_ROT270 = 3
TWBCOR_ROTX   = 4

# ICAP_BARCODESEARCHMODE values
TWBD_HORZ     = 0
TWBD_VERT     = 1
TWBD_HORZVERT = 2
TWBD_VERTHORZ = 3

# ICAP_BITORDER values
TWBO_LSBFIRST = 0
TWBO_MSBFIRST = 1

# ICAP_AUTODISCARDBLANKPAGES values
TWBP_DISABLE = -2
TWBP_AUTO    = -1

# ICAP_BITDEPTHREDUCTION values
TWBR_THRESHOLD        = 0
TWBR_HALFTONE         = 1
TWBR_CUSTHALFTONE     = 2
TWBR_DIFFUSION        = 3
TWBR_DYNAMICTHRESHOLD = 4

# ICAP_SUPPORTEDBARCODETYPES and TWEI_BARCODETYPE values
TWBT_3OF9                 = 0
TWBT_2OF5INTERLEAVED      = 1
TWBT_2OF5NONINTERLEAVED   = 2
TWBT_CODE93               = 3
TWBT_CODE128              = 4
TWBT_UCC128               = 5
TWBT_CODABAR              = 6
TWBT_UPCA                 = 7
TWBT_UPCE                 = 8
TWBT_EAN8                 = 9
TWBT_EAN13                = 10
TWBT_POSTNET              = 11
TWBT_PDF417               = 12
TWBT_2OF5INDUSTRIAL       = 13
TWBT_2OF5MATRIX           = 14
TWBT_2OF5DATALOGIC        = 15
TWBT_2OF5IATA             = 16
TWBT_3OF9FULLASCII        = 17
TWBT_CODABARWITHSTARTSTOP = 18
TWBT_MAXICODE             = 19
TWBT_QRCODE               = 20

# ICAP_COMPRESSION values
TWCP_NONE        = 0
TWCP_PACKBITS    = 1
TWCP_GROUP31D    = 2
TWCP_GROUP31DEOL = 3
TWCP_GROUP32D    = 4
TWCP_GROUP4      = 5
TWCP_JPEG        = 6
TWCP_LZW         = 7
TWCP_JBIG        = 8
TWCP_PNG         = 9
TWCP_RLE4        = 10
TWCP_RLE8        = 11
TWCP_BITFIELDS   = 12
TWCP_ZIP         = 13
TWCP_JPEG2000    = 14

# CAP_CAMERASIDE and TWEI_PAGESIDE values
TWCS_BOTH   = 0
TWCS_TOP    = 1
TWCS_BOTTOM = 2

# CAP_DEVICEEVENT values
TWDE_CUSTOMEVENTS          = 0x8000
TWDE_CHECKAUTOMATICCAPTURE = 0
TWDE_CHECKBATTERY          = 1
TWDE_CHECKDEVICEONLINE     = 2
TWDE_CHECKFLASH            = 3
TWDE_CHECKPOWERSUPPLY      = 4
TWDE_CHECKRESOLUTION       = 5
TWDE_DEVICEADDED           = 6
TWDE_DEVICEOFFLINE         = 7
TWDE_DEVICEREADY           = 8
TWDE_DEVICEREMOVED         = 9
TWDE_IMAGECAPTURED         = 10
TWDE_IMAGEDELETED          = 11
TWDE_PAPERDOUBLEFEED       = 12
TWDE_PAPERJAM              = 13
TWDE_LAMPFAILURE           = 14
TWDE_POWERSAVE             = 15
TWDE_POWERSAVENOTIFY       = 16

# TW_PASSTHRU.Direction values.
TWDR_GET = 1
TWDR_SET = 2

# TWEI_DESKEWSTATUS values.
TWDSK_SUCCESS    = 0
TWDSK_REPORTONLY = 1
TWDSK_FAIL       = 2
TWDSK_DISABLED   = 3

# CAP_DUPLEX values
TWDX_NONE        = 0
TWDX_1PASSDUPLEX = 1
TWDX_2PASSDUPLEX = 2

# CAP_FEEDERALIGNMENT values
TWFA_NONE   = 0
TWFA_LEFT   = 1
TWFA_CENTER = 2
TWFA_RIGHT  = 3

# ICAP_FEEDERTYPE values
TWFE_GENERAL = 0
TWFE_PHOTO   = 1

# ICAP_IMAGEFILEFORMAT values
TWFF_TIFF      = 0
TWFF_PICT      = 1
TWFF_BMP       = 2
TWFF_XBM       = 3
TWFF_JFIF      = 4
TWFF_FPX       = 5
TWFF_TIFFMULTI = 6
TWFF_PNG       = 7
TWFF_SPIFF     = 8
TWFF_EXIF      = 9
TWFF_PDF       = 10
TWFF_JP2       = 11
TWFF_JPX       = 13
TWFF_DEJAVU    = 14
TWFF_PDFA      = 15
TWFF_PDFA2     = 16
TWFF_PDFRASTER = 17

# ICAP_FLASHUSED2 values
TWFL_NONE   = 0
TWFL_OFF    = 1
TWFL_ON     = 2
TWFL_AUTO   = 3
TWFL_REDEYE = 4

# CAP_FEEDERORDER values
TWFO_FIRSTPAGEFIRST = 0
TWFO_LASTPAGEFIRST  = 1

# CAP_FEEDERPOCKET values
TWFP_POCKETERROR = 0
TWFP_POCKET1     = 1
TWFP_POCKET2     = 2
TWFP_POCKET3     = 3
TWFP_POCKET4     = 4
TWFP_POCKET5     = 5
TWFP_POCKET6     = 6
TWFP_POCKET7     = 7
TWFP_POCKET8     = 8
TWFP_POCKET9     = 9
TWFP_POCKET10    = 10
TWFP_POCKET11    = 11
TWFP_POCKET12    = 12
TWFP_POCKET13    = 13
TWFP_POCKET14    = 14
TWFP_POCKET15    = 15
TWFP_POCKET16    = 16

# ICAP_FLIPROTATION values
TWFR_BOOK    = 0
TWFR_FANFOLD = 1

# ICAP_FILTER values
TWFT_RED     = 0
TWFT_GREEN   = 1
TWFT_BLUE    = 2
TWFT_NONE    = 3
TWFT_WHITE   = 4
TWFT_CYAN    = 5
TWFT_MAGENTA = 6
TWFT_YELLOW  = 7
TWFT_BLACK   = 8

# TW_FILESYSTEM.FileType values
TWFY_CAMERA        = 0
TWFY_CAMERATOP     = 1
TWFY_CAMERABOTTOM  = 2
TWFY_CAMERAPREVIEW = 3
TWFY_DOMAIN        = 4
TWFY_HOST          = 5
TWFY_DIRECTORY     = 6
TWFY_IMAGE         = 7
TWFY_UNKNOWN       = 8

# CAP_IAFIELD*_LEVEL values
TWIA_UNUSED = 0
TWIA_FIXED  = 1
TWIA_LEVEL1 = 2
TWIA_LEVEL2 = 3
TWIA_LEVEL3 = 4
TWIA_LEVEL4 = 5

# ICAP_ICCPROFILE values
TWIC_NONE  = 0
TWIC_LINK  = 1
TWIC_EMBED = 2

# ICAP_IMAGEFILTER values
TWIF_NONE     = 0
TWIF_AUTO     = 1
TWIF_LOWPASS  = 2
TWIF_BANDPASS = 3
TWIF_HIGHPASS = 4
TWIF_TEXT     = TWIF_BANDPASS
TWIF_FINELINE = TWIF_HIGHPASS

# ICAP_IMAGEMERGE values
TWIM_NONE          = 0
TWIM_FRONTONTOP    = 1
TWIM_FRONTONBOTTOM = 2
TWIM_FRONTONLEFT   = 3
TWIM_FRONTONRIGHT  = 4

# CAP_JOBCONTROL values
TWJC_NONE = 0
TWJC_JSIC = 1
TWJC_JSIS = 2
TWJC_JSXC = 3
TWJC_JSXS = 4

# ICAP_JPEGQUALITY values
TWJQ_UNKNOWN = -4
TWJQ_LOW     = -3
TWJQ_MEDIUM  = -2
TWJQ_HIGH    = -1

# ICAP_LIGHTPATH values
TWLP_REFLECTIVE   = 0
TWLP_TRANSMISSIVE = 1

# ICAP_LIGHTSOURCE values
TWLS_RED   = 0
TWLS_GREEN = 1
TWLS_BLUE  = 2
TWLS_NONE  = 3
TWLS_WHITE = 4
TWLS_UV    = 5
TWLS_IR    = 6

# TWEI_MAGTYPE values
TWMD_MICR    = 0
TWMD_RAW     = 1
TWMD_INVALID = 2

# ICAP_NOISEFILTER values
TWNF_NONE         = 0
TWNF_AUTO         = 1
TWNF_LONEPIXEL    = 2
TWNF_MAJORITYRULE = 3

# ICAP_ORIENTATION values
TWOR_ROT0        = 0
TWOR_ROT90       = 1
TWOR_ROT180      = 2
TWOR_ROT270      = 3
TWOR_PORTRAIT    = TWOR_ROT0
TWOR_LANDSCAPE   = TWOR_ROT270
TWOR_AUTO        = 4
TWOR_AUTOTEXT    = 5
TWOR_AUTOPICTURE = 6

# ICAP_OVERSCAN values
TWOV_NONE      = 0
TWOV_AUTO      = 1
TWOV_TOPBOTTOM = 2
TWOV_LEFTRIGHT = 3
TWOV_ALL       = 4

# Palette types for TW_PALETTE8
TWPA_RGB  = 0
TWPA_GRAY = 1
TWPA_CMY  = 2

# ICAP_PLANARCHUNKY values
TWPC_CHUNKY = 0
TWPC_PLANAR = 1

# TWEI_PATCHCODE values
TWPCH_PATCH1 = 0
TWPCH_PATCH2 = 1
TWPCH_PATCH3 = 2
TWPCH_PATCH4 = 3
TWPCH_PATCH6 = 4
TWPCH_PATCHT = 5

# ICAP_PIXELFLAVOR values
TWPF_CHOCOLATE = 0
TWPF_VANILLA   = 1

# CAP_PRINTERMODE values
TWPM_SINGLESTRING       = 0
TWPM_MULTISTRING        = 1
TWPM_COMPOUNDSTRING     = 2
TWPM_IMAGEADDRESSSTRING = 3

# CAP_PRINTER values
TWPR_IMPRINTERTOPBEFORE    = 0
TWPR_IMPRINTERTOPAFTER     = 1
TWPR_IMPRINTERBOTTOMBEFORE = 2
TWPR_IMPRINTERBOTTOMAFTER  = 3
TWPR_ENDORSERTOPBEFORE     = 4
TWPR_ENDORSERTOPAFTER      = 5
TWPR_ENDORSERBOTTOMBEFORE  = 6
TWPR_ENDORSERBOTTOMAFTER   = 7

# CAP_PRINTERFONTSTYLE Added 2.3
TWPF_NORMAL    = 0
TWPF_BOLD      = 1
TWPF_ITALIC    = 2
TWPF_LARGESIZE = 3
TWPF_SMALLSIZE = 4

# CAP_PRINTERINDEXTRIGGER Added 2.3
TWCT_PAGE   = 0
TWCT_PATCH1 = 1
TWCT_PATCH2 = 2
TWCT_PATCH3 = 3
TWCT_PATCH4 = 4
TWCT_PATCHT = 5
TWCT_PATCH6 = 6

# CAP_POWERSUPPLY values
TWPS_EXTERNAL = 0
TWPS_BATTERY  = 1

# ICAP_PIXELTYPE values (PT_ means Pixel Type)
TWPT_BW       = 0
TWPT_GRAY     = 1
TWPT_RGB      = 2
TWPT_PALETTE  = 3
TWPT_CMY      = 4
TWPT_CMYK     = 5
TWPT_YUV      = 6
TWPT_YUVK     = 7
TWPT_CIEXYZ   = 8
TWPT_LAB      = 9
TWPT_SRGB     = 10
TWPT_SCRGB    = 11
TWPT_INFRARED = 16

# CAP_SEGMENTED values
TWSG_NONE   = 0
TWSG_AUTO   = 1
TWSG_MANUAL = 2

# ICAP_FILMTYPE values
TWFM_POSITIVE = 0
TWFM_NEGATIVE = 1

# CAP_DOUBLEFEEDDETECTION
TWDF_ULTRASONIC = 0
TWDF_BYLENGTH   = 1
TWDF_INFRARED   = 2

# CAP_DOUBLEFEEDDETECTIONSENSITIVITY
TWUS_LOW    = 0
TWUS_MEDIUM = 1
TWUS_HIGH   = 2

# CAP_DOUBLEFEEDDETECTIONRESPONSE
TWDP_STOP         = 0
TWDP_STOPANDWAIT  = 1
TWDP_SOUND        = 2
TWDP_DONOTIMPRINT = 3

# ICAP_MIRROR values
TWMR_NONE       = 0
TWMR_VERTICAL   = 1
TWMR_HORIZONTAL = 2

# ICAP_JPEGSUBSAMPLING values
TWJS_444YCBCR = 0
TWJS_444RGB   = 1
TWJS_422      = 2
TWJS_421      = 3
TWJS_411      = 4
TWJS_420      = 5
TWJS_410      = 6
TWJS_311      = 7

# CAP_PAPERHANDLING values
TWPH_NORMAL     = 0
TWPH_FRAGILE    = 1
TWPH_THICK      = 2
TWPH_TRIFOLD    = 3
TWPH_PHOTOGRAPH = 4

# CAP_INDICATORSMODE values
TWCI_INFO    = 0
TWCI_WARNING = 1
TWCI_ERROR   = 2
TWCI_WARMUP  = 3

# ICAP_SUPPORTEDSIZES values (SS_ means Supported Sizes)
TWSS_NONE         = 0
TWSS_A4           = 1
TWSS_JISB5        = 2
TWSS_USLETTER     = 3
TWSS_USLEGAL      = 4
TWSS_A5           = 5
TWSS_ISOB4        = 6
TWSS_ISOB6        = 7
TWSS_USLEDGER     = 9
TWSS_USEXECUTIVE  = 10
TWSS_A3           = 11
TWSS_ISOB3        = 12
TWSS_A6           = 13
TWSS_C4           = 14
TWSS_C5           = 15
TWSS_C6           = 16
TWSS_4A0          = 17
TWSS_2A0          = 18
TWSS_A0           = 19
TWSS_A1           = 20
TWSS_A2           = 21
TWSS_A7           = 22
TWSS_A8           = 23
TWSS_A9           = 24
TWSS_A10          = 25
TWSS_ISOB0        = 26
TWSS_ISOB1        = 27
TWSS_ISOB2        = 28
TWSS_ISOB5        = 29
TWSS_ISOB7        = 30
TWSS_ISOB8        = 31
TWSS_ISOB9        = 32
TWSS_ISOB10       = 33
TWSS_JISB0        = 34
TWSS_JISB1        = 35
TWSS_JISB2        = 36
TWSS_JISB3        = 37
TWSS_JISB4        = 38
TWSS_JISB6        = 39
TWSS_JISB7        = 40
TWSS_JISB8        = 41
TWSS_JISB9        = 42
TWSS_JISB10       = 43
TWSS_C0           = 44
TWSS_C1           = 45
TWSS_C2           = 46
TWSS_C3           = 47
TWSS_C7           = 48
TWSS_C8           = 49
TWSS_C9           = 50
TWSS_C10          = 51
TWSS_USSTATEMENT  = 52
TWSS_BUSINESSCARD = 53
TWSS_MAXSIZE      = 54

# ICAP_XFERMECH values (SX_ means Setup XFer)
TWSX_NATIVE  = 0
TWSX_FILE    = 1
TWSX_MEMORY  = 2
TWSX_MEMFILE = 4

# ICAP_UNITS values (UN_ means UNits)
TWUN_INCHES      = 0
TWUN_CENTIMETERS = 1
TWUN_PICAS       = 2
TWUN_POINTS      = 3
TWUN_TWIPS       = 4
TWUN_PIXELS      = 5
TWUN_MILLIMETERS = 6

#***************************************************************************#
# Country Constants                                                         #
#***************************************************************************#

TWCY_AFGHANISTAN    = 1001
TWCY_ALGERIA        = 213
TWCY_AMERICANSAMOA  = 684
TWCY_ANDORRA        = 33
TWCY_ANGOLA         = 1002
TWCY_ANGUILLA       = 8090
TWCY_ANTIGUA        = 8091
TWCY_ARGENTINA      = 54
TWCY_ARUBA          = 297
TWCY_ASCENSIONI     = 247
TWCY_AUSTRALIA      = 61
TWCY_AUSTRIA        = 43
TWCY_BAHAMAS        = 8092
TWCY_BAHRAIN        = 973
TWCY_BANGLADESH     = 880
TWCY_BARBADOS       = 8093
TWCY_BELGIUM        = 32
TWCY_BELIZE         = 501
TWCY_BENIN          = 229
TWCY_BERMUDA        = 8094
TWCY_BHUTAN         = 1003
TWCY_BOLIVIA        = 591
TWCY_BOTSWANA       = 267
TWCY_BRITAIN        = 6
TWCY_BRITVIRGINIS   = 8095
TWCY_BRAZIL         = 55
TWCY_BRUNEI         = 673
TWCY_BULGARIA       = 359
TWCY_BURKINAFASO    = 1004
TWCY_BURMA          = 1005
TWCY_BURUNDI        = 1006
TWCY_CAMAROON       = 237
TWCY_CANADA         = 2
TWCY_CAPEVERDEIS    = 238
TWCY_CAYMANIS       = 8096
TWCY_CENTRALAFREP   = 1007
TWCY_CHAD           = 1008
TWCY_CHILE          = 56
TWCY_CHINA          = 86
TWCY_CHRISTMASIS    = 1009
TWCY_COCOSIS        = 1009
TWCY_COLOMBIA       = 57
TWCY_COMOROS        = 1010
TWCY_CONGO          = 1011
TWCY_COOKIS         = 1012
TWCY_COSTARICA      = 506
TWCY_CUBA           = 5
TWCY_CYPRUS         = 357
TWCY_CZECHOSLOVAKIA = 42
TWCY_DENMARK        = 45
TWCY_DJIBOUTI       = 1013
TWCY_DOMINICA       = 8097
TWCY_DOMINCANREP    = 8098
TWCY_EASTERIS       = 1014
TWCY_ECUADOR        = 593
TWCY_EGYPT          = 20
TWCY_ELSALVADOR     = 503
TWCY_EQGUINEA       = 1015
TWCY_ETHIOPIA       = 251
TWCY_FALKLANDIS     = 1016
TWCY_FAEROEIS       = 298
TWCY_FIJIISLANDS    = 679
TWCY_FINLAND        = 358
TWCY_FRANCE         = 33
TWCY_FRANTILLES     = 596
TWCY_FRGUIANA       = 594
TWCY_FRPOLYNEISA    = 689
TWCY_FUTANAIS       = 1043
TWCY_GABON          = 241
TWCY_GAMBIA         = 220
TWCY_GERMANY        = 49
TWCY_GHANA          = 233
TWCY_GIBRALTER      = 350
TWCY_GREECE         = 30
TWCY_GREENLAND      = 299
TWCY_GRENADA        = 8099
TWCY_GRENEDINES     = 8015
TWCY_GUADELOUPE     = 590
TWCY_GUAM           = 671
TWCY_GUANTANAMOBAY  = 5399
TWCY_GUATEMALA      = 502
TWCY_GUINEA         = 224
TWCY_GUINEABISSAU   = 1017
TWCY_GUYANA         = 592
TWCY_HAITI          = 509
TWCY_HONDURAS       = 504
TWCY_HONGKONG       = 852
TWCY_HUNGARY        = 36
TWCY_ICELAND        = 354
TWCY_INDIA          = 91
TWCY_INDONESIA      = 62
TWCY_IRAN           = 98
TWCY_IRAQ           = 964
TWCY_IRELAND        = 353
TWCY_ISRAEL         = 972
TWCY_ITALY          = 39
TWCY_IVORYCOAST     = 225
TWCY_JAMAICA        = 8010
TWCY_JAPAN          = 81
TWCY_JORDAN         = 962
TWCY_KENYA          = 254
TWCY_KIRIBATI       = 1018
TWCY_KOREA          = 82
TWCY_KUWAIT         = 965
TWCY_LAOS           = 1019
TWCY_LEBANON        = 1020
TWCY_LIBERIA        = 231
TWCY_LIBYA          = 218
TWCY_LIECHTENSTEIN  = 41
TWCY_LUXENBOURG     = 352
TWCY_MACAO          = 853
TWCY_MADAGASCAR     = 1021
TWCY_MALAWI         = 265
TWCY_MALAYSIA       = 60
TWCY_MALDIVES       = 960
TWCY_MALI           = 1022
TWCY_MALTA          = 356
TWCY_MARSHALLIS     = 692
TWCY_MAURITANIA     = 1023
TWCY_MAURITIUS      = 230
TWCY_MEXICO         = 3
TWCY_MICRONESIA     = 691
TWCY_MIQUELON       = 508
TWCY_MONACO         = 33
TWCY_MONGOLIA       = 1024
TWCY_MONTSERRAT     = 8011
TWCY_MOROCCO        = 212
TWCY_MOZAMBIQUE     = 1025
TWCY_NAMIBIA        = 264
TWCY_NAURU          = 1026
TWCY_NEPAL          = 977
TWCY_NETHERLANDS    = 31
TWCY_NETHANTILLES   = 599
TWCY_NEVIS          = 8012
TWCY_NEWCALEDONIA   = 687
TWCY_NEWZEALAND     = 64
TWCY_NICARAGUA      = 505
TWCY_NIGER          = 227
TWCY_NIGERIA        = 234
TWCY_NIUE           = 1027
TWCY_NORFOLKI       = 1028
TWCY_NORWAY         = 47
TWCY_OMAN           = 968
TWCY_PAKISTAN       = 92
TWCY_PALAU          = 1029
TWCY_PANAMA         = 507
TWCY_PARAGUAY       = 595
TWCY_PERU           = 51
TWCY_PHILLIPPINES   = 63
TWCY_PITCAIRNIS     = 1030
TWCY_PNEWGUINEA     = 675
TWCY_POLAND         = 48
TWCY_PORTUGAL       = 351
TWCY_QATAR          = 974
TWCY_REUNIONI       = 1031
TWCY_ROMANIA        = 40
TWCY_RWANDA         = 250
TWCY_SAIPAN         = 670
TWCY_SANMARINO      = 39
TWCY_SAOTOME        = 1033
TWCY_SAUDIARABIA    = 966
TWCY_SENEGAL        = 221
TWCY_SEYCHELLESIS   = 1034
TWCY_SIERRALEONE    = 1035
TWCY_SINGAPORE      = 65
TWCY_SOLOMONIS      = 1036
TWCY_SOMALI         = 1037
TWCY_SOUTHAFRICA    = 27
TWCY_SPAIN          = 34
TWCY_SRILANKA       = 94
TWCY_STHELENA       = 1032
TWCY_STKITTS        = 8013
TWCY_STLUCIA        = 8014
TWCY_STPIERRE       = 508
TWCY_STVINCENT      = 8015
TWCY_SUDAN          = 1038
TWCY_SURINAME       = 597
TWCY_SWAZILAND      = 268
TWCY_SWEDEN         = 46
TWCY_SWITZERLAND    = 41
TWCY_SYRIA          = 1039
TWCY_TAIWAN         = 886
TWCY_TANZANIA       = 255
TWCY_THAILAND       = 66
TWCY_TOBAGO         = 8016
TWCY_TOGO           = 228
TWCY_TONGAIS        = 676
TWCY_TRINIDAD       = 8016
TWCY_TUNISIA        = 216
TWCY_TURKEY         = 90
TWCY_TURKSCAICOS    = 8017
TWCY_TUVALU         = 1040
TWCY_UGANDA         = 256
TWCY_USSR           = 7
TWCY_UAEMIRATES     = 971
TWCY_UNITEDKINGDOM  = 44
TWCY_USA            = 1
TWCY_URUGUAY        = 598
TWCY_VANUATU        = 1041
TWCY_VATICANCITY    = 39
TWCY_VENEZUELA      = 58
TWCY_WAKE           = 1042
TWCY_WALLISIS       = 1043
TWCY_WESTERNSAHARA  = 1044
TWCY_WESTERNSAMOA   = 1045
TWCY_YEMEN          = 1046
TWCY_YUGOSLAVIA     = 38
TWCY_ZAIRE          = 243
TWCY_ZAMBIA         = 260
TWCY_ZIMBABWE       = 263
TWCY_ALBANIA        = 355
TWCY_ARMENIA        = 374
TWCY_AZERBAIJAN     = 994
TWCY_BELARUS        = 375
TWCY_BOSNIAHERZGO   = 387
TWCY_CAMBODIA       = 855
TWCY_CROATIA        = 385
TWCY_CZECHREPUBLIC  = 420
TWCY_DIEGOGARCIA    = 246
TWCY_ERITREA        = 291
TWCY_ESTONIA        = 372
TWCY_GEORGIA        = 995
TWCY_LATVIA         = 371
TWCY_LESOTHO        = 266
TWCY_LITHUANIA      = 370
TWCY_MACEDONIA      = 389
TWCY_MAYOTTEIS      = 269
TWCY_MOLDOVA        = 373
TWCY_MYANMAR        = 95
TWCY_NORTHKOREA     = 850
TWCY_PUERTORICO     = 787
TWCY_RUSSIA         = 7
TWCY_SERBIA         = 381
TWCY_SLOVAKIA       = 421
TWCY_SLOVENIA       = 386
TWCY_SOUTHKOREA     = 82
TWCY_UKRAINE        = 380
TWCY_USVIRGINIS     = 340
TWCY_VIETNAM        = 84

#***************************************************************************#
# Language Constants                                                        #
#***************************************************************************#

TWLG_USERLOCALE           = -1
TWLG_DAN                  = 0
TWLG_DUT                  = 1
TWLG_ENG                  = 2
TWLG_FCF                  = 3
TWLG_FIN                  = 4
TWLG_FRN                  = 5
TWLG_GER                  = 6
TWLG_ICE                  = 7
TWLG_ITN                  = 8
TWLG_NOR                  = 9
TWLG_POR                  = 10
TWLG_SPA                  = 11
TWLG_SWE                  = 12
TWLG_USA                  = 13
TWLG_AFRIKAANS            = 14
TWLG_ALBANIA              = 15
TWLG_ARABIC               = 16
TWLG_ARABIC_ALGERIA       = 17
TWLG_ARABIC_BAHRAIN       = 18
TWLG_ARABIC_EGYPT         = 19
TWLG_ARABIC_IRAQ          = 20
TWLG_ARABIC_JORDAN        = 21
TWLG_ARABIC_KUWAIT        = 22
TWLG_ARABIC_LEBANON       = 23
TWLG_ARABIC_LIBYA         = 24
TWLG_ARABIC_MOROCCO       = 25
TWLG_ARABIC_OMAN          = 26
TWLG_ARABIC_QATAR         = 27
TWLG_ARABIC_SAUDIARABIA   = 28
TWLG_ARABIC_SYRIA         = 29
TWLG_ARABIC_TUNISIA       = 30
TWLG_ARABIC_UAE           = 31
TWLG_ARABIC_YEMEN         = 32
TWLG_BASQUE               = 33
TWLG_BYELORUSSIAN         = 34
TWLG_BULGARIAN            = 35
TWLG_CATALAN              = 36
TWLG_CHINESE              = 37
TWLG_CHINESE_HONGKONG     = 38
TWLG_CHINESE_PRC          = 39
TWLG_CHINESE_SINGAPORE    = 40
TWLG_CHINESE_SIMPLIFIED   = 41
TWLG_CHINESE_TAIWAN       = 42
TWLG_CHINESE_TRADITIONAL  = 43
TWLG_CROATIA              = 44
TWLG_CZECH                = 45
TWLG_DANISH               = TWLG_DAN
TWLG_DUTCH                = TWLG_DUT
TWLG_DUTCH_BELGIAN        = 46
TWLG_ENGLISH              = TWLG_ENG
TWLG_ENGLISH_AUSTRALIAN   = 47
TWLG_ENGLISH_CANADIAN     = 48
TWLG_ENGLISH_IRELAND      = 49
TWLG_ENGLISH_NEWZEALAND   = 50
TWLG_ENGLISH_SOUTHAFRICA  = 51
TWLG_ENGLISH_UK           = 52
TWLG_ENGLISH_USA          = TWLG_USA
TWLG_ESTONIAN             = 53
TWLG_FAEROESE             = 54
TWLG_FARSI                = 55
TWLG_FINNISH              = TWLG_FIN
TWLG_FRENCH               = TWLG_FRN
TWLG_FRENCH_BELGIAN       = 56
TWLG_FRENCH_CANADIAN      = TWLG_FCF
TWLG_FRENCH_LUXEMBOURG    = 57
TWLG_FRENCH_SWISS         = 58
TWLG_GERMAN               = TWLG_GER
TWLG_GERMAN_AUSTRIAN      = 59
TWLG_GERMAN_LUXEMBOURG    = 60
TWLG_GERMAN_LIECHTENSTEIN = 61
TWLG_GERMAN_SWISS         = 62
TWLG_GREEK                = 63
TWLG_HEBREW               = 64
TWLG_HUNGARIAN            = 65
TWLG_ICELANDIC            = TWLG_ICE
TWLG_INDONESIAN           = 66
TWLG_ITALIAN              = TWLG_ITN
TWLG_ITALIAN_SWISS        = 67
TWLG_JAPANESE             = 68
TWLG_KOREAN               = 69
TWLG_KOREAN_JOHAB         = 70
TWLG_LATVIAN              = 71
TWLG_LITHUANIAN           = 72
TWLG_NORWEGIAN            = TWLG_NOR
TWLG_NORWEGIAN_BOKMAL     = 73
TWLG_NORWEGIAN_NYNORSK    = 74
TWLG_POLISH               = 75
TWLG_PORTUGUESE           = TWLG_POR
TWLG_PORTUGUESE_BRAZIL    = 76
TWLG_ROMANIAN             = 77
TWLG_RUSSIAN              = 78
TWLG_SERBIAN_LATIN        = 79
TWLG_SLOVAK               = 80
TWLG_SLOVENIAN            = 81
TWLG_SPANISH              = TWLG_SPA
TWLG_SPANISH_MEXICAN      = 82
TWLG_SPANISH_MODERN       = 83
TWLG_SWEDISH              = TWLG_SWE
TWLG_THAI                 = 84
TWLG_TURKISH              = 85
TWLG_UKRANIAN             = 86
TWLG_ASSAMESE             = 87
TWLG_BENGALI              = 88
TWLG_BIHARI               = 89
TWLG_BODO                 = 90
TWLG_DOGRI                = 91
TWLG_GUJARATI             = 92
TWLG_HARYANVI             = 93
TWLG_HINDI                = 94
TWLG_KANNADA              = 95
TWLG_KASHMIRI             = 96
TWLG_MALAYALAM            = 97
TWLG_MARATHI              = 98
TWLG_MARWARI              = 99
TWLG_MEGHALAYAN           = 100
TWLG_MIZO                 = 101
TWLG_NAGA                 = 102
TWLG_ORISSI               = 103
TWLG_PUNJABI              = 104
TWLG_PUSHTU               = 105
TWLG_SERBIAN_CYRILLIC     = 106
TWLG_SIKKIMI              = 107
TWLG_SWEDISH_FINLAND      = 108
TWLG_TAMIL                = 109
TWLG_TELUGU               = 110
TWLG_TRIPURI              = 111
TWLG_URDU                 = 112
TWLG_VIETNAMESE           = 113

#***************************************************************************#
# Data Groups                                                               #
#***************************************************************************#

DG_CONTROL = 0x0001
DG_IMAGE   = 0x0002
DG_AUDIO   = 0x0004

# More Data Functionality may be added in the future.
# These are for items that need to be determined before DS is opened.
# NOTE: Supported Functionality constants must be powers of 2 as they are
#       used as bitflags when Application asks DSM to present a list of DSs.
#       to support backward capability the App and DS will not use the fields

DF_DSM2 = 0x10000000
DF_APP2 = 0x20000000

DF_DS2  = 0x40000000

DG_MASK = 0xFFFF

#***************************************************************************#
#                                                                           #
#***************************************************************************#

DAT_NULL       = 0x0000
DAT_CUSTOMBASE = 0x8000

# Data Argument Types for the DG_CONTROL Data Group.
DAT_CAPABILITY    = 0x0001
DAT_EVENT         = 0x0002
DAT_IDENTITY      = 0x0003
DAT_PARENT        = 0x0004
DAT_PENDINGXFERS  = 0x0005
DAT_SETUPMEMXFER  = 0x0006
DAT_SETUPFILEXFER = 0x0007
DAT_STATUS        = 0x0008
DAT_USERINTERFACE = 0x0009
DAT_XFERGROUP     = 0x000a
DAT_CUSTOMDSDATA  = 0x000c
DAT_DEVICEEVENT   = 0x000d
DAT_FILESYSTEM    = 0x000e
DAT_PASSTHRU      = 0x000f
DAT_CALLBACK      = 0x0010
DAT_STATUSUTF8    = 0x0011
DAT_CALLBACK2     = 0x0012
DAT_METRICS       = 0x0013
DAT_TWAINDIRECT   = 0x0014

# Data Argument Types for the DG_IMAGE Data Group.
DAT_IMAGEINFO       = 0x0101
DAT_IMAGELAYOUT     = 0x0102
DAT_IMAGEMEMXFER    = 0x0103
DAT_IMAGENATIVEXFER = 0x0104
DAT_IMAGEFILEXFER   = 0x0105
DAT_CIECOLOR        = 0x0106
DAT_GRAYRESPONSE    = 0x0107
DAT_RGBRESPONSE     = 0x0108
DAT_JPEGCOMPRESSION = 0x0109
DAT_PALETTE8        = 0x010a
DAT_EXTIMAGEINFO    = 0x010b
DAT_FILTER          = 0x010c

# Data Argument Types for the DG_AUDIO Data Group.
DAT_AUDIOFILEXFER   = 0x0201
DAT_AUDIOINFO       = 0x0202
DAT_AUDIONATIVEXFER = 0x0203

# misplaced
DAT_ICCPROFILE       = 0x0401
DAT_IMAGEMEMFILEXFER = 0x0402
DAT_ENTRYPOINT       = 0x0403

#***************************************************************************#
# Messages                                                                  #
#***************************************************************************#

# All message constants are unique.
# Messages are grouped according to which DATs they are used with.

MSG_NULL       = 0x0000
MSG_CUSTOMBASE = 0x8000

# Generic messages may be used with any of several DATs.
MSG_GET           = 0x0001
MSG_GETCURRENT    = 0x0002
MSG_GETDEFAULT    = 0x0003
MSG_GETFIRST      = 0x0004
MSG_GETNEXT       = 0x0005
MSG_SET           = 0x0006
MSG_RESET         = 0x0007
MSG_QUERYSUPPORT  = 0x0008
MSG_GETHELP       = 0x0009
MSG_GETLABEL      = 0x000a
MSG_GETLABELENUM  = 0x000b
MSG_SETCONSTRAINT = 0x000c

# Messages used with DAT_NULL
MSG_XFERREADY   = 0x0101
MSG_CLOSEDSREQ  = 0x0102
MSG_CLOSEDSOK   = 0x0103
MSG_DEVICEEVENT = 0x0104

# Messages used with a pointer to DAT_PARENT data
MSG_OPENDSM  = 0x0301
MSG_CLOSEDSM = 0x0302

# Messages used with a pointer to a DAT_IDENTITY structure
MSG_OPENDS     = 0x0401
MSG_CLOSEDS    = 0x0402
MSG_USERSELECT = 0x0403

# Messages used with a pointer to a DAT_USERINTERFACE structure
MSG_DISABLEDS      = 0x0501
MSG_ENABLEDS       = 0x0502
MSG_ENABLEDSUIONLY = 0x0503

# Messages used with a pointer to a DAT_EVENT structure
MSG_PROCESSEVENT = 0x0601

# Messages used with a pointer to a DAT_PENDINGXFERS structure
MSG_ENDXFER    = 0x0701
MSG_STOPFEEDER = 0x0702

# Messages used with a pointer to a DAT_FILESYSTEM structure
MSG_CHANGEDIRECTORY = 0x0801
MSG_CREATEDIRECTORY = 0x0802
MSG_DELETE          = 0x0803
MSG_FORMATMEDIA     = 0x0804
MSG_GETCLOSE        = 0x0805
MSG_GETFIRSTFILE    = 0x0806
MSG_GETINFO         = 0x0807
MSG_GETNEXTFILE     = 0x0808
MSG_RENAME          = 0x0809
MSG_COPY            = 0x080A
MSG_AUTOMATICCAPTUREDIRECTORY = 0x080B

# Messages used with a pointer to a DAT_PASSTHRU structure
MSG_PASSTHRU = 0x0901

# used with DAT_CALLBACK
MSG_REGISTER_CALLBACK = 0x0902

# used with DAT_CAPABILITY
MSG_RESETALL = 0x0A01

# used with DAT_TWAINDIRECT
MSG_SETTASK = 0x0B01

#***************************************************************************#
# Capabilities                                                              #
#***************************************************************************#

CAP_CUSTOMBASE = 0x8000  # Base of custom capabilities

# all data sources are REQUIRED to support these caps
CAP_XFERCOUNT = 0x0001

# image data sources are REQUIRED to support these caps
ICAP_COMPRESSION = 0x0100
ICAP_PIXELTYPE   = 0x0101
ICAP_UNITS       = 0x0102
ICAP_XFERMECH    = 0x0103

# all data sources MAY support these caps
CAP_AUTHOR                         = 0x1000
CAP_CAPTION                        = 0x1001
CAP_FEEDERENABLED                  = 0x1002
CAP_FEEDERLOADED                   = 0x1003
CAP_TIMEDATE                       = 0x1004
CAP_SUPPORTEDCAPS                  = 0x1005
CAP_EXTENDEDCAPS                   = 0x1006
CAP_AUTOFEED                       = 0x1007
CAP_CLEARPAGE                      = 0x1008
CAP_FEEDPAGE                       = 0x1009
CAP_REWINDPAGE                     = 0x100a
CAP_INDICATORS                     = 0x100b
CAP_PAPERDETECTABLE                = 0x100d
CAP_UICONTROLLABLE                 = 0x100e
CAP_DEVICEONLINE                   = 0x100f
CAP_AUTOSCAN                       = 0x1010
CAP_THUMBNAILSENABLED              = 0x1011
CAP_DUPLEX                         = 0x1012
CAP_DUPLEXENABLED                  = 0x1013
CAP_ENABLEDSUIONLY                 = 0x1014
CAP_CUSTOMDSDATA                   = 0x1015
CAP_ENDORSER                       = 0x1016
CAP_JOBCONTROL                     = 0x1017
CAP_ALARMS                         = 0x1018
CAP_ALARMVOLUME                    = 0x1019
CAP_AUTOMATICCAPTURE               = 0x101a
CAP_TIMEBEFOREFIRSTCAPTURE         = 0x101b
CAP_TIMEBETWEENCAPTURES            = 0x101c
CAP_MAXBATCHBUFFERS                = 0x101e
CAP_DEVICETIMEDATE                 = 0x101f
CAP_POWERSUPPLY                    = 0x1020
CAP_CAMERAPREVIEWUI                = 0x1021
CAP_DEVICEEVENT                    = 0x1022
CAP_SERIALNUMBER                   = 0x1024
CAP_PRINTER                        = 0x1026
CAP_PRINTERENABLED                 = 0x1027
CAP_PRINTERINDEX                   = 0x1028
CAP_PRINTERMODE                    = 0x1029
CAP_PRINTERSTRING                  = 0x102a
CAP_PRINTERSUFFIX                  = 0x102b
CAP_LANGUAGE                       = 0x102c
CAP_FEEDERALIGNMENT                = 0x102d
CAP_FEEDERORDER                    = 0x102e
CAP_REACQUIREALLOWED               = 0x1030
CAP_BATTERYMINUTES                 = 0x1032
CAP_BATTERYPERCENTAGE              = 0x1033
CAP_CAMERASIDE                     = 0x1034
CAP_SEGMENTED                      = 0x1035
CAP_CAMERAENABLED                  = 0x1036
CAP_CAMERAORDER                    = 0x1037
CAP_MICRENABLED                    = 0x1038
CAP_FEEDERPREP                     = 0x1039
CAP_FEEDERPOCKET                   = 0x103a
CAP_AUTOMATICSENSEMEDIUM           = 0x103b
CAP_CUSTOMINTERFACEGUID            = 0x103c
CAP_SUPPORTEDCAPSSEGMENTUNIQUE     = 0x103d
CAP_SUPPORTEDDATS                  = 0x103e
CAP_DOUBLEFEEDDETECTION            = 0x103f
CAP_DOUBLEFEEDDETECTIONLENGTH      = 0x1040
CAP_DOUBLEFEEDDETECTIONSENSITIVITY = 0x1041
CAP_DOUBLEFEEDDETECTIONRESPONSE    = 0x1042
CAP_PAPERHANDLING                  = 0x1043
CAP_INDICATORSMODE                 = 0x1044
CAP_PRINTERVERTICALOFFSET          = 0x1045
CAP_POWERSAVETIME                  = 0x1046
CAP_PRINTERCHARROTATION            = 0x1047
CAP_PRINTERFONTSTYLE               = 0x1048
CAP_PRINTERINDEXLEADCHAR           = 0x1049
CAP_PRINTERINDEXMAXVALUE           = 0x104A
CAP_PRINTERINDEXNUMDIGITS          = 0x104B
CAP_PRINTERINDEXSTEP               = 0x104C
CAP_PRINTERINDEXTRIGGER            = 0x104D
CAP_PRINTERSTRINGPREVIEW           = 0x104E
CAP_SHEETCOUNT                     = 0x104F
CAP_IMAGEADDRESSENABLED            = 0x1050
CAP_IAFIELDA_LEVEL                 = 0x1051
CAP_IAFIELDB_LEVEL                 = 0x1052
CAP_IAFIELDC_LEVEL                 = 0x1053
CAP_IAFIELDD_LEVEL                 = 0x1054
CAP_IAFIELDE_LEVEL                 = 0x1055
CAP_IAFIELDA_PRINTFORMAT           = 0x1056
CAP_IAFIELDB_PRINTFORMAT           = 0x1057
CAP_IAFIELDC_PRINTFORMAT           = 0x1058
CAP_IAFIELDD_PRINTFORMAT           = 0x1059
CAP_IAFIELDE_PRINTFORMAT           = 0x105A
CAP_IAFIELDA_VALUE                 = 0x105B
CAP_IAFIELDB_VALUE                 = 0x105C
CAP_IAFIELDC_VALUE                 = 0x105D
CAP_IAFIELDD_VALUE                 = 0x105E
CAP_IAFIELDE_VALUE                 = 0x105F
CAP_IAFIELDA_LASTPAGE              = 0x1060
CAP_IAFIELDB_LASTPAGE              = 0x1061
CAP_IAFIELDC_LASTPAGE              = 0x1062
CAP_IAFIELDD_LASTPAGE              = 0x1063
CAP_IAFIELDE_LASTPAGE              = 0x1064

# image data sources MAY support these caps
ICAP_AUTOBRIGHT                    = 0x1100
ICAP_BRIGHTNESS                    = 0x1101
ICAP_CONTRAST                      = 0x1103
ICAP_CUSTHALFTONE                  = 0x1104
ICAP_EXPOSURETIME                  = 0x1105
ICAP_FILTER                        = 0x1106
ICAP_FLASHUSED                     = 0x1107
ICAP_GAMMA                         = 0x1108
ICAP_HALFTONES                     = 0x1109
ICAP_HIGHLIGHT                     = 0x110a
ICAP_IMAGEFILEFORMAT               = 0x110c
ICAP_LAMPSTATE                     = 0x110d
ICAP_LIGHTSOURCE                   = 0x110e
ICAP_ORIENTATION                   = 0x1110
ICAP_PHYSICALWIDTH                 = 0x1111
ICAP_PHYSICALHEIGHT                = 0x1112
ICAP_SHADOW                        = 0x1113
ICAP_FRAMES                        = 0x1114
ICAP_XNATIVERESOLUTION             = 0x1116
ICAP_YNATIVERESOLUTION             = 0x1117
ICAP_XRESOLUTION                   = 0x1118
ICAP_YRESOLUTION                   = 0x1119
ICAP_MAXFRAMES                     = 0x111a
ICAP_TILES                         = 0x111b
ICAP_BITORDER                      = 0x111c
ICAP_CCITTKFACTOR                  = 0x111d
ICAP_LIGHTPATH                     = 0x111e
ICAP_PIXELFLAVOR                   = 0x111f
ICAP_PLANARCHUNKY                  = 0x1120
ICAP_ROTATION                      = 0x1121
ICAP_SUPPORTEDSIZES                = 0x1122
ICAP_THRESHOLD                     = 0x1123
ICAP_XSCALING                      = 0x1124
ICAP_YSCALING                      = 0x1125
ICAP_BITORDERCODES                 = 0x1126
ICAP_PIXELFLAVORCODES              = 0x1127
ICAP_JPEGPIXELTYPE                 = 0x1128
ICAP_TIMEFILL                      = 0x112a
ICAP_BITDEPTH                      = 0x112b
ICAP_BITDEPTHREDUCTION             = 0x112c
ICAP_UNDEFINEDIMAGESIZE            = 0x112d
ICAP_IMAGEDATASET                  = 0x112e
ICAP_EXTIMAGEINFO                  = 0x112f
ICAP_MINIMUMHEIGHT                 = 0x1130
ICAP_MINIMUMWIDTH                  = 0x1131
ICAP_AUTODISCARDBLANKPAGES         = 0x1134
ICAP_FLIPROTATION                  = 0x1136
ICAP_BARCODEDETECTIONENABLED       = 0x1137
ICAP_SUPPORTEDBARCODETYPES         = 0x1138
ICAP_BARCODEMAXSEARCHPRIORITIES    = 0x1139
ICAP_BARCODESEARCHPRIORITIES       = 0x113a
ICAP_BARCODESEARCHMODE             = 0x113b
ICAP_BARCODEMAXRETRIES             = 0x113c
ICAP_BARCODETIMEOUT                = 0x113d
ICAP_ZOOMFACTOR                    = 0x113e
ICAP_PATCHCODEDETECTIONENABLED     = 0x113f
ICAP_SUPPORTEDPATCHCODETYPES       = 0x1140
ICAP_PATCHCODEMAXSEARCHPRIORITIES  = 0x1141
ICAP_PATCHCODESEARCHPRIORITIES     = 0x1142
ICAP_PATCHCODESEARCHMODE           = 0x1143
ICAP_PATCHCODEMAXRETRIES           = 0x1144
ICAP_PATCHCODETIMEOUT              = 0x1145
ICAP_FLASHUSED2                    = 0x1146
ICAP_IMAGEFILTER                   = 0x1147
ICAP_NOISEFILTER                   = 0x1148
ICAP_OVERSCAN                      = 0x1149
ICAP_AUTOMATICBORDERDETECTION      = 0x1150
ICAP_AUTOMATICDESKEW               = 0x1151
ICAP_AUTOMATICROTATE               = 0x1152
ICAP_JPEGQUALITY                   = 0x1153
ICAP_FEEDERTYPE                    = 0x1154
ICAP_ICCPROFILE                    = 0x1155
ICAP_AUTOSIZE                      = 0x1156
ICAP_AUTOMATICCROPUSESFRAME        = 0x1157
ICAP_AUTOMATICLENGTHDETECTION      = 0x1158
ICAP_AUTOMATICCOLORENABLED         = 0x1159
ICAP_AUTOMATICCOLORNONCOLORPIXELTYPE = 0x115a
ICAP_COLORMANAGEMENTENABLED        = 0x115b
ICAP_IMAGEMERGE                    = 0x115c
ICAP_IMAGEMERGEHEIGHTTHRESHOLD     = 0x115d
ICAP_SUPPORTEDEXTIMAGEINFO         = 0x115e
ICAP_FILMTYPE                      = 0x115f
ICAP_MIRROR                        = 0x1160
ICAP_JPEGSUBSAMPLING               = 0x1161

# image data sources MAY support these audio caps
ACAP_XFERMECH                      = 0x1202

#***************************************************************************#
#            Extended Image Info Attributes section  Added 1.7              #
#***************************************************************************#

TWEI_BARCODEX              = 0x1200
TWEI_BARCODEY              = 0x1201
TWEI_BARCODETEXT           = 0x1202
TWEI_BARCODETYPE           = 0x1203
TWEI_DESHADETOP            = 0x1204
TWEI_DESHADELEFT           = 0x1205
TWEI_DESHADEHEIGHT         = 0x1206
TWEI_DESHADEWIDTH          = 0x1207
TWEI_DESHADESIZE           = 0x1208
TWEI_SPECKLESREMOVED       = 0x1209
TWEI_HORZLINEXCOORD        = 0x120A
TWEI_HORZLINEYCOORD        = 0x120B
TWEI_HORZLINELENGTH        = 0x120C
TWEI_HORZLINETHICKNESS     = 0x120D
TWEI_VERTLINEXCOORD        = 0x120E
TWEI_VERTLINEYCOORD        = 0x120F
TWEI_VERTLINELENGTH        = 0x1210
TWEI_VERTLINETHICKNESS     = 0x1211
TWEI_PATCHCODE             = 0x1212
TWEI_ENDORSEDTEXT          = 0x1213
TWEI_FORMCONFIDENCE        = 0x1214
TWEI_FORMTEMPLATEMATCH     = 0x1215
TWEI_FORMTEMPLATEPAGEMATCH = 0x1216
TWEI_FORMHORZDOCOFFSET     = 0x1217
TWEI_FORMVERTDOCOFFSET     = 0x1218
TWEI_BARCODECOUNT          = 0x1219
TWEI_BARCODECONFIDENCE     = 0x121A
TWEI_BARCODEROTATION       = 0x121B
TWEI_BARCODETEXTLENGTH     = 0x121C
TWEI_DESHADECOUNT          = 0x121D
TWEI_DESHADEBLACKCOUNTOLD  = 0x121E
TWEI_DESHADEBLACKCOUNTNEW  = 0x121F
TWEI_DESHADEBLACKRLMIN     = 0x1220
TWEI_DESHADEBLACKRLMAX     = 0x1221
TWEI_DESHADEWHITECOUNTOLD  = 0x1222
TWEI_DESHADEWHITECOUNTNEW  = 0x1223
TWEI_DESHADEWHITERLMIN     = 0x1224
TWEI_DESHADEWHITERLAVE     = 0x1225
TWEI_DESHADEWHITERLMAX     = 0x1226
TWEI_BLACKSPECKLESREMOVED  = 0x1227
TWEI_WHITESPECKLESREMOVED  = 0x1228
TWEI_HORZLINECOUNT         = 0x1229
TWEI_VERTLINECOUNT         = 0x122A
TWEI_DESKEWSTATUS          = 0x122B
TWEI_SKEWORIGINALANGLE     = 0x122C
TWEI_SKEWFINALANGLE        = 0x122D
TWEI_SKEWCONFIDENCE        = 0x122E
TWEI_SKEWWINDOWX1          = 0x122F
TWEI_SKEWWINDOWY1          = 0x1230
TWEI_SKEWWINDOWX2          = 0x1231
TWEI_SKEWWINDOWY2          = 0x1232
TWEI_SKEWWINDOWX3          = 0x1233
TWEI_SKEWWINDOWY3          = 0x1234
TWEI_SKEWWINDOWX4          = 0x1235
TWEI_SKEWWINDOWY4          = 0x1236
TWEI_BOOKNAME              = 0x1238
TWEI_CHAPTERNUMBER         = 0x1239
TWEI_DOCUMENTNUMBER        = 0x123A
TWEI_PAGENUMBER            = 0x123B
TWEI_CAMERA                = 0x123C
TWEI_FRAMENUMBER           = 0x123D
TWEI_FRAME                 = 0x123E
TWEI_PIXELFLAVOR           = 0x123F
TWEI_ICCPROFILE            = 0x1240
TWEI_LASTSEGMENT           = 0x1241
TWEI_SEGMENTNUMBER         = 0x1242
TWEI_MAGDATA               = 0x1243
TWEI_MAGTYPE               = 0x1244
TWEI_PAGESIDE              = 0x1245
TWEI_FILESYSTEMSOURCE      = 0x1246
TWEI_IMAGEMERGED           = 0x1247
TWEI_MAGDATALENGTH         = 0x1248
TWEI_PAPERCOUNT            = 0x1249
TWEI_PRINTERTEXT           = 0x124A
TWEI_TWAINDIRECTMETADATA   = 0x124B
TWEI_IAFIELDA_VALUE        = 0x124C
TWEI_IAFIELDB_VALUE        = 0x124D
TWEI_IAFIELDC_VALUE        = 0x124E
TWEI_IAFIELDD_VALUE        = 0x124F
TWEI_IAFIELDE_VALUE        = 0x1250
TWEI_IALEVEL               = 0x1251
TWEI_PRINTER               = 0x1252
TWEI_BARCODETEXT2          = 0x1253

TWEJ_NONE         = 0x0000
TWEJ_MIDSEPARATOR = 0x0001
TWEJ_PATCH1       = 0x0002
TWEJ_PATCH2       = 0x0003
TWEJ_PATCH3       = 0x0004
TWEJ_PATCH4       = 0x0005
TWEJ_PATCH6       = 0x0006
TWEJ_PATCHT       = 0x0007

#***************************************************************************#
#            Return Codes and Condition Codes section                       #
#***************************************************************************#

TWRC_CUSTOMBASE       = 0x8000
TWRC_SUCCESS          = 0
TWRC_FAILURE          = 1
TWRC_CHECKSTATUS      = 2
TWRC_CANCEL           = 3
TWRC_DSEVENT          = 4
TWRC_NOTDSEVENT       = 5
TWRC_XFERDONE         = 6
TWRC_ENDOFLIST        = 7
TWRC_INFONOTSUPPORTED = 8
TWRC_DATANOTAVAILABLE = 9
TWRC_BUSY             = 10
TWRC_SCANNERLOCKED    = 11

# Condition Codes: Application gets these by doing DG_CONTROL DAT_STATUS
# MSG_GET.
TWCC_CUSTOMBASE        = 0x8000
TWCC_SUCCESS           = 0
TWCC_BUMMER            = 1
TWCC_LOWMEMORY         = 2
TWCC_NODS              = 3
TWCC_MAXCONNECTIONS    = 4
TWCC_OPERATIONERROR    = 5
TWCC_BADCAP            = 6
TWCC_BADPROTOCOL       = 9
TWCC_BADVALUE          = 10
TWCC_SEQERROR          = 11
TWCC_BADDEST           = 12
TWCC_CAPUNSUPPORTED    = 13
TWCC_CAPBADOPERATION   = 14
TWCC_CAPSEQERROR       = 15
TWCC_DENIED            = 16
TWCC_FILEEXISTS        = 17
TWCC_FILENOTFOUND      = 18
TWCC_NOTEMPTY          = 19
TWCC_PAPERJAM          = 20
TWCC_PAPERDOUBLEFEED   = 21
TWCC_FILEWRITEERROR    = 22
TWCC_CHECKDEVICEONLINE = 23
TWCC_INTERLOCK         = 24
TWCC_DAMAGEDCORNER     = 25
TWCC_FOCUSERROR        = 26
TWCC_DOCTOOLIGHT       = 27
TWCC_DOCTOODARK        = 28
TWCC_NOMEDIA           = 29

# bit patterns: for query the operation that are supported by the data source
# on a capability
# Application gets these through DG_CONTROL/DAT_CAPABILITY/MSG_QUERYSUPPORT
TWQC_GET           = 0x0001
TWQC_SET           = 0x0002
TWQC_GETDEFAULT    = 0x0004
TWQC_GETCURRENT    = 0x0008
TWQC_RESET         = 0x0010
TWQC_SETCONSTRAINT = 0x0020
TWQC_GETHELP       = 0x0100
TWQC_GETLABEL      = 0x0200
TWQC_GETLABELENUM  = 0x0400

#***************************************************************************#
# Depreciated Items                                                         #
#***************************************************************************#

HPBYTE = ct.POINTER(BYTE)
HPVOID = ct.c_void_p

TW_STR1024 = ct.c_ubyte * 1026 ; pTW_STR1024 = pTW_STR1026 = ct.POINTER(TW_STR1024)
TW_UNI512  = ct.c_wchar * 512  ; pTW_UNI512  = ct.POINTER(TW_UNI512)

TWTY_STR1024 = 0x000d
TWTY_UNI512  = 0x000e

TWFF_JPN = 12

DAT_TWUNKIDENTITY  = 0x000b
DAT_SETUPFILEXFER2 = 0x0301

CAP_CLEARBUFFERS        = 0x101d
CAP_SUPPORTEDCAPSEXT    = 0x100c
CAP_FILESYSTEM          = "????"  # 0x????
CAP_PAGEMULTIPLEACQUIRE = 0x1023
CAP_PAPERBINDING        = 0x102f
CAP_PASSTHRU            = 0x1031
CAP_POWERDOWNTIME       = 0x1034
ACAP_AUDIOFILEFORMAT    = 0x1201

MSG_CHECKSTATUS     = 0x0201
# Mac Only, deprecated - use DAT_NULL and MSG_xxx instead
MSG_INVOKE_CALLBACK = 0x0903

TWQC_CONSTRAINABLE = 0x0040

TWSX_FILE2 = 3

# CAP_FILESYSTEM values (FS_ means file system)
TWFS_FILESYSTEM      = 0
TWFS_RECURSIVEDELETE = 1

# ICAP_PIXELTYPE values (PT_ means Pixel Type)
TWPT_SRGB64 = 11
TWPT_BGR    = 12
TWPT_CIELAB = 13
TWPT_CIELUV = 14
TWPT_YCBCR  = 15

# ICAP_SUPPORTEDSIZES values (SS_ means Supported Sizes)
TWSS_B        = 8
TWSS_A4LETTER = TWSS_A4
TWSS_B3       = TWSS_ISOB3
TWSS_B4       = TWSS_ISOB4
TWSS_B6       = TWSS_ISOB6
TWSS_B5LETTER = TWSS_JISB5

# ACAP_AUDIOFILEFORMAT values (AF_ means audio format).  Added 1.8
TWAF_WAV  = 0
TWAF_AIFF = 1
TWAF_AU   = 3
TWAF_SND  = 4

# CAP_CLEARBUFFERS values
TWCB_AUTO    = 0
TWCB_CLEAR   = 1
TWCB_NOCLEAR = 2

# DAT_SETUPFILEXFER2. Sets up DS to application data transfer via a file.
# Added 1.9
class TW_SETUPFILEXFER2(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("FileName",     TW_MEMREF),
    ("FileNameType", TW_UINT16),
    ("Format",       TW_UINT16),
    ("VRefNum",      TW_INT16),
    ("parID",        TW_UINT32),
]
pTW_SETUPFILEXFER2 = ct.POINTER(TW_SETUPFILEXFER2)

# DAT_TWUNKIDENTITY. Provides DS identity and 'other' information necessary
#                    across thunk link.
class TW_TWUNKIDENTITY(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("identity", TW_IDENTITY),
    ("dsPath",   TW_STR255),
]
pTW_TWUNKIDENTITY = ct.POINTER(TW_TWUNKIDENTITY)

# Provides DS_Entry parameters over thunk link.
class TW_TWUNKDSENTRYPARAMS(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("destFlag",    TW_INT8),
    ("dest",        TW_IDENTITY),
    ("dataGroup",   TW_INT32),
    ("dataArgType", TW_INT16),
    ("message",     TW_INT16),
    ("pDataSize",   TW_INT32),
    # ("pData",     TW_MEMREF),
]
pTW_TWUNKDSENTRYPARAMS = ct.POINTER(TW_TWUNKDSENTRYPARAMS)

# Provides DS_Entry results over thunk link.
class TW_TWUNKDSENTRYRETURN(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("returnCode",    TW_UINT16),
    ("conditionCode", TW_UINT16),
    ("pDataSize",     TW_INT32),
    # ("pData",       TW_MEMREF),
]
pTW_TWUNKDSENTRYRETURN = ct.POINTER(TW_TWUNKDSENTRYRETURN)

class TW_CAPEXT(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("Cap",        TW_UINT16),
    ("Properties", TW_UINT16),
]
pTW_CAPEXT = ct.POINTER(TW_CAPEXT)

# DAT_SETUPAUDIOFILEXFER, information required to setup an audio
# file transfer
class TW_SETUPAUDIOFILEXFER(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("FileName", TW_STR255),  # full path target file
    ("Format",   TW_UINT16),  # one of TWAF_xxxx
    ("VRefNum",  TW_INT16),
]
pTW_SETUPAUDIOFILEXFER = ct.POINTER(TW_SETUPAUDIOFILEXFER)

#***************************************************************************#
# Entry Points                                                              #
#***************************************************************************#

#*************************************************************************#
# Function: DSM_Entry, the only entry point into the Data Source Manager. #
#*************************************************************************#

DSMENTRYPROC = CFUNC(TW_UINT16,
                     pTW_IDENTITY, pTW_IDENTITY,
                     TW_UINT32, TW_UINT16, TW_UINT16, TW_MEMREF)

#*************************************************************************#
# Function: DS_Entry, the entry point provided by a Data Source.          #
#*************************************************************************#

DSENTRYPROC = CFUNC(TW_UINT16,
                    pTW_IDENTITY,
                    TW_UINT32, TW_UINT16, TW_UINT16, TW_MEMREF)

TWAINCALLBACKPROC = CFUNC(TW_UINT16,
                          pTW_IDENTITY, pTW_IDENTITY,
                          TW_UINT32, TW_UINT16, TW_UINT16, TW_MEMREF)

#******************#
# Helpers          #
#******************#

DSM_MEMALLOCATE = CFUNC(TW_HANDLE, TW_UINT32)
DSM_MEMFREE     = CFUNC(None,      TW_HANDLE)
DSM_MEMLOCK     = CFUNC(TW_MEMREF, TW_HANDLE)
DSM_MEMUNLOCK   = CFUNC(None,      TW_HANDLE)

# DAT_ENTRYPOINT. returns essential entry points.
class TW_ENTRYPOINT(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("Size",            TW_UINT32),
    ("DSM_Entry",       DSMENTRYPROC),
    ("DSM_MemAllocate", DSM_MEMALLOCATE),
    ("DSM_MemFree",     DSM_MEMFREE),
    ("DSM_MemLock",     DSM_MEMLOCK),
    ("DSM_MemUnlock",   DSM_MEMUNLOCK),
]
pTW_ENTRYPOINT = ct.POINTER(TW_ENTRYPOINT)

# DAT_FILTER
class TW_FILTER_DESCRIPTOR(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("Size",            TW_UINT32),
    ("HueStart",        TW_UINT32),
    ("HueEnd",          TW_UINT32),
    ("SaturationStart", TW_UINT32),
    ("SaturationEnd",   TW_UINT32),
    ("ValueStart",      TW_UINT32),
    ("ValueEnd",        TW_UINT32),
    ("Replacement",     TW_UINT32),
]
pTW_FILTER_DESCRIPTOR = ct.POINTER(TW_FILTER_DESCRIPTOR)

# DAT_FILTER
class TW_FILTER(ct.Structure):
    _pack_ = _pack
    _fields_ = [
    ("Size",               TW_UINT32),
    ("DescriptorCount",    TW_UINT32),
    ("MaxDescriptorCount", TW_UINT32),
    ("Condition",          TW_UINT32),
    ("hDescriptors",       TW_HANDLE),
]
pTW_FILTER = ct.POINTER(TW_FILTER)

# ========================================================================= #

try:
    DSM_Entry = DSMENTRYPROC(("DSM_Entry", dll), (
                             (1, "pOrigin"),
                             (1, "pDest"),
                             (1, "DG"),
                             (1, "DAT"),
                             (1, "MSG"),
                             (1, "pData"),))
except: pass  # noqa: E722

# eof
