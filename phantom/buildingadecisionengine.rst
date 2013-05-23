=========================================================
Building a Decision Engine with the Phantom Scripting API
=========================================================

Once you have gotten familiar with Phantom, you may want behaviors that
Phantom does not already provide. For example, you may want to scale your
domain with behaviour that you cannot define in the GUI. This page will
guide you in creating a "Decision Engine" for Phantom that will automate
scaling your VMs in a domain.

As an example, we will build a decision engine that starts a new VM every
10 seconds, then lets them run for a minute, then shuts them down.

You can get the source to the tutorial decision engine
`on github <https://github.com/nimbusproject/Phantom/blob/master/sandbox/de_tutorial.py>`_.

Basics
======

Ensure that your have set up a suitable scripting environment. The
:doc:`/scripting` page will guide you in setting up your environment. This
guide assumes that you are familiar with Python.

Initializing your Decision engine
=================================

To start, we will import the necessary libraries, and set up the basics of our
decision engine::

    import os
    import urlparse
    import boto
    import boto.ec2.autoscale

    from boto.regioninfo import RegionInfo
    from boto.ec2.autoscale import Tag
    from boto.ec2.autoscale.launchconfig import LaunchConfiguration
    from boto.ec2.autoscale.group import AutoScalingGroup


    class MyPhantomDecisionEngine(object):

        def __init__(self):

            self.username = os.environ['EC2_ACCESS_KEY']
            self.password = os.environ['EC2_SECRET_KEY']
            self.iaas_url = os.environ['PHANTOM_URL']

            self.domain_name = "my_domain"
            self.launch_config_name = "my_launch_config"

            self.vm_image = "hello-phantom.gz"
            self.key_name = "phantomkey"
            self.image_type = "m1.small"
            self.max_vms = 4
            self.clouds = ["hotel", "sierra"]

            # Create our Phantom connection
            parsed_url = urlparse.urlparse(iaas_url)
            ssl = parsed_url.scheme == "https"
            host = parsed_url.hostname
            port = parsed_url.port

            region = RegionInfo(name="nimbus", endpoint=host)
            self.connection = boto.ec2.autoscale.AutoScaleConnection(
                aws_access_key_id=username, aws_secret_access_key=password,
                is_secure=ssl, port=port, region=region, validate_certs=False)

            self.connection.host = host

If you are comfortable with Python, this should be fairly familiar to you. We
import a few modules that we will use in creating our decision engine. Next, we
create a class called "MyPhantomDecisionEngine", and initialize a few variables
that we will use later. You must set EC2_ACCESS_KEY, EC2_SECRET_KEY, and
PHANTOM_URL in your env before running this script.

Our decision engine will use the hello-phantom.gz image, will use the
"phantomkey" SSH key, will use an "m1.small" image,  will start a maximum of
4 VMs per cloud, and will launch VMs on both hotel and sierra.

Next, we create our connection to Phantom. We pull out the hostname and port
from our phantom URL, then construct our connection to Phantom.

Initializing our Launch Configuration
=====================================

Now we will create a utility function which will initialize our Launch
Configuration::

        def create_launch_configuration(self):

            existing_launch_configurations = connection.get_all_launch_configurations()
            existing_lc_names = [lc.name for lc in existing_launch_configurations]

            for cloud in self.clouds:
                full_lc_name = "%s@%s" % (self.launch_config_name, cloud)

                if not full_lc_name in existing_lc_names:
                    print "Creating launch config '%s'" % full_lc_name

                    launch_config = LaunchConfiguration(
                        self.connection, name=full_lc_name, image_id=self.image,
                        key_name=self.key_name, security_groups=['default'],
                        instance_type=self.image_type)

                    self.connection.create_launch_configuration(launch_config)
                else:
                    print "Launch config '%s' has already been added, skipping..." % (full_lc_name,)

First, we get a list of all of the existing launch configurations that we might
have previously created. Then we create any LCs that do not exist. Note that we
create an LC for each cloud that we want to use, named with the lc_name@cloud
convention. So if we wanted an LC named "my_great_lc" on a cloud named hotel,
we would create an LC named my_great_lc@hotel.

Note that we are feeding in the parameters we set in our init function into the
LC. We set the name of the LC, the image_id, the key_name, and the instance_type.

Initializing our Domain
=======================

Next, we want to set up our domain::

        def create_domain(self):

            # Set our policy name
            policy_name_key = 'PHANTOM_DEFINITION'
            policy_name = 'error_overflow_n_preserving'

            # Set the order of clouds in which VMs are started
            ordered_clouds_key = 'clouds'
            ordered_clouds = ""
            cloud_size_pairs = ["%s:%s" % (cloud, self.max_vms) for cloud in self.clouds]
            ordered_clouds = ",".join(cloud_size_pairs)

            # Get a Cloud and Launch Config to feed to the domain constructor
            a_cloud = self.clouds[0]
            a_lc_name = "%s@%s" % (self.launch_config_name, a_cloud)
            a_lc_list = self.connection.get_all_launch_configurations(names=[a_lc_name, ])

            if len(a_lc_list) != 1:
                print "Couldn't get launch config %s" % self.launch_config_name
                raise SystemExit("Couldn't get launch config %s" % self.launch_config_name)
            a_lc = a_lc_list[0]

            # Set how many domains we would like to start our domain with
            n_preserve_key = 'minimum_vms'
            n_preserve = 0

            # Marshall Phantom Parameters
            policy_tag = Tag(connection=self.connection, key=policy_name_key,
                             value=policy_name, resource_id=self.domain_name)
            clouds_tag = Tag(connection=self.connection, key=ordered_clouds_key,
                             value=ordered_clouds, resource_id=self.domain_name)
            npreserve_tag = Tag(connection=self.connection, key=n_preserve_key,
                                value=n_preserve, resource_id=self.domain_name)

            tags = [policy_tag, clouds_tag, npreserve_tag]

            # Remove any existing domain name with the same name
            existing_domains = self.connection.get_all_groups(names=[self.domain_name, ])
            for domain in existing_domains:
                print "Removing existing instance of domain '%s'" % domain.name
                domain.delete()

            # Create our domain
            print "Creating domain %s" % self.domain_name
            domain = AutoScalingGroup(
                availability_zones=["us-east-1"],
                connection=self.connection, group_name=self.domain_name,
                min_size=n_preserve, max_size=n_preserve, launch_config=a_lc, tags=tags)
            self.connection.create_auto_scaling_group(domain)

First, we must set up the parameters that we will feed to Phantom. We select a
policy for Phantom to use, 'error_overflow_n_preserving'. This is generally the
policy you will want to use when creating a decision engine.

Next, you will create an ordering of clouds for Phantom to start VMs on. In our
case, we don't particularly care where Phantom sets up its VMs.

Next, we get a name of a cloud, and a name of a launch config. These are set up
in the previous step. The parameters here don't matter so much, but are required
as the AWS Autoscale API requires them. Phantom does not really use them, but boto
will validate these parameters.

Next, we set how many VMs we would like to be started when we start our domain.
We will start with 0, but this can be whatever you like.

Next, we marshal the Phantom parameters into tags, which we will feed into the
AutoScalingGroup constructor.

Next, we remove any existing domains with the same name as ours (perhaps from
an earlier run of the decision engine.

Finally, we create our domain. We feed in the parameters we've prepared, and
start the domain.

Defining our Decision Engine Policy
===================================

Now that we have setup up our Launch Config and Domain, we can define the policy
for our domain. As stated in the intro, we will increase our VM capacity every
ten seconds, then we will let them run for a minute, then shut them down::

        def run_policy(self):

            domains = self.connection.get_all_groups(names=[self.domain_name, ])
            if len(domains) != 1:
                raise SystemExit("Couldn't get domain %s" % self.domain_name)
            domain = domains[0]

            capacity = 1
            print "set %s capacity to %s" % (self.domain_name, capacity)
            domain.set_capacity(capacity)
            time.sleep(10)

            capacity += 1
            print "set %s capacity to %s" % (self.domain_name, capacity)
            domain.set_capacity(capacity)
            time.sleep(10)

            capacity += 1
            print "set %s capacity to %s" % (self.domain_name, capacity)
            domain.set_capacity(capacity)
            time.sleep(10)

            capacity += 1
            print "set %s capacity to %s" % (self.domain_name, capacity)
            domain.set_capacity(capacity)

            print "let domain settle for 60s"
            time.sleep(60)

            capacity = 0
            print "set %s capacity back to %s" % (self.domain_name, capacity)
            domain.set_capacity(capacity)

Use your Decision Engine
========================

Finally, go back to your __init__ function, and call the three functions you
created::

            self.create_launch_configuration()
            self.create_domain()
            self.run_policy()

Then save your file, and try out your Decision Engine::

    $ python de.py
    Launch config 'my_launch_config@hotel' has already been added, skipping...
    Launch config 'my_launch_config@sierra' has already been added, skipping...
    Removing existing instance of domain 'my_domain'
    Creating domain my_domain
    set my_domain capacity to 1
    set my_domain capacity to 2
    set my_domain capacity to 3
    set my_domain capacity to 4
    let domain settle for 60s
    set my_domain capacity back to 0
