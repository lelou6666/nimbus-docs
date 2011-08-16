=====================
Nimbus Context Broker
=====================

What is the Context Broker?
===========================

The Context Broker is a service that allows clients to coordinate large virtual cluster launches automatically and repeatably.

It's used for deploying "one-click" virtual clusters that function right after launch as opposed to launching a set of "unconnected" virtual machines like most VM-on-demand services give you. It also provides a facility to personalize VMs (seed them with secrets, access policies, and just-in-time configurations). This requires that the VMs run a lightweight script at boot time called the Context Agent.

This is a user-oriented system that runs as an overlay on top of the normal VM-on-demand mechanics. It's been used on top of Nimbus clouds as well as with EC2 resources.
 

What is the standalone Context Broker?
======================================

The Context Broker is already included as a running service if you install Nimbus IaaS, so there is no need to follow any extra instructions if you are also interested in IaaS.  But you can install the Context Broker on its own if you would like to only use it with your VMs on other clouds and have a slimmer installation.

To move forward with only the standalone broker, see the `install guide <install.html>`_.


How does it work?
=================

For a detailed explanation, see the `cluster guide <http://www.nimbusproject.org/docs/current/clouds/clusters2.html#howdoes>`_.


Problems
========

If you are encountering a specific error, follow the instructions `here <http://www.nimbusproject.org/contact/#error>`_.  Common context broker errors are listed in the troubleshooting section listed there.
