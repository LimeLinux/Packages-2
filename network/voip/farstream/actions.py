#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr \
                         --with-html-dir=/%s/%s/html \
                         --with-package-name='limelinux farstream package' \
                         --with-package-origin='http://www.limelinux.org'"
                         % (get.docDIR(), get.srcNAME()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "INSTALL", "COPYING", "NEWS", "README")
