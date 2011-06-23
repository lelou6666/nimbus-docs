==========
Installing
==========

cloudinit.d is registered on pypi and can thus be installed with 
easy_install.  If you have python 2.5 or greater installed on your 
system the easiest way to install cloudinitd is:

.. code-block:: none

    easy_install cloudinitd

Install from git
================

If you would like to download the source code and install from a git
checkout you can run the following command set:

.. code-block:: none

    git clone git://github.com/nimbusproject/cloudinit.d.git
    cd cloudinitd
    python setup.py install

python 2.5 or greater is required.

Installing on CentOS 5.5 or RHEL 5
==================================

Because CentOS 5.5 does not come with python 2.5 the installation requires
a few additional sets:

.. code-block:: none

    rpm -Uvh http://download.fedora.redhat.com/pub/epel/5/i386/epel-release-5-4.noarch.rpm
    yum -y install python26-devel python26-distribute.noarch gcc
    easy_install-2.6 cloudinitd
    cloudinitd --help

