===================
Example Launchplans
===================

A powerful feature of cloudinit.d is the ability to share launch plans.
Not only can a launch plan be created that describes a web application
but that launch plan can be distributed to others and used many times
over.  This page has example launch plans which boot well known applications.

Typically each launch plan will need a couple of environment variables
set before they can be used (mainly for security reasons) but otherwise
no customization should be needed.

* :ref:`WordPress <wpref>`
* :ref:`CloudFoundry <cfref>`

WordPress
=========

.. _wpref: 
.. image:: wordpress-logo-stacked-rgb.png
   :width: 250
   :height: 155

#. `Download <http://www.nimbusproject.org/downloads/wordpress.tar.gz>`_

   .. code-block:: none

        wget http://www.nimbusproject.org/downloads/wordpress.tar.gz
        tar -zxvf wordpress.tar.gz

#. Set the security information

   .. code-block:: none

    $ export CLOUDINITD_IAAS_ACCESS_KEY=<your EC2 access key>
    $ export CLOUDINITD_IAAS_SECRET_KEY=<your EC2 secret key>
    $ export CLOUDINITD_IAAS_SSHKEY=<the path to your ssh key>
    $ export CLOUDINITD_IAAS_SSHKEYNAME=<the name of your ssh key in EC2>

#. Boot it

   .. code-block:: none

    cloudinitd -v -v -v boot wordpress/top.conf

This launch plan will boot two VMs.  One that runs a MySQL server and 
the other runs an apache2 server with WordPress.  More details on this
launch plan can be found :doc:`here <wordpress>`.


Cloud Foundry
=============
.. _cfref:

.. image:: vmware_cloud_foundry.png
   :width: 256
   :height: 256

#. `Download <http://www.nimbusproject.org/downloads/cloudfoundry-multinode.tar.gz>`_

   .. code-block:: none

        wget http://www.nimbusproject.org/downloads/cloudfoundry-multinode.tar.gz
        tar -zxvf cloudfoundry.tar.gz

#. Set the security information

   .. code-block:: none

    $ export CLOUDINITD_IAAS_ACCESS_KEY=<your EC2 access key>
    $ export CLOUDINITD_IAAS_SECRET_KEY=<your EC2 secret key>
    $ export CLOUDINITD_IAAS_SSHKEY=<the path to your ssh key>
    $ export CLOUDINITD_IAAS_SSHKEYNAME=<the name of your ssh key in EC2>

#. Boot it

   .. code-block:: none

    cloudinitd -v -v -v boot cloudfoundry-multinode/main.conf

