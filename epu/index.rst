==================================
Nimbus Elastic Scaling System: EPU
==================================

Overview
========

The EPU system is used with IaaS systems to control services that:

- Do not disappear because any failures are compensated with replacements.
- Can be configured to be elastic: responding to monitoring signals with adjustments of the amount of instances a service is made up of.

If you have a service that cannot handle instances being added and dropped on the fly (many services have static node-number configurations), you can still take advantage of the automatic launch, monitoring, and failure replacement capabilities.

The EPU system is cloud-agnostic and is devised with most types of service or worker instance in mind:

- Workers drawing from a central queue
- Launching/monitoring the queue itself
- Storage systems
- Batch job queue systems
- Application containers
- Webservers
- Load balancers
- Databases
- PaaS systems


Easy to Bootstrap
=================

Both *cloudinit.d* and *epumgmt* are Python tools you can install in a few short commands.  One of the beauties of cloudinit.d is that the EPU system launch plan is a repeatable blueprint and many samples have been pre-authored and tested.

Once you have these two programs installed and a launch plan in hand, the rest is driven by automatic VM instance creation and configuration recipes.


Main Components
===============

The EPU system is running in virtual machines itself (one or many) and is made up of the following software components:

- The *provisioner* service is used to launch IaaS instances and make sure they contextualize as desired.  It is also used for ongoing monitoring and termination.
- Each service being "EPU-ified" has a dedicated *EPU controller* service instance that is responsible for making sure that the service has the capacity desired for the situation at hand (according to policy). It is also what keeps track of worker heartbeats, error, and other sensor information.
- The *deployable type registry* is where you define what exactly to launch on each cloud for each EPU type (and there are flexible variable substitutions possible for each launch)
- If you are using a queue-based work model, there is typically an agent present at the queue for monitoring.
- For tighter integration and higher reliability, each worker instance may also have an agent installed on it (for heartbeat and error reporting).

Something needs to bootstrap and monitor the base system itself from a pre-existing computer and that is *cloudinit.d*. This tool is not specific to the EPU architecture but it is integral to launching and monitoring it. It takes a "launch plan" as input, this is made up of bootlevel-style descriptions of what needs to run.

Once launched, the *epumgmt* tool can be used to inspect what is happening in the EPU system. Since cloudinit.d is not aware of VMs that are launched by the provisioner service, epumgmt is also what should be used to cleanly tear a running EPU system down.

The EPU components have their own dependencies, mainly RabbitMQ and Cassandra.  These are themselves launched as part of most launch plans but you can also reference pre-existing instances of them if you prefer.


Next steps
==========

Before jumping right in and launching samples (which we provide with step by step instructions), it will probably help to dig a little deeper and peruse some diagrams.

So first there is a conceptual walkthrough:

- `What is cloudinit.d? <cloudinitd.html>`_
- `After bootstrap <afterboot.html>`_


And then the quickstart:




