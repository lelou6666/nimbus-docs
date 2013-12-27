==================================
Nimbus Stream Management Framework
==================================

The Stream Management Framework
-------------------------------

The Stream Management Framework is a system for managing streams of data, and transformation operations made to those streams. A transformation operation is a process that runs on a VM, and is handed stream data from the Stream framework, and its output is taken from the process and passed to an output stream

:ref:`stream-introduction`

The Process Dispatcher
----------------------

The Process Dispatcher is a system for managing processes on virtual machines. It takes process requests from the Stream Management Framework, and then requests virtual machines from the Phantom Resource Management Platform, and communicates with an agent on the virtual machine which runs those processes.

:ref:`process-dispatcher-introduction`

The Phantom Resource Management Platform
----------------------------------------

Phantom is a service that provides auto-scaling and high availability for collections of resources deployed over multiple IaaS cloud providers allowing users to develop scalable and reliable applications.

`Phantom Introduction <http://www.nimbusproject.org/doc/phantom/latest/>`_
