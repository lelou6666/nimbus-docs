=================================
Using Sensors with your VM Images
=================================

Introduction
============
`tcollector <http://opentsdb.net/tcollector.html>`_ is a simple program that
provides sensor monitoring information about your deployed virtual machines.
It works with the `OpenTSDB <http://opentsdb.net/>`_ Monitoring System to keep
track of the metrics of your Virtual Machines, which Phantom can use to scale
the VMs for your application. This guide explains how to install tcollector on
your VM image.

If you don't want to install tcollector on an image, and are only looking to
test Phantom's sensor capabilities, please try the hello-phantom.gz image
available on FutureGrid clouds. You may also base your application image on it.

Installation and Prerequisites
==============================

tcollector requires that you have (at least) Python 2.6 installed on your VM image. This can generally be installed with your distribution's package manager, or built from source from `python.org <http://python.org/>`_.

Once you have tcollecor installed, you can install it like so::

    # wget http://build.nimbusproject.org:8000/tcollector/master/tcollector-HEAD.tar.gz
    # tar xzvf tcollector-HEAD.tar.gz
    # mv tcollector /usr/local/tcollector

That's it! You can start tcollector like so to test it::

    # /usr/local/tcollector/tcollector.py --host nimbus-opentsdb.no-ip.org --port 4242

Now to make tcollector start on system start, you can use the provided startstop script. Install it like so::

    # cp /usr/local/tcollector/startstop /etc/init.d/tcollector

Open up the script and set the TSD_HOST variable to point to the Phantom
OpenTSDB installation::

    # vim /etc/init.d/tcollector

Line 5 should look like::

    TSD_HOST=nimbus-opentsdb.no-ip.org

You can confirm that you've set this right by running the following, and
verifying that the output is the same::

    # grep 'TSD_HOST=' /etc/init.d/tcollector
    TSD_HOST=nimbus-opentsdb.no-ip.org

Now save your image, and you're finished.

Custom Sensors
==============

Creating custom tcollector sensors is easy. To do this, you simply need to
create a script that periodically outputs your metric data. As an example::

    #!/usr/bin/python
    import sys
    import time
    COLLECTION_INTERVAL = 15  # seconds

    while True:
        ts = int(time.time())
        print "test.my.value %s 42" % ts
        sys.stdout.flush()
        time.sleep(COLLECTION_INTERVAL)

When this script is running on your VM, you will have the test.my.value metric
available.

If you would like to create your own sensors, check out the `tcollector documentation <http://opentsdb.net/tcollector.html>`_, and for inspiration, check out the `phantom sensors <https://github.com/nimbusproject/phantom-sensors>`_ that are included with the
tcollector tarball.
