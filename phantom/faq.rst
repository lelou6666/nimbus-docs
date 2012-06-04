===========================================
Nimbus Autoscale Frequently Asked Questions
===========================================

.. contents::
    :local:


What is the Autoscale Service?
==============================

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
`epu <>`_, 
`REST API <https://github.com/nimbusproject/Phantom>`_,
`Web Application <https://github.com/nimbusproject/PhantomWebApp>`_,
`PhantomSQL <https://github.com/nimbusproject/PhantomSQL>`_,
`ceiclient <https://github.com/nimbusproject/ceiclient>`_,
`epu <https://github.com/ooici/epu>`_


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
available service.  Of course there are some practicle limits based
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

How can I get a FutureGrid account?
===================================

Can I automatically scale my VMs based on a policy?
===================================================

What are the planned future features?
=====================================

What is the REST API service?
=============================

What is the EPUM?
=================

What is the provisioner?
========================

What is the DTRS?
=================


