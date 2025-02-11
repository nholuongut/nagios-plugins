#!/usr/bin/env python3
#  vim:ts=4:sts=4:sw=4:et
#
#  Author: Nho Luong
#  Date: 2016-02-18 18:44:59 +0000 (Thu, 18 Feb 2016)
#
#  nholuongut/nagios-pnholuongut/nagios-plugins
#
#  License: see accompanying Hari Sekhon LICENSE file
#
#  If you're using my code you're welcome to connect with me on LinkedIn and optionally send me feedback # pylint: disable=line-too-long
#
#  https://www.linkedin.com/in/nholuong
#

"""

Nagios Plugin to check Apache Drill's status via its Rest API

The API has limitations around reflecting Drill issues however, see:

https://issues.apache.org/jira/browse/DRILL-5990
https://issues.apache.org/jira/browse/DRILL-6406

Recommend if running a cluster to also use:

    ./check_apache_drill_cluster_node.py - for a specific node
    ./check_apache_drill_cluster_nodes.py - to check minimum number of nodes in cluster
    ./check_apache_drill_cluster_nodes_offline.py - to check for number of down nodes

Tested on Apache Drill 1.7, 1.8, 1.9, 1.10, 1.11, 1.12, 1.13, 1.14, 1.15

(API endpoint is not available in Apache Drill versions < 1.7, see check_apache_drill_status.py instead)

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import os
import re
import sys
import traceback
libdir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'pylib'))
sys.path.append(libdir)
try:
    # pylint: disable=wrong-import-position
    from harisekhon import StatusNagiosPlugin
    from harisekhon import RequestHandler
except ImportError:
    print(traceback.format_exc(), end='')
    sys.exit(4)

__author__ = 'Hari Sekhon'
__version__ = '0.3'


class CheckApacheDrillStatus(StatusNagiosPlugin):

    def __init__(self):
        # Python 2.x
        super(CheckApacheDrillStatus, self).__init__()
        # Python 3.x
        # super().__init__()
        self.name = 'Apache Drill'
        self.default_port = 8047

    def get_status(self):
        url = 'http://{0}:{1}/status.json'.format(self.host, self.port)
        req = RequestHandler().get(url)
        status = self.parse(req)
        return status

    def parse(self, req):
        json_data = json.loads(req.content)
        status = json_data['status']
        # Found a STARTUP status in cluster nodes state but looking at the code for /status is looks like Running is all there is, or results for this endpoint are not properly undocumented - see https://issues.apache.org/jira/browse/DRILL-6407
        #if status in ("Startup", "Initializing"):
        #    self.warning()
        if re.match('^Running!?$', status):
            self.ok()
        else:
            self.critical()
        return status


if __name__ == '__main__':
    CheckApacheDrillStatus().main()
