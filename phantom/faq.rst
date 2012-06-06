===========================================
Nimbus Auto-scale Frequently Asked Questions
===========================================

.. contents::
    :local:


What is the Auto-scale Service?
==============================

The Auto-scaling service is software-as-a-service for the scientific community.
The goal of the service is to make using the cloud easier for the 
scientific applications.  Virtualization adds amazing elastic scaling
possibilities the scientific applications can leverage, however in the 
current state of the industry the users must be Virtualization experts
in order to do so.  This service provides an easy to use interface to the 
elasticity of the cloud.

What is Phantom?
================

Phantom was the original code name for this project.  It remains used 
by the development community in conversation and is thus referenced in
documentation as well.

How is the software licensed?
=============================

Nimbus code is licensed under the terms of the `Apache License, version 2 <http://www.apache.org/licenses/LICENSE-2.0>`_.

Where is the source code?
=========================

All of the source code can be found on 
`GitHub <https://github.com/nimbusproject/>`_.  
It is stored in several different repositories including:

* `REST API <https://github.com/nimbusproject/Phantom>`_,
* `Web Application <https://github.com/nimbusproject/PhantomWebApp>`_,
* `PhantomSQL <https://github.com/nimbusproject/PhantomSQL>`_,
* `ceiclient <https://github.com/nimbusproject/ceiclient>`_,
* `epu <https://github.com/ooici/epu>`_

Where is this service running?
==============================

The service is running on the University of Chicago FutureGrid resources.
The hardware is located at `Argonne National Lab <http://www.anl.gov>`_.
The vast majority of the services are run inside of VMs on the Nimbus 
cloud called "hotel".  This allows us to provide a highly available 
and scalable service.

How is this serviced released?
==============================

This application is currently being released as a service.  The 
software is freely available on github, but at this time no formal 
releases are being packed and announced.

Is this service highly available?
=================================

Much care and expertise went into designing a scalable and highly 
available service.  Of course there are some practical limits based
on our available hardware and maintenance schedules.

Can I use this service to scale any cloud?
==========================================

This service was designed to run against any cloud the speaks
the AWS EC2 query interface protocol.  This includes Nimbus, OpenStack,
AWS EC2, and Eucalyptus.  The service has been tested in scale against
Nimbus and EC2.  A project known as `the Ocean Observatories Initiative 
<http://www.oceanobservatories.org/>`_ uses it heavily against EC2.
However, the hosted version running on FutureGrid can only be used 
against the FutureGrid Nimbus clouds.  This is a operations choice,
not a software limitation.

Is there an easy to use web applications?
=========================================

Yes.  Please use it!  If can be found at: 

What is FutureGrid?
===================

FutureGrid is a community cloud which provides free services for qualifying
applications.  More information about FutureGrid can be found 
`here <http://www.futuregrid.org>`_.

How can I get a FutureGrid account?
===================================

You can apply for a `FutureGrid  <http://www.futuregrid.org>`_ account
`here <https://portal.futuregrid.org/user/register>`_.

Can I automatically scale my VMs based on a policy?
===================================================

This is definitely possible and is the ultimate goal of Phantom.  In
the 0.1 release of Phantom the user must run their own policy engine.
The user is responsible for having their own software running and monitoring
their workload.  When that workload is too heavy or too light that software
can tell phantom to make the needed adjustment.  In future releases we
plan to have software that will help the user create such policies.

What are the planned future features?
=====================================

In the near future we will add a set of common sensors that will make 
auto-scaling an application trivial.  We will also add automated 
VM contextualization.  We have many other useful features planned and you
can follow our progress on `github <https://github.com/nimbusproject/>`_.

What is the REST API service?
=============================

The REST service API is a AWS Auto-scaling Service clone.  It implements
the same protocol, and thus allows you to use the same clients, however
it does have some minor semantic differences.

What is the EPUM?
=================

The EPU Management Service is an internal component of the scaling service.
The EPUM is responsible for creating, monitoring, 
and destroying all of the Deployable Units under its control. This 
service evaluates sensor data (such as VM life cycle and health state) 
against policies, and regulates the population of a domain by deploying or 
terminating additional VMs.


What is the provisioner?
========================

The provisioner is an internal component of the scaling service that
communicates with compute clouds.
The task of the Provisioner is to deploy and contextualize VMs, terminate 
them as needed, and keep track of the Life cycle State

What is the DTRS?
=================

The Deployable Type Registry Service (DTRS) is an internal component 
of the scaling service that
stores information relating to a users launch configuration.
DTRS is a key/value store that 
maps DT identifiers into launchable data.  It contains a VM image name
(or identifier), a cloud instance type (like m1.small, m1.large), and
a keyname.


