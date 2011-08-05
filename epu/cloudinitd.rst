====================
What is cloudinit.d?
====================

This page is part of the EPU's conceptual walkthrough, it assumes you have read the `EPU overview page <index.html>`_.


Launch Plan
===========

cloudinit.d consumes a "launch plan" which is a description of services to run, broken out into bootlevels.  The tool automatically configures each service/VM (according to to the plan).  After launching, it can also be used to monitor each configured service/VM.

cloudinit.d is IaaS-agnostic. Even within a single launch plan, you can launch different VMs on different clouds.


Services/VMs
============

The EPU system is made of services that run in such VMs, you use a launch plan with cloudinit.d to bring them to life.  Then the EPU services bring up and monitor the services you want running (more on this later).  The EPU services can themselves live on just one base node if desired.

Each service/VM is launched/verified in the order necessary for dependencies to work out.  cloudinit.d will not proceed past each level until a verification has been run (the verification step is particular to each service; it's also optional).

Each level can contain any number of service/VM configurations, it could be just one or it could be 100. Like in the unix runlevel concept (cloudinit.d's namesake), if there is more than one thing configured in a level then you are stating that they can be started simultaneously -- as long as it's after all the things in previous runlevels.


Dependencies
============

Further, attributes can be provided from one level to the next. For example, the hostname of a dependency started in a previous level can be specified as a configuration input to a subsequent VM.

In the EPU system, this is used to bootstrap things like RabbitMQ and Cassandra and feed their coordinates into ION service configurations.


cloudinit.d & the EPU
=====================

Here is the most basic outline of the EPU system as launched by cloudinit.d (click the image to see a larger version):

.. TODO: image is too close to text

.. image:: images/cloudinitd+epu-thumb.png
   :target: _images/cloudinitd+epu.png


Next
====

You can find out more about cloudinit.d itself by reading the `cloudinit.d docs <../cloudinitd/index.html>`_, but in the EPU launch instructions you will learn what you need to know.

Moving along to the next section of the EPU conceptual walkthrough: `after bootstrap <afterboot.html>`_.

