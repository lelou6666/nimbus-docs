===========================
Scripting with the REST API
===========================

Because the Nimbus autoscaling service is protocol compliant with
the AWS autoscaling service there are many clients and libraries
that can be used.  However, the only one tested thus far is
`boto <https://github.com/buzztroll/boto>`_.  On this page we will describe
some simple boto applications for interacting with the Nimbus
Auto Scale service.

Sample scripts
==============

The following sample programs can be used to aid in understanding.  For
all of the programs to work the user must first set three environment
variables::

    EC2_ACCESS_KEY=<your FutureGrid access key>
    EC2_SECRET_KEY=<your FutureGrid access secret>
    PHANTOM_URL=https://svc.uc.futuregrid.org:8445

All of these values can be found in your FutureGrid cloud-client
cloud.properties file.

* `Create a Launch Configuration <https://github.com/nimbusproject/Phantom/blob/master/sandbox/lc_create.py>`_.

* `Delete a Launch Configuration <https://github.com/nimbusproject/Phantom/blob/master/sandbox/lc_delete.py>`_.

* `List all Launch Configurations <https://github.com/nimbusproject/Phantom/blob/master/sandbox/lc_list.py>`_.

* `Create a Domain <https://github.com/nimbusproject/Phantom/blob/master/sandbox/asg_create.py>`_.

* `Delete a Domain <https://github.com/nimbusproject/Phantom/blob/master/sandbox/asg_delete.py>`_.

* `List all running domains <https://github.com/nimbusproject/Phantom/blob/master/sandbox/asg_list.py>`_.

* `Change the n-preserving value <https://github.com/nimbusproject/Phantom/blob/master/sandbox/asg_alter.py>`_.

Here is a sample session of using the above scripts.  In it we will create a 
launch configuration that has 2 sites.  We will then launch a domain that
spans those 2 sites.  First we create the launch configuration::

    $ python lc_create.py testlc1@hotel hello-cloud
    $ python lc_create.py testlc1@sierra hello-cloud
    $ python lc_list.py
    testlc1@hotel
    testlc1@sierra

Note that we had to call lc_create.py twice, once for each cloud.  We 
used the same name so that the two calls will be associated.  In 
the listing they appear as two separate launch configurations, and 
as far as the AWS protocol goes they are treated as two launch configurations.
However, in Phantom they will be treated as one. 

The next thing we do is create a domain using that launch configuration::

    $ python asg_create.py testDomain1 testlc1@hotel 3 hotel:1 sierra:2
    using LaunchConfiguration:testlc1@hotel
    $ python asg_list.py
    testDomain1
        testlc1 : 3
        Instances:
        ---------
            sierra : Healthy
            hotel : Healthy
            sierra : Healthy

The arguments to that program are as follows in order:

* the new domain name
* the launch configuration name
* the size of the domain
* a list of clouds and the maximum number of domains that will be on them. 
  This takes the following format <cloud name>:<max vms>

Notice the we used the launch configuration name *testlc1@hotel*.  We could 
have also used the name *testlc1@sierra* if we wanted to.  It just has to
match one of the AWS launch configuration names.  Phantom will internally
associate it with all the sites that have the name prefix of "testlc1".

Now we clean everything up::

    $ python asg_delete.py testDomain1
    deleting AutoScaleGroup<testDomain1>
    $ python lc_delete.py testlc1@hotel
    $ python lc_delete.py testlc1@sierra

