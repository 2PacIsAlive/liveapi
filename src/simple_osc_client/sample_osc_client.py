#!/usr/bin/python
"""
# Copyright (C) 2007 Nathan Ramella (nar@remix.net)
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# For questions regarding this module contact
# Nathan Ramella <nar@remix.net> or visit http://www.liveapi.org
"""
import sys

sys.path.append('..\_LiveAPICore')

import RemixNet

udpClient = RemixNet.UDPClient('localhost', 9000)
udpClient.open()

oscClient = RemixNet.OSCClient(udpClient)

# Send an echo request
oscClient.send('/remix/echo', 'echotest')

# Set the tempo to 80
oscClient.send('/live/tempo', 80)

# Play the first clip in the first track
oscClient.send('/live/play/clip', (0,0))

print 'done'
