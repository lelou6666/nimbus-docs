===========================
Scripting with the Phantom Autoscale API
===========================

Phantom uses the AWS Autoscaling protocol, and we
`boto <https://github.com/boto/boto>`_ for scripting Phantom.
On this page we will describe
some simple boto applications for interacting with Phantom.

Phantom API
========

The first thing you will need in order to use the Autoscale API is your 
FutureGrid access tokens.  Acquiring your FutureGrid access tokens is 
described `here <https://portal.futuregrid.org/tutorials/nimbus>`_.
Inside of your hotel.conf file you will find the access tokens under the
entries::

    vws.repository.s3id=<access key>
    vws.repository.s3key=<secret key>

You will also need to know the URL of the Phantom API. It is:
https://phantom.nimbusproject.org/api/dev.

For convenience store those values in the following environment variables::

    $ export EC2_ACCESS_KEY=<access key>
    $ export EC2_SECRET_KEY=<secret key>
    $ export PHANTOM_URL=https://phantom.nimbusproject.org/api/dev

Installing requests
==============

We recommend using requests to interact with the Phantom API.

To get started, create a new
`virtual environment <http://pypi.python.org/pypi/virtualenv>`_ and install
requests into it.  The following commands should do this for you::

    $ virtualenv phantom
    New python executable in phantom/bin/python
    Installing distribute...............done.
    Installing pip...............done.

    $ source phantom/bin/activate

    $ pip install requests
    Downloading/unpacking requests
      Downloading requests-1.2.3.tar.gz (348kB): 348kB downloaded
      Running setup.py egg_info for package requests

    Installing collected packages: requests
      Running setup.py install for requests

    Successfully installed requests
    Cleaning up...

You now have requests installed and ready to use.  Please note the command::

    $ source phantom/bin/activate

You will need to run this command in every session where you 
wish to use your Python requests environment.

Getting a Token
===============

The Phantom API uses tokens and Basic Authentication for authentication. Users
must request a token to access most endpoints in the API.  All other requests
must be authenticated using this token. To use this token with curl, 
for example::

    $ curl -d "username=alice&password=restaurant" http://phantom.nimbusproject.org/api/dev/token
    {"token": "xgy-4h324h2i4h32oi4h23", "user": 1, "success": true}

For convenience store those values in the following environment variables::

    $ export USER_ID=<user id>
    $ export TOKEN=<token>

Then, to use other endpoints, use this user id and token when querying. You can either include the 
user and token as request parameters in any call to phantom, or you can use the basic access authentication
scheme:

1. Combine user id and token into string "user:token"
2. Encode resulting string using Base64
3. Prepend "Basic " (including the trailing space) to the resulting Base64 encoded string

Curl (and most http libraries) do this automatically for you:

   .. sourcecode:: none

      $ curl -u 1:xgy-4h324h2i4h32oi4h23 http://phantom.nimbusproject.org/api/dev/sites
      []


Sample scripts
==============

The following sample programs can be used to aid in understanding.
All of these values can be found in your FutureGrid cloud-client
cloud.properties file.

* `Create a Launch Configuration <https://github.com/nimbusproject/phantomwebapp/blob/master/example_scripts/lc_create.py>`_.

* `Delete a Launch Configuration <https://github.com/nimbusproject/phantomwebapp/blob/master/example_scripts/lc_delete.py>`_.

* `List all Launch Configurations <https://github.com/nimbusproject/phantomwebapp/blob/master/example_scripts/lc_list.py>`_.

* `Create a Domain <https://github.com/nimbusproject/phantomwebapp/blob/master/example_scripts/domain_create.py>`_.

* `Delete a Domain <https://github.com/nimbusproject/phantomwebapp/blob/master/example_scripts/domain_delete.py>`_.

* `List all running domains <https://github.com/nimbusproject/phantomwebapp/blob/master/example_scripts/domain_list.py>`_.

* `Change the n-preserving value <https://github.com/nimbusproject/phantomwebapp/blob/master/example_scripts/domain_alter.py>`_.

Here is a sample session of using the above scripts.  In it we will create a 
launch configuration.  We will then launch a domain that
uses that launch configuration.  First we create the launch configuration::

    $ python lc_create.py testlc1 hello-phantom.gz hotel
    $ python lc_list.py
    testlc1

The next thing we do is create a domain using that launch configuration::

    $ python domain_create.py testDomain1 testlc1 1
    using LaunchConfiguration:testlc1
    $ python asg_list.py
    testDomain1
        testlc1 : 1
        Instances:
        ---------
            hotel : Healthy

The arguments to that program are as follows in order:

* the new domain name
* the launch configuration name
* the size of the domain

Now we clean everything up::

    $ python domain_delete.py testDomain1
    deleting testDomain1
    $ python lc_delete.py testlc1
