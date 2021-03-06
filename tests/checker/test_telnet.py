# Copyright (C) 2004-2012 Bastian Kleineidam
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""
Test telnet checking.
"""
from .telnetserver import TelnetServerTest


class TestTelnet(TelnetServerTest):
    """Test telnet: link checking."""

    def test_telnet_error(self):
        url = "telnet:"
        nurl = self.norm(url)
        resultlines = [
            "url %s" % url,
            "cache key None",
            "real url %s" % nurl,
            "error",
        ]
        self.direct(url, resultlines)

    def test_telnet_localhost(self):
        url = self.get_url()
        resultlines = [
            "url %s" % url,
            "cache key %s" % url,
            "real url %s" % url,
            "valid",
        ]
        self.direct(url, resultlines)
        url = self.get_url(user="test")
        resultlines = [
            "url %s" % url,
            "cache key %s" % url,
            "real url %s" % url,
            "valid",
        ]
        self.direct(url, resultlines)
        url = self.get_url(user="test", password="test")
        resultlines = [
            "url %s" % url,
            "cache key %s" % url,
            "real url %s" % url,
            "valid",
        ]
        self.direct(url, resultlines)
