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
`on github <https://github.com/nimbusproject/PhantomWebApp/blob/master/example_scripts/de_tutorial.py>`_.

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
    import sys
    import time
    import json
    import requests


    class MyPhantomDecisionEngine(object):

        def __init__(self):

            self.user_id = os.environ['USER_ID']
            self.token = os.environ['TOKEN']
            self.api_url = os.environ.get('PHANTOM_URL', "https://phantom.nimbusproject.org/api/dev")

            self.domain_name = "my_domain"
            self.launch_config_name = "my_launch_config"
            self.vm_image = "hello-phantom.gz"
            self.max_vms = 4
            self.key_name = "phantomkey"
            self.image_type = "m1.small"
            self.clouds = ["hotel", "sierra"]

            self.create_launch_configuration()
            self.create_domain()
            self.run_policy()

If you are comfortable with Python, this should be fairly familiar to you. We
import a few modules that we will use in creating our decision engine. Next, we
create a class called "MyPhantomDecisionEngine", and initialize a few variables
that we will use later. You must set USER_ID, TOKEN, and
PHANTOM_URL in your env before running this script.

Our decision engine will use the hello-phantom.gz image, will use the
"phantomkey" SSH key, will use an "m1.small" image,  will start a maximum of
4 VMs per cloud, and will launch VMs on both hotel and sierra.

Initializing our Launch Configuration
=====================================

Now we will create a utility function which will initialize our Launch
Configuration::

        def create_launch_configuration(self):

            # Get a list of existing launch configurations
            r = requests.get("%s/launchconfigurations" % self.api_url, auth=(self.user_id, self.token))
            existing_launch_configurations = r.json()
            existing_lc_names = [lc.get('name') for lc in existing_launch_configurations]

            # Create launch configuration if it doesn't exist
            if self.launch_config_name not in existing_lc_names:

                print "Creating launch config '%s'" % self.launch_config_name
                new_lc = {
                    'name': self.launch_config_name,
                    'cloud_params': {}
                }

                rank = 0
                for cloud in self.clouds:
                    rank = rank + 1
                    cloud_param = {
                        'image_id': self.vm_image,
                        'instance_type': self.image_type,
                        'max_vms': self.max_vms,
                        'common': True,
                        'rank': rank,
                    }
                    new_lc['cloud_params'][cloud] = cloud_param

                r = requests.post("%s/launchconfigurations" % self.api_url,
                    data=json.dumps(new_lc), auth=(self.user_id, self.token))

            else:
                print "Launch config '%s' has already been added, skipping..." % (
                    self.launch_config_name,)

First, we get a list of all of the existing launch configurations that we might
have previously created. Then we create our LC if it does not yet exist.

Note that we are feeding in the parameters we set in our init function into the
LC. We set the name of the LC, the image_id, the instance_type, the
maximum_number of vms, and the rank. The rank is the ordering of clouds in
which phantom will attempt to start VMs.

Initializing our Domain
=======================

Next, we want to set up our domain::

        def create_domain(self):

            # Check if domain already exists
            r = requests.get("%s/domains" % self.api_url, auth=(self.user_id, self.token))
            existing_domains = r.json()

            domain_exists = False
            domain_id = None
            for domain in existing_domains:
                if domain.get('name') == self.domain_name:
                    domain_exists = True
                    domain_id = domain.get('id')
                    break

            # Create our domain
            print "Creating domain %s" % self.domain_name
            new_domain = {
                'name': self.domain_name,
                'de_name': 'multicloud',
                'lc_name': self.launch_config_name,
                'vm_count': 0
            }

            if domain_exists:
                r = requests.put("%s/domains/%s" % (self.api_url, domain_id),
                    data=json.dumps(new_domain), auth=(self.user_id, self.token))
                if r.status_code != 200:
                    sys.exit("Error: %s" % r.text)
            else:
                r = requests.post("%s/domains" % self.api_url,
                    data=json.dumps(new_domain), auth=(self.user_id, self.token))
                if r.status_code != 201:
                    sys.exit("Error: %s" % r.text)

First, we must check whether there is already a domain with the name we like. If
so, we will need to overwrite it, rather than create it.

Next, we pick the decision engine name to use. We will use the standard
'multicloud' de.

Then, we pick the launch configuration this domain should use. We want to use
the one we set up earlier.

Next, we set how many VMs we would like to be started when we start our domain.
We will start with 0, but this can be whatever you like. This is the vm_count.

Finally, we create our domain. We feed in the parameters we've prepared, and
start the domain.

Defining our Decision Engine Policy
===================================

Now that we have setup up our Launch Config and Domain, we can define the policy
for our domain. As stated in the intro, we will increase our VM capacity every
ten seconds, then we will let them run for a minute, then shut them down::

        def run_policy(self):

            r = requests.get("%s/domains" % self.api_url, auth=(self.user_id, self.token))
            existing_domains = r.json()
            domain = None
            for _domain in existing_domains:
                if _domain.get('name') == self.domain_name:
                    domain = _domain
                    break
            else:
                raise SystemExit("Couldn't get domain %s" % self.domain_name)

            vm_count = 1
            print "set %s vm_count to %s" % (self.domain_name, vm_count)
            domain['vm_count'] = vm_count
            r = requests.put("%s/domains/%s" % (self.api_url, domain.get('id')),
                    data=json.dumps(domain), auth=(self.user_id, self.token))
            time.sleep(10)

            vm_count += 1
            print "set %s vm_count to %s" % (self.domain_name, vm_count)
            domain['vm_count'] = vm_count
            r = requests.put("%s/domains/%s" % (self.api_url, domain.get('id')),
                    data=json.dumps(domain), auth=(self.user_id, self.token))
            time.sleep(10)

            vm_count += 1
            print "set %s vm_count to %s" % (self.domain_name, vm_count)
            domain['vm_count'] = vm_count
            r = requests.put("%s/domains/%s" % (self.api_url, domain.get('id')),
                    data=json.dumps(domain), auth=(self.user_id, self.token))
            time.sleep(10)

            vm_count += 1
            print "set %s vm_count to %s" % (self.domain_name, vm_count)
            domain['vm_count'] = vm_count
            r = requests.put("%s/domains/%s" % (self.api_url, domain.get('id')),
                    data=json.dumps(domain), auth=(self.user_id, self.token))
            time.sleep(10)

            print "let domain settle for 60s"
            time.sleep(60)

            vm_count = 0
            domain['vm_count'] = vm_count
            r = requests.put("%s/domains/%s" % (self.api_url, domain.get('id')),
                    data=json.dumps(domain), auth=(self.user_id, self.token))
            print "set %s vm_count back to %s" % (self.domain_name, vm_count)

Use your Decision Engine
========================

Finally, go back to your __init__ function, and call the three functions you
created::

            self.create_launch_configuration()
            self.create_domain()
            self.run_policy()

At the end of your file, initialize your DE::

    MyPhantomDecisionEngine()
   

Then save your file, and try out your Decision Engine::

    $ python de.py
    Launch config 'my_launch_config@hotel' has already been added, skipping...
    Launch config 'my_launch_config@sierra' has already been added, skipping...
    Removing existing instance of domain 'my_domain'
    Creating domain my_domain
    set my_domain vm_count to 1
    set my_domain vm_count to 2
    set my_domain vm_count to 3
    set my_domain vm_count to 4
    let domain settle for 60s
    set my_domain vm_count back to 0
