=============================
Auto Scale Service Quickstart
=============================

The first preview releases of the service will run exclusively on 
`FutureGrid <http://www.futuregrid.org>`_ resources.  Later releases
will allow users to add any cloud to which they have access.

Get an account
==============

In order to use this service you will first need to have a FutureGrid account.
You can apply for one `here <https://portal.futuregrid.org/user/register>`_.
Once you have a FutureGrid account, request to join the `Nimbus Auto Scale
<https://portal.futuregrid.org/projects/224>`_ project.
We will create your Phantom account when your project join request has been
accepted.

You should also subscribe to the `Nimbus Phantom mailing list
<https://lists.mcs.anl.gov/mailman/listinfo/nimbus-phantom>`_ to receive
announcements, report bugs, or request new features.

Phantom Autoscale API
=====================

The first thing you will need in order to use the Phantom Autoscale API is your
FutureGrid access tokens.  Acquiring your FutureGrid access tokens is 
described `here <https://portal.futuregrid.org/tutorials/nimbus>`_.
Inside of your hotel.conf file you will find the access tokens under the
entries::

    vws.repository.s3id=<access key>
    vws.repository.s3key=<secret key>

You will also need to know the URL of the Autoscale API service. It is:
https://svc.uc.futuregrid.org:8445.

For convenience store those values in the following environment variables::

    export EC2_ACCESS_KEY=<access key>
    export EC2_SECRET_KEY=<secret key>
    export PHANTOM_URL=https://svc.uc.futuregrid.org:8445

boto
====

We recommend using boto to interact with the system.  Unfortunately
the latest released version of boto does not yet include a needed
patch so you will need to get our forked version 
`here <https://github.com/buzztroll/boto>`_ (use the asgcreatetags branch).

The first thing you should do is create a python
`virtual environment <http://pypi.python.org/pypi/virtualenv>`_ and install
boto into it.  The following commands should do this for you::

    $ virtualenv phantom
    New python executable in phantom/bin/python
    Installing distribute...............done.
    Installing pip...............done.

    $ source phantom/bin/activate

    $ pip install -e git://github.com/buzztroll/boto.git@asgcreatetags#egg=boto
    Obtaining boto from git+git://github.com/buzztroll/boto.git@asgcreatetags#egg=boto
      Cloning git://github.com/buzztroll/boto.git (to asgcreatetags) to ./phantom/src/boto
      Running setup.py egg_info for package boto

    .......

    Successfully installed boto
    Cleaning up...

You now have boto installed and ready to use.  Please note the command::

    $ source phantom/bin/activate

You will need to run this command in every session where you 
wish to use your python boto environment.

You can now look at the example 
:doc:`scripting` 
page to see how to use boto to 
interact with the service.
