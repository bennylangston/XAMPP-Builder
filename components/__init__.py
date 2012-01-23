"""
  XAMPP Builder
  Copyright 2011 Apache Friends, GPLv2+ licensed
  ==============================================

"""

import components.zlib.ZLib
import components.openssl.OpenSSL
import components.libjpeg.LibJPEG
import components.libltdl.LibLTDL
import components.libpng.LibPNG
import components.libxml.LibXML
import components.libxslt.LibXSLT
import components.ncurses.Ncurses
import components.sqlite.SQLite
import components.expat.Expat
import components.freetype.FreeType
import components.apache.Apache
import components.mysql.MySQL
import components.proftpd.ProFTPd
import components.perl.Perl
import components.postgresql.Postgresql

KNOWN_COMPONENTS = [
	components.zlib.ZLib,
	components.openssl.OpenSSL,
	components.libjpeg.LibJPEG,
#	components.libltdl.LibLTDL,
	components.libpng.LibPNG,
	components.libxml.LibXML,
	components.libxslt.LibXSLT,
	components.ncurses.Ncurses,
	components.sqlite.SQLite,
	components.expat.Expat,
	components.freetype.FreeType,
	components.apache.Apache,
	components.mysql.MySQL,
	components.proftpd.ProFTPd,
	components.perl.Perl,
#	components.postgresql.Postgresql
]