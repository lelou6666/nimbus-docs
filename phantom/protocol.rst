=========================
Nimbus Phantom protocol
=========================

The Nimbus Phantom service implements a subset of the
`AWS Auto Scaling service <http://aws.amazon.com/autoscaling/>`_.
It is a REST API that allows users to interact with a service which
will monitor the health of VMs and preserve N VMs at one time on
various different clouds.

REST API
========

The AWS protocol on which the Nimbus Phantom service is based is
well documented
`here <http://docs.amazonwebservices.com/AutoScaling/latest/APIReference/>`_.
Understanding how the AWS service works is not necessary to understand
the Nimbus service; however, since the two services are wire protocol
compatible, it is helpful to understand the subset of commands
which have been implemented by the Nimbus Phantom service:


* ``CreateLaunchConfiguration``. This API call allows a user to
  associate a VM image with an instance type (the number of CPUs,
  amount of memory, and network configuration) and a security
  key.  It describes the details of every VM instance
  that will be launched in a group.  An important difference between
  the Nimbus system and the AWS protocol is the name given to a launch
  configuration.  On Nimbus Phantom you must use the following naming convention:
  <unique user selected name>@<target cloud name>.  The
  user selected name can be anything the user wishes, but it must be
  unique.  The cloud name must be one of the Nimbus Futuregrid clouds:
  1) hotel, 2) sierra, 3) foxtrot, 4) alamo.
  The REST protocol details
  can be found `here <http://docs.amazonwebservices.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html>`_.

* ``DeleteLaunchConfiguration``.  This simply deletes a launch
  configuration that the user previously created with a call to
  CreateLaunchConfiguration.
  The REST protocol details
  can be found `here <http://docs.amazonwebservices.com/AutoScaling/latest/APIReference/API_DeleteLaunchConfiguration.html>`_.

* ``DescribeLaunchConfigurations``.  List all of the launch configurations
  that the user previously created with calls to CreateLaunchConfiguration.
  The REST protocol details
  can be found `here <http://docs.amazonwebservices.com/AutoScaling/latest/APIReference/API_DescribeLaunchConfigurations.html>`_.

* ``CreateAutoScalingGroup``.  This API function will start running a group
  of VMs described by the provided 'Launch Configuration'.
  The REST protocol details
  can be found `here <http://docs.amazonwebservices.com/AutoScaling/latest/APIReference/API_CreateAutoScalingGroup.html>`_.

* ``DeleteAutoScalingGroup``.   This API call will stop a running auto scale
  group.
  The REST protocol details
  can be found `here <http://docs.amazonwebservices.com/AutoScaling/latest/APIReference/API_DeleteAutoScalingGroup.html>`_.

* ``DescribeAutoScalingGroups``  This API call lists all of the calling
  users currently running autoscaling groups.
  The REST protocol details
  can be found `here <http://docs.amazonwebservices.com/AutoScaling/latest/APIReference/API_DescribeAutoScalingGroups.html>`_.

* ``SetDesiredCapacity``.  This API call sets the number of VMs currently
  running in a given Auto Scaling Group.  The user is free to adjust this.
  The REST protocol details
  can be found `here <http://docs.amazonwebservices.com/AutoScaling/latest/APIReference/API_SetDesiredCapacity.html>`_.


Typical Flow
============

Here we will describe a typical user execution flow.  The first thing
a user will do is create a VM image.  This task is outside of the scope
of this document and we assume that the reader is familiar with this.
Once the user has selected the VM image they wish to use, they will
pick an `instance type <http://aws.amazon.com/ec2/instance-types/>`_.
The instance type describes the hardware in which the VM image
will run.  The last thing the user must pick is a ssh key to use.
The ssh key should already be associated with the cloud (or clouds)
on which the user will run their Auto Scale Group.  The process of
associating a ssh public key with a cloud is described `here <http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/generating-a-keypair.html>`_.

When these three items are selected the user can create a Launch
Configuration (a single reference to the tuple of the above described
values.  The AWS concept of `Launch
Configuration <http://docs.amazonwebservices.com/AutoScaling/latest/GettingStartedGuide/CreateASGroup.html#create-launch-config>`_ is similar and may
be helpful to understand.  Launch Configurations can be stored for
many runs and reused.

Once a launch configuration is created, the user will launch an
"Auto Scale Group".  To do this the user picks a target cloud, and
a target number of VMs to preserve.  Once the Auto Scale Group is
created the service will make sure that the desired number of VMs will
be running at all times.  If a VM unexpectedly dies, the service will
start a new one in its place.

During the life-cycle of the user's application, they may decide to change the
number of VMs they have.  They can do this with a call to 'SetDesiredCapacity'.

When the user's application is complete, a call to 'DeleteAutoScalingGroup'
will terminate all the associated running VMs.
