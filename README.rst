libtwain
========

Python binding for the *libtwain* C library.

Overview
========

| Python |package_bold| module is a low-level binding for *libtwain* C library.
| It is an effort to allow python programs full access to the API provided
  by the well known *libtwain* Unix C library and by its implementations
  provided under Win32 systems by such packet capture systems as:
  `Npcap <https://nmap.org/npcap/>`__,
  `WinPcap <https://www.winpcap.org>`__

`PyPI record`_.

`Documentation`_.

| *libtwain* is a lightweight Python package, based on the *ctypes* library.
| It is fully compliant implementation of the original C *libtwain* from
  1.0.0 up to 1.9.0 API and the *WinPcap*'s 4.1.3 libtwain (1.0.0rel0b) API
  by implementing whole its functionality in a clean Python instead of C.
|
| Useful *libtwain* API documentation can be found at:

  | `Main pcap man page <https://www.tcpdump.org/manpages/pcap.3pcap.html>`__,
  | `(MORE pcap man pages) <https://www.tcpdump.org/manpages/>`__

About original LIBPCAP:
-----------------------

| LIBPCAP 1.x.y
| Now maintained by "The Tcpdump Group"
| https://www.tcpdump.org

Anonymous Git is available via:

    git clone git://bpf.tcpdump.org/|package|

formerly from:

  | Lawrence Berkeley National Laboratory
  | Network Research Group <libtwain@ee.lbl.gov>
  | ftp://ftp.ee.lbl.gov/old/libtwain-0.4a7.tar.Z

This directory contains source code for libtwain, a system-independent
interface for user-level packet capture.  libtwain provides a portable
framework for low-level network monitoring.  Applications include
network statistics collection, security monitoring, network debugging,
etc.  Since almost every system vendor provides a different interface
for packet capture, and since we've developed several tools that
require this functionality, we've created this system-independent API
to ease in porting and to alleviate the need for several
system-dependent packet capture modules in each application.

For some platforms there are README.{system} files that discuss issues
with the OS's interface for packet capture on those platforms, such as
how to enable support for that interface in the OS, if it's not built in
by default.

The libtwain interface supports a filtering mechanism based on the
architecture in the BSD packet filter.  BPF is described in the 1993
Winter Usenix paper "The BSD Packet Filter: A New Architecture for
User-level Packet Capture".  A compressed PostScript version can be
found at:

    ftp://ftp.ee.lbl.gov/papers/bpf-usenix93.ps.Z

or:

    https://www.tcpdump.org/papers/bpf-usenix93.ps.Z

and a gzipped version can be found at:

    https://www.tcpdump.org/papers/bpf-usenix93.ps.gz

A PDF version can be found at:

    https://www.tcpdump.org/papers/bpf-usenix93.pdf

Although most packet capture interfaces support in-kernel filtering,
libtwain utilizes in-kernel filtering only for the BPF interface.
On systems that don't have BPF, all packets are read into user-space
and the BPF filters are evaluated in the libtwain library, incurring
added overhead (especially, for selective filters).  Ideally, libtwain
would translate BPF filters into a filter program that is compatible
with the underlying kernel subsystem, but this is not yet implemented.

BPF is standard in 4.4BSD, BSD/OS, NetBSD, FreeBSD, OpenBSD, DragonFly
BSD, and Mac OS X; an older, modified and undocumented version is
standard in AIX.  DEC OSF/1, Digital UNIX, Tru64 UNIX uses the
packetfilter interface but has been extended to accept BPF filters
(which libtwain utilizes).  Also, you can add BPF filter support to
Ultrix using the kernel source and/or object patches available in:

    https://www.tcpdump.org/other/bpfext42.tar.Z

Linux, in the 2.2 kernel and later kernels, has a "Socket Filter"
mechanism that accepts BPF filters; see the README.linux file for
information on configuring that option.

Note to Linux distributions and \*BSD systems that include libtwain:

There's now a rule to make a shared library, which should work on Linux
and \*BSD, among other platforms.

It sets the soname of the library to "libtwain.so.1"; this is what it
should be, *NOT* libtwain.so.1.x or libtwain.so.1.x.y or something such as
that.

We've been maintaining binary compatibility between libtwain releases for
quite a while; there's no reason to tie a binary linked with libtwain to
a particular release of libtwain.

Current versions can be found at: https://www.tcpdump.org

\- The TCPdump group

Requirements
============

- | It is a fully independent package.
  | All necessary things are installed during the normal installation process.
- ATTENTION: currently works and tested only for Windows.

Installation
============

Prerequisites:

+ Python 3.8 or higher

  * https://www.python.org/
  * with C libtwain 1.8.1 are primary test environments.

+ pip and setuptools

  * https://pypi.org/project/pip/
  * https://pypi.org/project/setuptools/

To install run:

  .. parsed-literal::

    python -m pip install --upgrade |package|

Development
===========

Prerequisites:

+ Development is strictly based on *tox*. To install it run::

    python -m pip install --upgrade tox

Visit `Development page`_.

Installation from sources:

clone the sources:

  .. parsed-literal::

    git clone |respository| |package|

and run:

  .. parsed-literal::

    python -m pip install ./|package|

or on development mode:

  .. parsed-literal::

    python -m pip install --editable ./|package|

License
=======

  | Copyright (c) 2016-2024 Adam Karpierz
  | Licensed under the zlib/libpng License
  | https://opensource.org/license/zlib
  | Please refer to the accompanying LICENSE file.

Authors
=======

* Adam Karpierz <adam@karpierz.net>

.. |package| replace:: libtwain
.. |package_bold| replace:: **libtwain**
.. |respository| replace:: https://github.com/karpierz/libtwain.git
.. _Development page: https://github.com/karpierz/libtwain
.. _PyPI record: https://pypi.org/project/libtwain/
.. _Documentation: https://libtwain.readthedocs.io/
