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
  configuration.  

  On Nimbus Phantom you must use the following naming convention:
  <launch configuration name>@<target cloud name>.  The
  launch configuration name can be anything the user wishes, but it must be
  unique.  The cloud name must be one of the site names which you have 
  configured.  The current options are:
  1) hotel, 2) sierra, 3) foxtrot, 4) alamo, 5) ec2 (if you have set it up).

  When setting up a Launch configuration you can add many sites to a 
  single launch configuration name.  By doing this you can take advantage 
  of the multi-cloud overflow capabilities which are unique to Phantom.

  For example, if you wish to have a launch configuration named *mylaunch*
  that will later 
  allow you to launch 10 VMs such that 8 are on FutureGrid's hotel and
  2 are on EC2, you would need to call CreateLaunchConfiguration twice,
  first with mylaunch@hotel and next with mylaunch@ec2.

  The REST protocol details
  can be found `here <http://docs.amazonwebservices.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html>`_.

* ``DeleteLaunchConfiguration``.  This simply deletes a launch
  configuration that the user previously created with a call to
  CreateLaunchConfiguration.  You must use the 
  <launch configuration name>@<target cloud name> name here.
  The REST protocol details
  can be found `here <http://docs.amazonwebservices.com/AutoScaling/latest/APIReference/API_DeleteLaunchConfiguration.html>`_.

* ``DescribeLaunchConfigurations``.  List all of the launch configurations
  that the user previously created with calls to CreateLaunchConfiguration.
  You must use the
  <launch configuration name>@<target cloud name> name here.
  The REST protocol details
  can be found `here <http://docs.amazonwebservices.com/AutoScaling/latest/APIReference/API_DescribeLaunchConfigurations.html>`_.

* ``CreateAutoScalingGroup``.  This API function will start running a group
  of VMs described by the provided 'Launch Configuration'.

  A major difference between Phantom and EC2 is that in this call you must 
  specify some Tags that control how your autoscale group will interact
  between clouds.  The following 3 tags are needed:

    * key: PHANTOM_DEFINTION, value: error_overflow_n_preserving
      In this version of Phantom that is the only accepted value

    * key: clouds, value: a comma separated ordered list of 
      the following format:
      
      <cloud name>:<max VMs for that cloud>
      
      each cloud name must be in the LaunchConfiguration also given to 
      this API call.  The max VM value tells phantom to not run more 
      VMs than that number of the cloud.  A value of -1 means infinity.

   * key: n_preserve, value: an integer specifying the maximum number of 
     VMs to schedule across all the clouds.

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

For every cloud on which you want your domain to run you must call 
`Create Launch Configuration <http://docs.amazonwebservices.com/AutoScaling/latest/GettingStartedGuide/CreateASGroup.html#create-launch-config>`_
Pick a launch configuration name and append "@<sitename>" to it.
Then that name will be used to manage what each site will run via 
the Create Launch Configuration REST API call.

Once a launch configuration is created, the user will launch an
"Auto Scale Group".  To do this the user must pick three things:

* The total number of VMs that will be in this autoscale group (this
  number can be adjusted later).  The set of VMs may be across many
  clouds.  This value is called the *desired size*.

* The launch configuration to be used with this domain.

* The set of clouds on which the VMs will be run.  Each cloud must be in
  the associated launch configuration.  The list of clouds needs to be 
  ordered.  A maximum number of VMs can be associated with each cloud, a
  value of negative one means infinity.

When scheduling scheduling VMs phantom will try to achieve the *desired size*.
It will start with the first cloud and launch VMs until it hits the limit
for that cloud or until it starts running into errors (typically due
to capacity limits on that cloud).  At that point it will move to the 
next cloud.

During the life-cycle of the user's application, they may decide to change the
number of VMs they have.  They can do this with a call to 'SetDesiredCapacity'.

When the user's application is complete, a call to 'DeleteAutoScalingGroup'
will terminate all the associated running VMs.
