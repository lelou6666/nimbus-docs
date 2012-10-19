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
Once you have a FutureGrid account you should join the project 
`Nimbus Auto Scale <https://portal.futuregrid.org/projects/224>`_.

Once you have a FutureGrid account, please request a Phantom account by sending
email to workspace-user@lists.globus.org.

REST API
========

The first thing you will need in order to use the REST API is your 
FutureGrid access tokens.  Acquiring your FutureGrid access tokens is 
described `here <https://portal.futuregrid.org/tutorials/nimbus>`_.
Inside of your hotel.conf file you will find the access tokens under the
entries::

    vws.repository.s3id=<access key>
    vws.repository.s3key=<secret key>

You will also need to know the URL of the REST service. It is:
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
`here <https://github.com/buzztroll/boto>`_

The first thing you should do is create a python
`virtual environment <http://pypi.python.org/pypi/virtualenv>`_ and install
boto into it.  The following commands should do this for you::

    $ virtualenv phantom
    New python executable in phantom/bin/python
    Installing distribute...............done.
    Installing pip...............done.

    $ source phantom/bin/activate

    ~$ git clone git://github.com/buzztroll/boto.git
    Cloning into 'boto'...
    remote: Counting objects: 22004, done.
    remote: Compressing objects: 100% (5802/5802), done.
    Receiving objects: 100% (22004/22004), 5.27 MiB | 414 KiB/s, done.
    remote: Total 22004 (delta 16804), reused 21222 (delta 16144)
    Resolving deltas: 100% (16804/16804), done.
    $ cd boto/
    $ python setup.py install
    .......
    Processing dependencies for boto==2.5.2
    Finished processing dependencies for boto==2.5.2

You now have boto installed and ready to use.  Please note the command::

    $ source phantom/bin/activate

You will need to run this command in every session where you 
wish to use your python boto environment.

You can now look at the example 
:doc:`scripting` 
page to see how to use boto to 
interact with the service.
