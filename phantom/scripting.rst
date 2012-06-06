===========================
Scripting with the REST API
===========================

Because the Nimbus autoscaling service is protocol complaint with 
the AWS autocaling service there are many clients and libraries
that can be used.  However, the only one tested thus far is 
`boto <https://github.com/boto/boto>`_.  On this page we will describe 
some simple boto applications for interacting with the Nimbus
Auto Scale service.

Sample scripts
==============

The following sample programs can be used to aid in understanding.  For 
all of the programs to work the user must first set three environment
variables: EC2_ACCESS_KEY=<your FutureGrid access key>, 
EC2_SECRET_KEY=<your FutureGrid access secret>, 
PHANTOM_URL=https://svc.uc.futuregrid.org:8445.  All of these values 
can be found in your FutureGrid cloud-client cloud.properties file.

* ``Create a Launch Confiuration`` 
   `example <https://github.com/nimbusproject/Phantom/blob/master/sandbox/lc_create.py>`_.

* ``Delete a Launch Confiuration``
   `example <https://github.com/nimbusproject/Phantom/blob/master/sandbox/lc_delete.py>`_.

* ``List all Launch Configurations`` 
   `example <https://github.com/nimbusproject/Phantom/blob/master/sandbox/lc_list.py>`_.

* ``Create a Domain``
  `example <https://github.com/nimbusproject/Phantom/blob/master/sandbox/asg_create.py>`_.

* ``Delete a Domain``
  `example <https://github.com/nimbusproject/Phantom/blob/master/sandbox/asg_delete.py>`_.

* ``List all running domains``
  `example <https://github.com/nimbusproject/Phantom/blob/master/sandbox/asg_list.py>`_.

* ``Change the n-preserving value``
  `example <https://github.com/nimbusproject/Phantom/blob/master/sandbox/asg_alter.py>`_.



