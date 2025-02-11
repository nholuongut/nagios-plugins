#!/usr/bin/env python3
#  coding=utf-8
#  vim:ts=4:sts=4:sw=4:et
#
#  Author: Nho Luong
#  Date: 2017-09-06 13:09:35 +0200 (Wed, 06 Sep 2017)
#
#  nholuongut/nagios-pnholuongut/nagios-plugins
#
#  License: see accompanying Hari Sekhon LICENSE file
#
#  If you're using my code you're welcome to connect with me on LinkedIn
#  and optionally send me feedback to help steer this or other code I publish
#
#  https://www.linkedin.com/in/nholuong
#

"""

Nagios Plugin to check the version of the Hadoop NameNode via the JMX API

Tested on HDP 2.6.1 and Apache Hadoop 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import sys
import traceback
srcdir = os.path.abspath(os.path.dirname(__file__))
libdir = os.path.join(srcdir, 'pylib')
sys.path.append(libdir)
try:
    # pylint: disable=wrong-import-position
    from harisekhon.utils import UnknownError
    from harisekhon import RestVersionNagiosPlugin
except ImportError:
    print(traceback.format_exc(), end='')
    sys.exit(4)

__author__ = 'Hari Sekhon'
__version__ = '0.2'


# pylint: disable=too-few-public-methods
class CheckHadoopNameNodeVersion(RestVersionNagiosPlugin):

    def __init__(self):
        # Python 2.x
        super(CheckHadoopNameNodeVersion, self).__init__()
        # Python 3.x
        # super().__init__()
        self.name = 'Hadoop NameNode'
        self.default_port = 50070
        self.path = '/jmx?qry=Hadoop:service=NameNode,name=NameNodeInfo'
        self.json = True
        self.auth = False
        self.ok()

    # must override, cannot change to @staticmethod
    def parse_json(self, json_data):  # pylint: disable=no-self-use
        data = json_data['beans'][0]
        if data['name'] != 'Hadoop:service=NameNode,name=NameNodeInfo':
            raise UnknownError('name {} != Hadoop:service=NameNode,name=NameNodeInfo'.format(data['name']))
        version = data['Version']
        #log.info("raw version = '%s'", version)
        version = version.split(',')[0]
        return version


if __name__ == '__main__':
    CheckHadoopNameNodeVersion().main()
