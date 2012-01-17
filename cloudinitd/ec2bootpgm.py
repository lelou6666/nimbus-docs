#!/usr/bin/env python

import sys
import os

cmd = "sudo sh -c 'env DEBIAN_FRONTEND=noninteractive apt-get -q -y install apache2'"
os.system(cmd)

f = open("hello.html", "w")
f.write("<html><body>Hello cloudinit.d!</body></html>")
f.close()

cmd = "sudo cp hello.html /var/www/"
os.system(cmd)

sys.exit(0)
