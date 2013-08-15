Utility to run SAX (SHARP APL for UNIX™) on a UTF-8 terminal
=======================================

This is a simple fork of luit-1.1.1, as distributed by Xorg, that adds a custom character encoding. The encoding is called "SAX" and allows you to run SHARP APL for UNIX™ on a regular UTF-8 terminal, provided you have a suitable font and input method on your system, to display and enter Unicode APL characters.

The encoding is taken from SHARP APL for UNIX™ Language Guide, Chapter 3, Table 3.1. "APL Character Set". All charactes are mapped to their Unicode codepoints, both when output and during terminal input.

Luit was chosen as a basis for this utility because it's a well-known and debugged tool to perform this very task, handling all aspects and corner cases.

The following characters were replaced with graphically similar ones, since they are not part of Unicode, I didn't want to use combining characters, and I shamefully ignore their purpose in SAX. Patches are welcome, if you can offer a better translation:
- 0x01 should be a semicolon overbar according to the manual, but is mapped to U+236E semicolon underbar by this software;
- 0xf6 should be a star overbar, but is mapped to U+2363 star diaeresis.

How to compile and install it
--------------------------------

Get the necessary requirements to build the original luit on your system. For example on Debian you need `build-essential`, `pkg-config`, and `libfontenc-dev`. Then download this fork, enter its directory and issue:

	./configure --with-localealiasfile=/usr/share/X11/locale/locale.alias
	make

You should be able to issue `./luit -list` and see "SAX" listed as an available charset. Then install this version into `/usr/local/bin`:

	sudo make install

How to use it
---------------

Save this script as `/usr/local/bin/sax`:

	#!/bin/sh
	unset DISPLAY
	exec /usr/local/bin/luit -encoding SAX /usr/sax/rel/bin/sax

You should be able to type `sax` and be presented with a Unicode terminal version of SAX (type `)off` to exit.)
