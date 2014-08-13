============================
Building a Phantom Appliance
============================

You can use Phantom to run any kind of application in the cloud. However, since
Phantom instantiates and manages virtual machines on your behalf, you will want
to reduce to a minimum any manual interaction with virtual machines and
automate the configuration of your application.

This page presents some guidelines on how to use Phantom to automatically run
fully-configured applications.  We will show how to create virtual machines
running specific applications, i.e. appliances that we can deploy with Phantom.

Customizing virtual machine images
==================================

The most basic step in creating a Phantom appliance is to customize a virtual
machine image with your applications of choice. This can be done by starting
from scratch or by customizing an existing virtual machine image.

Creating an image from scratch offers the most flexibility and control: you
decide exactly what operating system and software to install in the virtual
machine image. However, it is a difficult task, as your image needs to be
compatible with the IaaS cloud you intend to use (image format, operating
system, network configuration, etc.). If you want to create an image from
scratch, it is best to first document yourself about the virtualization
technology used by your cloud (see our `Science Clouds page
<http://scienceclouds.org/infrastructure-clouds/>`_ for more details). You can
create an image from scratch with a manual operating system installation inside
a virtual machine, or you can use `an automated tool
<http://scienceclouds.org/ecosystem/generation-of-virtual-machine-images/>`_.

An alternative and simpler approach is to start from an existing image. On most
IaaS clouds, you will find basic images with few packages installed, that you
can further customize to run your applications. For example, Nimbus on
FutureGrid has the *hello-cloud* image and several Ubuntu images. Amazon EC2
offers a very large range of public images, for example `Ubuntu images
<http://cloud-images.ubuntu.com/locator/ec2/>`_.

The steps for customizing a virtual machine image are specific to each type of
cloud. For Amazon EC2, the procedure is described `here
<http://docs.aws.amazon.com/gettingstarted/latest/wah-linux/getting-started-create-custom-ami.html>`_.
For Nimbus, you can follow `this tutorial
<https://portal.futuregrid.org/tutorials/nimbus>`_ (scroll down to *Create a
New VM Image*).

Configuring virtual machines with user-data
===========================================

Often customizing a virtual machine image is not enough, as applications need
to be configured with information available only at the time of deployment.
For solving this, most clouds provide a way to pass data to instances. In
Amazon EC2 and Nimbus, this is called `user-data
<http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html>`_.
The content of user-data can be retrieved from each instance using an HTTP
request.  On Amazon EC2, this request is made to a fixed address. On Nimbus,
this is made to the service node, whose hostname is stored in
``/var/nimbus-metadata-server-url`` just before deploying an instance.

Phantom allows you to pass user data to your instances as part of the launch
configuration.  This can be leveraged for configuring virtual machines. For
example, a shell script can be passed via user-data and automatically executed
by your instances. With Nimbus, this can be performed by executing the
following code on boot::

    TMPFILE=`mktemp`
    I=0
    while ! curl "`cat /var/nimbus-metadata-server-url`/latest/user-data" -o $TMPFILE; do
      sleep 1
      I=`expr $I + 1`
      if [ $I -gt 60 ]; then
        exit 1
      fi
    done
    chmod +x $TMPFILE
    $TMPFILE

This script attempts to download the content of user-data from the hostname
stored in ``/var/nimbus-metadata-server-url`` and executes it, or gives up
after failing to do so for a minute.

Automatically interacting with Phantom
======================================

Just as it is possible to use :doc:`scripting </scripting>` to interact with
Phantom from your workstation, you can also configure your appliance to use
boto scripts to interact with Phantom on your behalf. For example, this is used
by our `TORQUE appliance
<http://scienceclouds.org/appliances/autoscaling-torque-appliance/>`_ to manage
an autoscaling TORQUE cluster. In that case the software doing the interaction
with Phantom is `Phorque <https://github.com/cu-csc/phorque>`_. You can read
its source code to learn more about it.
