=======
Install
=======

Dependencies
============

We strive to make the Nimbus context broker node as simple as possible to install and configure, but there are a few system dependencies and requirements you will need before starting.


- Sun Java 1.5 or later

  The *java* and *javac* commands should be on your path. You can check your Java version with these commands:

  .. code-block:: none

    java -version
    javac -version

  Note that GCJ is not supported.

- Python 2.5 or later (but not 3.x)

  You can check the version of your system Python with this command:
  
  .. code-block:: none
  
    python -V

  Note that Nimbus does not support Python 3 at this time. The most recent compatible Python version is 2.7.

- Apache Ant 1.6.2 or later

  You must also have the *propertyfile* task available which is usually installed separately from Ant itself. On Redhat-compatible systems this is often a package called *ant-nodeps*. On Debian/Ubuntu the package is *ant-optional*.  To be sure, you can check for the presence of a library called *ant-nodeps.jar* in your Ant installation.


Distribution
============

The latest tarball for the standalone broker can be found on the  `Nimbus download page <http://www.nimbusproject.org/downloads/>`_.  Look for the link in the *Platform* section.


Installer
=========

Once downloaded, you will expand the tarball anywhere, pick a target directory for installation, and run the installer.

- Creating a new user dedicated to running the service is recommended, e.g. *nimbus*

- Expand the tarball

  .. code-block:: none
  
    tar xfz nimbus-ctxbroker-2.8-src.tar.gz
  
- Check dependencies

  .. code-block:: none
  
    cd nimbus-ctxbroker-2.8-src
    ./scripts/check-dependencies.sh
  
- Pick a target directory

  It could be within the *nimbus* user home directory, or something like */opt/nimbus*. If the directory exists, it must be empty and writable by the *nimbus* user.  If it does not exist, the parent directory must be writable by the *nimbus* user.
  
- Throughout this guide, we will refer to this installation directory as *$NIMBUS_HOME*.

- To install, run the install command from the source directory (specifying your chosen destination).
  
  .. code-block:: none
  
    cd nimbus-ctxbroker-2.8-src
    ./install $NIMBUS_HOME

.. note::
  The installer will ask you a few configuration questions. 

.. note::
  Software is not installed anywhere else on the machine, only under this installation directory.


Operate
=======

To start the context broker, run:

  .. code-block:: none

    $NIMBUS_HOME/bin/brokerctl start

To see the other commands, run:

  .. code-block:: none

    $NIMBUS_HOME/bin/brokerctl -h

After starting, the logs are here:

  .. code-block:: none

    less $NIMBUS_HOME/var/broker.log
    
You need to open the default ports to the outside for anything to be able to use the broker:

- 8443 (WSRF)
- 8446 (REST)

To add users follow the instructions in the following file:

  .. code-block:: none

    $NIMBUS_HOMEservices/etc/nimbus-context-broker/user-mapfile





