.. _process-dispatcher-introduction:

===============================
Process Dispatcher Introduction
===============================

The Process Dispatcher is a system for managing processes on virtual machines. It takes process requests from the Stream Management Framework, and then requests virtual machines from the Phantom Resource Management Platform, and communicates with an agent on the virtual machine which runs those processes.

It is similar to systems like `HTCondor<http://research.cs.wisc.edu/htcondor/>`_ and `Torque PBS<http://www.adaptivecomputing.com/products/open-source/torque/>`_. The primary difference between these systems and the Process Dispatcher is their intention. The Process Dispatcher is intended to run service-like processes on a dynamic system of virtual machines, rather than running batch processes. `Cloud Scheduler<https://github.com/hep-gc/cloud-scheduler>`_ is similar to the combination of Process Dispatcher and Phantom, however as works with Condor to manage jobs, it is more suited to running thousands of batch jobs than individual services.

How it works
------------

The process dispatcher works as follows:

*Step 1*: The Stream Manager requests a Stream Agent process from the Process Dispatcher:

.. image:: images/pd_step1.png
   :width: 150px

*Step 2*: The Process Dispatcher requests a VM from Phantom to run the process:

.. image:: images/pd_step2.png
   :width: 150px

*Step 3*: Phantom Starts a VM and runs the eeagent on the VM:

.. image:: images/pd_step3.png
   :width: 150px

*Step 4*: The Process Dispatcher requests a Stream Agent process run on the eeagent:

.. image:: images/pd_step4.png
   :width: 300px

(PDA: Would an API listing be helpful here? or is a high level overview enough)
