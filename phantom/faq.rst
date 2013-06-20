===========================================
Nimbus Phantom Frequently Asked Questions
===========================================

.. contents::
    :local:


What is the Nimbus Phantom Service?
===================================

The Nimbus Phantom service is a hosted service that makes it easy to leverage
on-demand resources provided by infrastructure clouds. 
Phantom allows the user to easily deploy a set of virtual machines over
multiple private, community, and commercial clouds and then automatically grows
or shrinks this set based on policies defined by the user. The user can also
supplement resources in a local cluster with cloud resources. Phantom can then
be used to implement elastic services (growing and shrinking to demand) or
highly available services (where failed resources always get restarted).
Phantom itself has been
implemented as a highly available service.

Where can I work with Phantom?
==============================

Phantom is currently being released as a service deployed on `FutureGrid
<https://futuregrid.org/>`_ and is freely available to all comers via an
easy-to-use web interface.  Instructions on :doc:`how to get an account </webapp>` and a
:doc:`quickstart </webapp>` are available.

Another instantiation of Phantom is being operated by the `Ocean Observatory
Initiative project <http://www.oceanobservatories.org/>`_ whose infrastructure
is built on its capabilities; however this version is only available to users
within that project.

How can I use Phantom?
======================

Most users use Phantom to enhance a specific application, such as a job
scheduler, a workflow engine, a data transfer service, or a caching service.
For example, a job scheduler may want to increase the number of available
resources in proportion to the size of a job queue. 
In this case, a sensor agent monitors the length of the job queue overtime and
directs Phantom to add resources as needed; the added resources can be
supplementing a local cluster or other resources provisioned in the cloud.
The resources are added to the set available to the job
scheduler so that jobs can be run on them. When the length of the scheduler’s
queue goes below a certain threshold the resources are relinquished. One such
scenario was described in `Elastic Site: Using Clouds to Elastically Extend
Site Resources
<http://www.nimbusproject.org/files/elasticsite_ccgrid_2010.pdf>`_.

Similarly, a caching service, implemented as a set of workers that fetch data
from a remote location and cache them locally may want to acquire additional
resources  and start up additional workers based on the number of requests it
receives. In this case, a sensor agent monitors the number of requests to the
service and provisions additional resources as needed.

In both cases, additional resources can also be provided based on examining the
load and other system properties of used resources.

What clouds can I use with Phantom?
===================================

Phantom is currently in active use with AWS EC2, OpenStack, and Nimbus clouds.
However this is primarily an operational choice reflecting popularity among our
users; Phantom can be configured to run against any infrastructure cloud
supported by `Apache Libcloud <http://libcloud.apache.org/>`_.

What clients can I use with Phantom?
====================================

Phantom currently provides a :doc:`Web Application </webapp>` as well as a
REST API. We recommend Python and 
`requests <http://docs.python-requests.org/en/latest/>` for scripting.
Documentation on how to use the web application is available in our
:doc:`Quickstart Guide </webapp>` and the documentation on how to use scripting
in our :doc:`Advanced Documentation </advanced>`.

For developers, Phantom also provides an `AMQP <http://www.amqp.org/>`_
interface.

How can I extend Phantom?
=========================

Phantom can be extended by developing new *Decision Engines* – components that
determine the behavior of the service. Most users extend Phantom by developing
an *external Decision Engine*, i.e. an agent that monitors a desired behavior
(potentially based on data provided by Phantom), makes decisions on how to
evolve a group of VMs, and then calls out to Phantom to enforce those
decisions.

Decision Engines that capture frequently occurring behaviors, such as
regulating deployment over multiple cloud or scaling based on frequently
considered system factors such as load, are captured by *internal Decision
Engines*. Those are contributed to Phantom code directly and, like every open
source contribution, require review.


Is the software for Phantom available?
======================================

The software is freely available on
`GitHub <https://github.com/nimbusproject/>`_, licensed under the terms of the
`Apache License, Version 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`_
It is stored in several different repositories including:

* `Phantom Autoscale API <https://github.com/nimbusproject/Phantom>`_,
* `Web Application <https://github.com/nimbusproject/PhantomWebApp>`_,
* `PhantomSQL <https://github.com/nimbusproject/PhantomSQL>`_,
* `ceiclient <https://github.com/nimbusproject/ceiclient>`_,
* `epu <https://github.com/ooici/epu>`_

However, at this time Phantom is primarily available as a service and no formal
releases are being packaged and announced.

Where can I find out more about how to use Phantom?
===================================================

Our :doc:`Quickstart </webapp>` guide is a good place to start and our
:doc:`Advanced Documentation </advanced>` will take you further.

Where can I find out more about Phantom architecture?
=====================================================

The architecture has been described in `Infrastructure Outsourcing in
Multi-Cloud Environment
<http://www.nimbusproject.org/files/keahey_wcs_ocs_2012.pdf>`_. Our `other
publications <http://www.nimbusproject.org/papers/>`_ also describe the effect
of various policies on resource scaling in multi-cloud environment and explore
relevant techniques. 
