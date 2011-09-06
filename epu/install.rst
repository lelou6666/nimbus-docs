=======
Install
=======

This page is part of the EPU quickstart, it assumes you have read the `EPU overview page <index.html>`_.

After this page you will have installed the software necessary to launch EPUs, it assumes you have read the `dependencies section <dependencies.html>`_ and followed any necessary instructions. 


===============
cloudinit.d 1.0
===============

Activate the virtualenv discussed in the `dependencies section <dependencies.html>`_:

.. code-block:: none

    $ cd /tmp/epu
    $ source bin/activate

Check that the virtualenv is active:

.. code-block:: none

    $ which python
    /tmp/epu/bin/python

Install cloudinit.d 1.0:

.. code-block:: none

    $ easy_install cloudinitd==1.0


=======
epumgmt
=======

Next, with the same virtualenv activated, install epumgmt:

.. code-block:: none

    $ git clone https://github.com/nimbusproject/epumgmt.git
    $ cd epumgmt
    $ git checkout -b R1 previewR1
    $ python setup.py install


=============
Install Check
=============

Make sure the program installations went well.  In a fresh terminal:

.. code-block:: none

    $ alias epu="source /tmp/epu/bin/activate && cd /tmp/epu"
    $ epu
    $ which cloudinitd
    /tmp/epu/bin/cloudinitd
    $ which epumgmt
    /tmp/epu/bin/epumgmt
    $ cloudinitd -h
    [...]
    $ epumgmt -h
    [...]
    



