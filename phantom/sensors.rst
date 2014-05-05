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

Once you have Python installed, you can install it like so::

    # wget http://build.nimbusproject.org:8001/tcollector/master/tcollector-HEAD.tar.gz
    # tar xzvf tcollector-HEAD.tar.gz
    # mv tcollector /usr/local/tcollector

That's it! You can start tcollector like so to test it::

    # /usr/local/tcollector/tcollector.py --host nimbus-opentsdb.no-ip.info --port 4242

Now to make tcollector start on system start, you can use the provided startstop script. Install it like so::

    # cp /usr/local/tcollector/startstop /etc/init.d/tcollector

.. note::
    
    If you are running your VM on OpenStack clouds running OpenStack prior to Havana,
    there is `a bug <https://bugs.launchpad.net/nova/+bug/1096468>`_ in the EC2 interface
    which affects this script. We have an `alternative script available 
    <https://github.com/nimbusproject/tcollector/blob/master/startstop.india-openstack>`_,
    which works around the problem.

    Instead of the above command, use:

        # wget https://raw.githubusercontent.com/nimbusproject/tcollector/master/startstop.india-openstack
        # cp startstop.india-openstack /etc/init.d/tcollector

Open up the script and set the TSD_HOST variable to point to the Phantom
OpenTSDB installation::

    # vim /etc/init.d/tcollector

Line 5 should look like::

    TSD_HOST=nimbus-opentsdb.no-ip.info

You can confirm that you've set this right by running the following, and
verifying that the output is the same::

    # grep 'TSD_HOST=' /etc/init.d/tcollector
    TSD_HOST=nimbus-opentsdb.no-ip.info

You will now want to set this init script to start on boot. To do this on
Debian or Ubuntu based distros, you will want to use `update-rc.d
<http://manpages.ubuntu.com/manpages/precise/man8/update-rc.d.8.html>`_::

    # update-rc.d tcollector defaults

On Redhat based distros like CentOS and Scientific Linux, you will want to
use `chkconfig <http://www.centos.org/docs/5/html/Deployment_Guide-en-US/s1-services-chkconfig.html>`_::

    # /sbin/chkconfig --add tcollector

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

Domain Sensors
==============

If you would like to set up a sensor that is not associated with a particular
hostname, that is simple as well. You may want to do this if you would like to
scale based on some external metric, like say you had a system set up with 
Torque on a static headnode, and you set Phantom up to scale based on your 
queue length. 

Installing tcollector
---------------------

Installing tcollector to use as a domain sensor is simple, and very similar to
installing it on your VM image. 

tcollector requires that you have (at least) Python 2.6 installed on your VM image. This can generally be installed with your distribution's package manager, or built from source from `python.org <http://python.org/>`_.

Once you have Python installed, you can install it like so::

    # wget http://build.nimbusproject.org:8001/tcollector/master/tcollector-HEAD.tar.gz
    # tar xzvf tcollector-HEAD.tar.gz
    # mv tcollector /usr/local/tcollector

That's it! You can start tcollector like so to test it::

    # /usr/local/tcollector/tcollector.py --host nimbus-opentsdb.no-ip.info --port 4242

Now to make tcollector start on system start, you can use the provided startstop script. Install it like so::

    # cp /usr/local/tcollector/startstop /etc/init.d/tcollector

Open up the script and set the TSD_HOST variable to point to the Phantom
OpenTSDB installation::

    # vim /etc/init.d/tcollector

Line 5 should look like::

    TSD_HOST=nimbus-opentsdb.no-ip.info

You can confirm that you've set this right by running the following, and
verifying that the output is the same::

    # grep 'TSD_HOST=' /etc/init.d/tcollector
    TSD_HOST=nimbus-opentsdb.no-ip.info

You will now want to set this init script to start on boot. To do this on
Debian or Ubuntu based distros, you will want to use update-rc.d::

    # update-rc.d tcollector defaults
     Adding system startup for /etc/init.d/tcollector ...
       /etc/rc0.d/K20tcollector -> ../init.d/tcollector
       /etc/rc1.d/K20tcollector -> ../init.d/tcollector
       /etc/rc6.d/K20tcollector -> ../init.d/tcollector
       /etc/rc2.d/S20tcollector -> ../init.d/tcollector
       /etc/rc3.d/S20tcollector -> ../init.d/tcollector
       /etc/rc4.d/S20tcollector -> ../init.d/tcollector
       /etc/rc5.d/S20tcollector -> ../init.d/tcollector

On Redhat based distros like CentOS and Scientific Linux, you will want
to use chkconfig::

    # /sbin/chkconfig --add tcollector

Now save your image, and you're finished.


Configuring tcollector for your Domain
--------------------------------------

Now that you have tcollector installed, you can configure it to push metrics 
for your domain. To do this, open up the configuration as follows::

    # vim /usr/local/tcollector/collectors/etc/config.py

and set the USER and DOMAIN lines to your Phantom username and Domain, by
removing the leading '#' and setting the correct values. Check your values with::

    # egrep '^USER|^DOMAIN' /usr/local/tcollector/collectors/etc/config.py
    USER = "iamauser"
    DOMAIN = "iamadomain"

You will probably also want to remove the existing metrics, since they probably
won't be helpful to your domain. You can do this with::

   # rm /usr/local/tcollector/collectors/0/*

You can now place your custom domain collector into your tcollector install::

  # cp mycollector.py /usr/local/tcollector/collectors/0/

Using Domain Metrics with Phantom
---------------------------------

Use these metrics in the same way you use regular host metrics, but prefix the
name of the metric with "domain:" for example, with a metric named 
*my.domain.metric*, use "domain:my.domain.metric" when adding the sensor, the 
same way that is explained in the :doc:`webapp`.
