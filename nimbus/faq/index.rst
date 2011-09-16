=================================
Nimbus Frequently Asked Questions
=================================

.. contents::
    :local:

*******
General
*******

What is Nimbus?
===============

Nimbus is an open source project focused on cloud computing, it is built around three goals targeting three different communities:

* Enable resource owners to provide their resources as an infrastructure cloud

* Enable cloud users to access infrastructure cloud resources more easily

* Enable scientists and developers to extend and experiment with both sets of capabilities.

The first goal is realized by the Nimbus Infrastructure (the Workspace Service and Cumulus components providing a compute and storage cloud, respectively), the second by the Nimbus Platform (e.g., the Context Broker and cloudinit.d tools), and the third by strongly supporting open source development practices via modular, extensible code and engagement with open source developers.

The Nimbus project has been created by an international collaboration of open source contributors and institutions.  For more information, see the `Contributors </about/people>`_ page.


What is Nimbus Platform?
========================

Nimbus Platform is an integrated set of open source tools that allow users to easily leverage "Infrastructure-as-a-Service" (IaaS) cloud computing systems. This includes application instantiation, configuration, monitoring, and repair. For more information on cloudinit.d and Context Broker, start below with the `Nimbus Platform FAQ section <#platform>`_, in particular `What is cloudinit.d?`_ and `What is the Context Broker?`_


What is Nimbus Infrastructure?
==============================

Nimbus Infrastructure is a set of open source tools that together provide             an "Infrastructure-as-a-Service" (IaaS) cloud computing solution.  Our mission is to evolve the infrastructure with emphasis on the needs of science, but many non-scientific use cases are supported as well.

Nimbus Infrastructure allows a client to lease remote resources by deploying virtual machines (VMs) on those resources and configuring them to represent an environment desired by the user.

For more information, start below with the `Nimbus Infrastructure FAQ section <#infrastructure>`_.


How is the software licensed?
=============================

Nimbus code is licensed under the terms of the `Apache License, version 2 <http://www.apache.org/licenses/LICENSE-2.0>`_.


Where is the source code?
=========================

Nimbus code can all be found on `GitHub <https://github.com/nimbusproject/>`_ which allows us to work in a distributed fashion and easily work with casual contributors (using GitHub's "pull request" feature).


********
Platform
********

For overview information about *Nimbus Platform*, see the questions above:

* `What is Nimbus?`_
* `What is Nimbus Platform?`_


Can Nimbus Platform work on clouds other than Nimbus IaaS?
===========================================================

Yes, the tools work with multiple IaaS systems.  The Context Broker works with AWS and Nimbus IaaS. Because cloudinit.d uses the boto and libcloud libraries, there are many IaaS systems that it can work with.  Cloudinit.d has been tested against AWS, Nimbus IaaS, Eucalyptus, and OpenStack.  The `boto <http://code.google.com/p/boto/>`_ tool can work with many other EC2 protocol-compliant systems.  And `libcloud <http://libcloud.apache.org>`_ can be used with `many other IaaS systems <http://libcloud.apache.org/supported_providers.html>`_.


How is Nimbus Platform different than "PaaS"?
=============================================

Nimbus Platform is not a "code and run" platform like a typical "Platform-as-a-Service" (PaaS).  It is a collection of tools that run above the IaaS layer that make it easier to instantiate, configure, monitor, repair, and scale applications running on IaaS.  A PaaS system might itself be built out of such tools.


What benefits does Nimbus Platform have over using IaaS with my own scripts?
============================================================================

Nimbus Platform tools provide functionality well beyond homemade scripts, they give you a structure and APIs for launching, configuring, and monitoring your applications.  They are well tested and proven (cloudinit.d has 80+% code coverage, for example) and they are portable across IaaS clouds.  Using these tools you also have the ability to take advantage of other people's work by reusing launch plans, images, and contextualization recipes.


What is cloudinit.d?
====================

cloudinit.d is a tool for launching, configuring, monitoring, and repairing a set of interdependent virtual machines in an IaaS cloud or over a set of IaaS clouds.  A single launch can consist of many VMs and can span multiple IaaS providers, including offerings from commercial and academic space.

For a full introduction see the `cloudinit.d docs <http://www.nimbusproject.org/doc/cloudinitd/latest/>`_.


What is the Context Broker?
===========================

The Context Broker is used to deploy "one-click" virtual clusters that function right after launch as opposed to launching a set of "unconnected" virtual machines like most VM-on-demand services give you. This requires that the VMs run a lightweight script at boot time called the `Context Agent <#what-is-the-context-agent>`_.

This is a user-oriented system that runs as an "overlay" on top of the normal VM-on-demand mechanics.  It's been used on top of Nimbus clouds as well as with EC2 resources.

See the `Context Broker docs <http://www.nimbusproject.org/doc/ctxbroker/latest/>`_.


What is the Context Agent?
==========================

A lightweight agent on each VM -- its only dependencies are Python and the ubiquitous curl program -- securely contacts the context broker using a secret key.  This key was created on the fly and seeded inside the instance. This agent gets information concerning the cluster from the context broker and then causes last minute changes inside the image to adapt to the environment.


Is Nimbus Platform hard to install?
===================================

cloudinit.d could not be any simpler to install, you can use the Python *easy_install* tool.  Using one of the sample launch plans, all you then need to do is configure your IaaS credentials.

The Context Broker requires that you install and configure a service container (using a provided install script that only requires the presence of Java) and make the service open to the networks where your IaaS based VMs will run.  You then need to install the context agent on any VM that will be used.


What is the difference between cloudinit.d and the Context Broker?
==================================================================

Context Broker is a configuration "pull" model and cloudinit.d is a "push" model.  cloudinit.d will start and monitor the IaaS instances for you and works with many more IaaS clouds, the context broker has none of this functionality.  Also, cloudinit.d can be used with images that have no pre-installed agent.

cloudinit.d is generally the better choice unless you are dealing with a very large number of nodes or contextualizing VM instances more programatically (as we do in the upcoming elastic scaling tools).


Can Nimbus Platform use multiple clouds at the same time?
=========================================================

cloudinit.d is built from the ground up to handle this situation, you can author launch plans that simultaneously target specific services at different clouds, AWS regions, etc.

If you launch vms on multiple clouds using independent tools, the Context Broker can be used in a limited way, it was not originally geared for this.

For more about multiple cloud support, see the question above: `Can Nimbus Platform work on clouds other than Nimbus IaaS?`_


Can Chef be used with Nimbus Platform tools?
============================================

Chef can be used in conjunction with cloudinit.d and the Context Broker as the "last mile" configuration mechanism: people use chef-solo extensively with both.  See the cloudinit.d example launch plans in particular for how to get started.


**************
Infrastructure
**************

For overview information about *Nimbus Infrastructure*, see the questions above:

* `What is Nimbus?`_
* `What is Nimbus Infrastructure?`_


What is the main way to deploy Nimbus Infrastructure?
=====================================================

Options aren't always a good thing, especially to start with.  The main way to deploy Nimbus is the cloud configuration.  This involves hosting a site manager service and creating an image repository (see the `Zero To Cloud guide </docs/current/admin/z2c/>`_ for details).  You direct your new users to use the `cloud client </docs/current/clouds/cloudquickstart.html>`_ which gets them up and running in just a few minutes.

*Overview of the cloud configuration:*

.. image:: img/cloud-overview.png
   :width: 600px


Is Nimbus Infrastructure hard to install?
=========================================

Nimbus itself is not hard to install, it has a script driven install that asks you two questions.

Nimbus requires that some dependencies are installed first.  On the service node: Java, Python, and bash.  On the hypervisor nodes: Python, bash, ebtables, libvirt and KVM or Xen.

All of these things are installable via the package management system of all the popular Linux distributions.

See the `Zero To Cloud guide </docs/current/admin/z2c/>`_ for details including detailed `prerequisite information </docs/current/admin/z2c/service-dependencies.html>`_


What are the main Nimbus Infrastructure components?
===================================================

* The *Workspace Service* site manager - `What is the Workspace Service?`_

* A *WSRF* based remote protocol implementation - `What is the WSRF frontend?`_

* An *EC2* based remote protocol implementation of their SOAP and Query APIs (partial) - `What is the EC2 frontend?`_

* *Cumulus* is an open source implementation of the Amazon S3 REST API.  It is used as the Nimbus repository solution and can also be installed standalone - `What is Cumulus?`_

* The *RM API* bridge between remote protocols/security and specific site manager implementations - `What is the RM API?`_

* The *cloud client* aims to get users up and running in minutes with instance launches and one-click clusters - `What is the cloud client?`_

* The *reference client* exposes the entire feature set in the WSRF protocol as a commandline client (with underlying Java client library). For advanced uses, scripting, portal integration, etc. - `What is the reference client?`_

* The *Workspace Pilot* allows you to integrate VMs with resources already configured to manage jobs (i.e., already using a batch scheduler like PBS) - `What is the Workspace Pilot?`_

* The *workspace-control* agent implements VMM and network specific tasks on each hypervisor - `What is workspace-control?`_

* The *metadata server* allows VMs to query for information about themselves - `What is the metadata server?`_

The components are lightweight and self-contained so that they can be selected and composed in a variety of ways.  For example, using the workspace service with the pilot will enable a different cluster integration strategy.  You can mix and match protocol implementations with the "pure Java" resource management module.

Writing new components should be a matter of "dropping" them in.  As explained in `What is the RM API?`_", the Java side of things is particularly LEGO&#0174; like.  As of Nimbus 2.3 workspace-control (the VMM component) is modularized with around 10 plugin points.  And we are working towards modularizing even more and providing better implementations for various components.


What is the Workspace Service?
==============================

The Workspace service is a standalone site VM manager that different remote protocol frontends can invoke.

The current supported protocols are Web Services based or HTTP based.  They all run in either an `Apache Axis <http://ws.apache.org/axis/>`_ based Java container or `Apache CXF <http://cxf.apache.org/>`_.  But there is only a certain level of necessity:

* There is nothing specific to web services based remote protocols in the workspace service implementation, the messaging system just needs to be able to speak to Java based libraries.

* Workspace service dependencies have nothing to do with what container it is running in, they are normal Java application dependencies like `Spring <http://www.springframework.org/>`_, `ehcache <http://ehcache.sourceforge.net/>`_, `backport-util-concurrent <http://backport-jsr166.sourceforge.net>`_, and JDBC (currently using the embedded `Derby <http://db.apache.org/derby/>`_ database).


What is the WSRF frontend?
==========================

This is the protocol implementation in longstanding use by previous workspace services and clients including the popular cloud-client.


What is the EC2 frontend?
=========================

This is an implementation of two of the Amazon `Elastic Compute Cloud <http://aws.amazon.com/ec2>`_ (EC2) interfaces that allow you to use clients developed for the real EC2 system against Nimbus based clouds.

There is support for both EC2 interfaces: SOAP and Query.

See `What EC2 operations are supported?`_


What EC2 operations are supported?
==================================

Nimbus Infrastructure provides a partial protocol implementation of EC2's WSDL (namespace *http://ec2.amazonaws.com/doc/2009-08-15/*, a previous version supported *2008-05-05*) and the Query API complement to that WSDL. The operations behind these EC2 commandline clients are currently provided:

* *ec2-describe-images* - See what images in your personal cloud directory you can run.

* *ec2-run-instances* - Run images that are in your personal cloud directory.

* *ec2-describe-instances* - Report on currently running instances.

* *ec2-terminate-instances* - Destroy currently running instances.

* *ec2-reboot-instances* - Reboot currently running instances.

* *ec2-add-keypair* - Add personal SSH public key that can be installed for root SSH logins

* *ec2-delete-keypair* - Delete keypair mapping.


What is the metadata server?
============================

The metadata server responds to HTTP queries from VMs, using the same path name as the `EC2 metadata server <http://docs.amazonwebservices.com/AWSEC2/latest/DeveloperGuide/index.html?AESDG-chapter-instancedata.html>`_.

The URL for this is obtained by looking at '*/var/nimbus-metadata-server-url*' on the VM, which is an optional customization task injected by the Nimbus service on your behalf (we are considering trying to simulate Amazon's hardcoded IP address "169.254.169.254" on any subnet).

Like on EC2, its responses are based on the source IP address from the TCP packet, giving the information specific to each VM instance.  This also means there is an assumption that the immediately local network is non-spoofable.  Administrators, you should also put in place a firewall rule that restricts this port to the VMs only, just in case.

The metadata server is disabled by default, consult your administrator (or try a query from inside your VM).

Administrators, see "services/etc/nimbus/workspace-service/metadata.conf" for the details.


What metadata server fields are supported?
==========================================

(See `What is the metadata server?`_)

Nimbus provides a partial implementation of EC2's version of the metadata server (`their full field listing <href="http://docs.amazonwebservices.com/AWSEC2/latest/DeveloperGuide/index.html?instancedata-data-categories.html>`_).

These fields are currently supported:

* *user-data* - "opaque" information injected by the client at launch time

* *meta-data/ami-id* - the ami-id assigned to this image.  This is simulated by the EC2 protocols in Nimbus, the "definitive" piece of information for a launch is really the filename in the repository, there is not AMI registry like on EC2.

* *meta-data/ami-launch-index* - if this VM instance was launched as part of a group (cluster), it might have a launch index other than zero.  This differentiates it from other homogenous nodes in the launch.

* *meta-data/local-hostname* - the 'private' hostname of this VM [1]

* *meta-data/local-ipv4* - the 'private' IP of this VM [1]

* *meta-data/public-ipv4* - the 'public' hostname of this VM [1]

* *meta-data/public-ipv4* - the 'public' IP of this VM [1]

[1] - What 'public' and 'private' mean in this context is up to an administrator configuration.  The VM also may or may not have two NICs on it, the values of these fields might be equal or not.


What is the cloud client?
=========================

The cloud client aims to get users up and running in minutes with instance launches and one-click clusters, even from laptops, NATs, etc.  See the cloud client `quickstart </docs/current/clouds/cloudquickstart.html>`_ and `cluster quickstart </docs/current/clouds/clusters.html>`_ to see what it can do.


What is the reference client?
=============================

The reference client exposes all features of the <a href="#wsrf-frontend">WSRF frontend</a> as a commandline client.  It is relatively complex to use and thus typically wrapped by task-specific scripts.

Internally, it's implemented around a base Java client API suitable for portal integration or any programmatic usage.  Docs on this API are forthcoming but if you are interested check out the *org.globus.workspace.client_core* Java package in the client source tree (contains Javadoc comments and also consult example usages in the *org.globus.workspace.client.modes* package).


What is the Workspace Pilot?
============================

The pilot is a program the service will submit to a local site resource manager (LRM) in order to obtain time on the VMM nodes. When not allocated to the workspace service, these nodes will be used for jobs as normal (the jobs run in normal system accounts in Xen domain 0 with no guest VMs running).

Several extra safeguards have been added to make sure the node is returned from VM hosting mode at the proper time, including support for:

* The workspace service being down or malfunctioning

* LRM preemption (including deliberate LRM job cancellation)

* Node reboot/shutdown

Also included is a one-command "kill 9" facility for administrators as a "worst case scenario" contingency.

Using the pilot is optional. By default the service does not operate with it, the service instead directly manages the nodes it is configured to manage.


What is the RM API?
===================

Most things having to do with the Java server side components are very flexible, featuring an extensibility system that allows for customization and replacement at runtime of various behaviors. By employing the `Spring <http://www.springframework.org/>`_ framework's "Dependency Injection" system, the Java components are very modular.

One of the very strong internal interfaces here is the site resource management module which allows the remote security and protocol implementations and semantics to be separate from one consistent set of management operations.  The implementing module governs how and when callers get VMs, it assigns resources to use, and takes them away at the appropriate times, etc.


What is workspace-control?
==========================

Program installed on each VMM node used to (1) to start, stop and pause VMs, (2) implement VM image reconstruction and management, (3) securely connect the VMs to the network, and (4) to deliver contextualization information (see Context Broker).

Currently, the workspace control tools work with Xen and KVM.

Implemented in Python in order to be portable and easy to install. Requires libvirt, sudo, ebtables, and a DHCP server library.


What is Nimbus Web?
===================

Nimbus Web is the evolving web interface for Nimbus. Its aim is to provide administrative and user functions in a friendly interface. 

Nimbus Web is centered around a Python Django web application that is intended to be deployable completely separate from the Nimbus service. Instructions for configuring and starting the application are in `this section </docs/current/admin/reference.html#nimbusweb-config">`_ of the `administrator guide </docs/current/admin/index.html>`_.

Existing features:

* User X509 certificate management and distribution

* Query interface authentication token management

* Cloud configuration functionality


What is Cumulus?
================

Cumulus is an open source implementation of the S3 REST API.  Some features such as versioning and COPY are not yet implemented, but some additional features are added, such as file system usage quotas.


What clients can I use with Cumulus?
====================================

Cumulus is compliant with the S3 REST network API, therefore clients that work against the S3 REST API should work with Cumulus.  Some of the more popular ones are boto and s3cmd.  The Nimbus cloud client uses the Jets3t library to interact with Cumulus.


How are Nimbus IaaS and Cumulus related?
========================================

Cumulus is the front end to the Nimbus IaaS VM image repository.  In order to boot an image on a given Nimbus IaaS cloud, that image must first be put into that same cloud's Cumulus repository (advanced use cases can bypass this).


Can Cumulus be installed without Nimbus IaaS?
=============================================

Yes.  Cumulus does not rely on any higher level libraries and thus users who wish to install it as a stand alone front end to their storage system may do so.


Can Nimbus IaaS be installed without Cumulus?
=============================================

No.  Nimbus version 2.5 and higher is packaged with Cumulus and so Nimbus IaaS is intimately aware of Cumulus.  Nimbus IaaS must be installed with the version of Cumulus with which it is packaged.


Does the Nimbus IaaS system directly use Cumulus for image propagation?
=======================================================================

No.  While Cumulus is the primary interface for transfer images in and out of the cloud, it is not the mechanism by which images are propagated from the repository to the virtual machine monitors. Propagation is done in a variety of different ways, many of which we are still developing and researching in order to find the best solution for scientific users.


How reliable is Cumulus?
========================

The reliability of Cumulus depends entirely on the storage system that is backing it. In order to achieve S3 levels of reliability you need S3 levels of hardware investment but with our system even small providers can still be S3 protocol compliant while making an independent choice on cost/reliability.


What type of storage system backs the Cumulus repository?
=========================================================

In the first release of Cumulus we are only providing a posix filesystem backend storage system.  However this is a very powerful plugin.  It can be used against a variety of storage systems including PVFS, GFS, and HDFS (under a FUSE module).  We have prototyped HDFS and BlobSeer plugins and we will be releasing them soon.


What is LANTorrent?
===================

LANTorrent is a file distribution protocol integrated into the Nimbus IaaS toolkit.  It works as a means to multi-cast virtual machine images to many backend nodes.  The protocol is optimized for propagating virtual machine images (typically large files) from a central repository across a LAN to many virtual machine monitor nodes.


How do I enable LANTorrent?
===========================

See the document `here </docs/current/admin/reference.html#lantorrent>`_.


I am seeing boot errors from 'mount' when I try to launch an image I created
============================================================================

If when launching a VM image that you create from cloud client you see 
something like::
    
    OK: /opt/nimbus/var/workspace-control/tmp/5afba46b-a365-4565-b222

     - target OK: /root/.ssh/authorized_keys

     Altering image (dryrun = false):

     command = /bin/mount -o loop,noexec,nosuid,nodev,noatime,sync
     /opt/nimbus/var/workspace-control/secureimages/wrksp-XXXX/tmpXsw7ZQRepo__VMS__XXXXXXXXXXXXXXXXX
     /opt/nimbus/var/workspace-control/mnt/wrksp-XXXX

     mount: you must specify the filesystem type

     Exiting with error code: 3

     Workspace "vm-XXX" did NOT reach target state "Running"

You may need to make sure that your VM image has the directory: /root/.ssh 
created.





























