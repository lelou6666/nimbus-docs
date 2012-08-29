===============
Nimbus Platform
===============

Infrastructure clouds created a revolution in the outsourcing of computational
resources: they enable users to provision resources customized to their needs,
including the right software stack and execution privileges on a pay-as-you-go
basis. But the ability to leverage this new outsourcing capability is still a
challenge to many: users need to find ways to allow the on-demand resources to
share security and configuration context, manage the deployment of potentially
diverse platform, ensure reliability and scalability in the environment, etc.

Nimbus Platform provides an integrated set of tools designed to overcome these
challenges. Our aim is to enable users to move to the cloud quickly and
effortlessly, automating and facilitating much of the process. We also aim to
provide a bridge allowing a user to overlay familiar concepts, such as virtual
clusters, onto the resources provisioned in the cloud.

The current Nimbus Platform tools are described below.

cloudinit.d
===========

cloudinit.d is a tool for launching, controlling, and monitoring cloud
applications. If the application is simple or complex, single cloud or
multi-cloud, VM based or bare metal, or any combination of the above,
cloudinit.d is designed to make the management and coordination of that
application easy. `Learn more <http://www.nimbusproject.org/doc/cloudinitd/>`_.

Phantom
=======

Phantom is a service that provides auto-scaling and high availability for
collections of resources deployed over multiple IaaS cloud providers allowing
users to develop scalable and reliable applications.
`Learn more <http://www.nimbusproject.org/doc/phantom/>`_.

Context Broker
==============

The Context Broker is a service that allows clients to coordinate large virtual
cluster launches automatically and repeatably.
`Learn more <http://www.nimbusproject.org/doc/ctxbroker/>`_.
