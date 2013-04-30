=======================
Nimbus Phantom HTTP API
=======================

.. contents::
    :local:


Site Resources
==============

.. http:get:: /api/v1.0/sites

   List all clouds known to the authenticated user, and their details

   :statuscode 200: no error

   **Example request**:

   .. sourcecode:: http

      GET /api/v1.0/sites HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      [
        {
          "id": "ec2",
          "credentials": "/api/v1.0/credentials/ec2",
          "uri": "/api/v1.0/sites/ec2"
        },
        {
          "id": "hotel",
          "credentials": "/api/v1.0/credentials/hotel",
          "uri": "/api/v1.0/sites/hotel"
        },
        {
          "id": "sierra",
          "credentials": "/api/v1.0/credentials/sierra",
          "uri": "/api/v1.0/sites/sierra"
        }
      ]

.. http:get:: /api/v1.0/sites/(cloud_id)

   Get details for the cloud `cloud_id`

   :statuscode 200: no error
   :statuscode 404: cloud is unknown

   **Example request**:

   .. sourcecode:: http

      GET /api/v1.0/sites/hotel HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "id": "hotel",
        "credentials": "/api/v1.0/credentials/hotel",
        "uri": "/api/v1.0/sites/hotel"
      }


Credentials Resources
=====================

.. http:get:: /api/v1.0/credentials

   List all cloud credentials for the authenticated user

   :statuscode 200: no error

   **Example request**:

   .. sourcecode:: http

      GET /api/v1.0/credentials HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      [
        {
          "id": "ec2",
          "access_key": "aws_access_key_id",
          "secret_key": "aws_secret_access_key",
          "key_name": "phantom_ssh_key",
          "uri": "/api/v1.0/credentials/ec2"
        },
        {
          "id": "hotel",
          "access_key": "hotel_access_key_id",
          "secret_key": "hotel_secret_access_key",
          "key_name": "phantom_ssh_key",
          "uri": "/api/v1.0/credentials/hotel"
        }
      ]

.. http:get:: /api/v1.0/credentials/(cloud_id)

   Get cloud credentials for the cloud `cloud_id`

   :statuscode 200: no error
   :statuscode 404: cloud is unknown

   **Example request**:

   .. sourcecode:: http

      GET /api/v1.0/credentials/hotel HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "id": "hotel",
        "access_key": "hotel_access_key_id",
        "secret_key": "hotel_secret_access_key",
        "key_name": "phantom_ssh_key",
        "uri": "/api/v1.0/credentials/hotel"
      }

.. http:post:: /api/v1.0/credentials

   Save new cloud credentials

   :statuscode 201: credentials saved

   **Example request**:

   .. sourcecode:: http

      POST /api/v1.0/credentials HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

      {
        "id": "sierra",
        "access_key": "sierra_access_key_id",
        "secret_key": "sierra_secret_access_key",
        "key_name": "phantom_ssh_key"
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 201 Created
      Content-Type: application/json
      Location: /api/v1.0/credentials/sierra

      {
        "id": "sierra",
        "access_key": "sierra_access_key_id",
        "secret_key": "sierra_secret_access_key",
        "key_name": "phantom_ssh_key",
        "uri": "/api/v1.0/credentials/sierra"
      }

.. http:put:: /api/v1.0/credentials/(cloud_id)

   Update cloud credentials

   :statuscode 200: credentials updated

   **Example request**:

   .. sourcecode:: http

      PUT /api/v1.0/credentials/ec2 HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

      {
        "id": "ec2",
        "access_key": "updated_aws_access_key_id",
        "secret_key": "updated_aws_secret_access_key",
        "key_name": "phantom_ssh_key"
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json
      Location: /api/v1.0/credentials/ec2

      {
        "id": "ec2",
        "access_key": "updated_aws_access_key_id",
        "secret_key": "updated_aws_secret_access_key",
        "key_name": "phantom_ssh_key",
        "uri": "/api/v1.0/credentials/ec2"
      }

.. http:delete:: /api/v1.0/credentials/(cloud_id)

   Delete cloud credentials for the cloud `cloud_id`

   :statuscode 204: credentials deleted

   **Example request**:

   .. sourcecode:: http

      DELETE /api/v1.0/credentials/ec2 HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No Content
      Content-Type: application/json


Launch Configuration Resources
==============================

.. http:get:: /api/v1.0/launchconfigurations

   List all launch configurations for the authenticated user

   :statuscode 200: no error

   **Example request**:

   .. sourcecode:: http

      GET /api/v1.0/launchconfigurations HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      [
        {
          "id": "myfirstlc",
          "cloud_params": {
            "hotel": {
              "image_id": "hello-phantom.gz",
              "instance_type": "m1.small",
              "max_vms": 16,
              "common": true,
              "rank": 1,
              "user_data": null
            },
            "ec2": {
              "image_id": "ami-deadbeef",
              "instance_type": "m1.small",
              "max_vms": -1,
              "common": false,
              "rank": 2,
              "user_data": null
            }
          },
          "uri": "/api/v1.0/launchconfigurations/myfirstlc"
        }
      ]

.. http:get:: /api/v1.0/launchconfigurations/(launchconfiguration_id)

   Get details for the launch configuration `launch_configuration_id`

   :statuscode 200: no error
   :statuscode 404: launch configuration is unknown

   **Example request**:

   .. sourcecode:: http

      GET /api/v1.0/launchconfigurations/myfirstlc HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "id": "myfirstlc",
        "cloud_params": {
          "hotel": {
            "image_id": "hello-phantom.gz",
            "instance_type": "m1.small",
            "max_vms": 16,
            "common": true,
            "rank": 1,
            "user_data": null
          },
          "ec2": {
            "image_id": "ami-deadbeef",
            "instance_type": "m1.small",
            "max_vms": -1,
            "common": false,
            "rank": 2,
            "user_data": null
          }
        },
        "uri": "/api/v1.0/launchconfigurations/myfirstlc"
      }

.. http:post:: /api/v1.0/launchconfigurations

   Create a new launch configuration

   :statuscode 201: launch configuration created

   **Example request**:

   .. sourcecode:: http

      POST /api/v1.0/launchconfigurations HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

      {
        "id": "mysecondlc",
        "cloud_params": {
          "hotel": {
            "image_id": "hello-cloud",
            "instance_type": "m1.large",
            "max_vms": -1,
            "common": true,
            "rank": 1,
            "user_data": "Hello World"
          }
        }
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 201 Created
      Content-Type: application/json
      Location: /api/v1.0/launchconfigurations/mysecondlc

      {
        "id": "mysecondlc",
        "cloud_params": {
          "hotel": {
            "image_id": "hello-cloud",
            "instance_type": "m1.large",
            "max_vms": -1,
            "common": true,
            "rank": 1,
            "user_data": "Hello World"
          }
        },
        "uri": "/api/v1.0/launchconfigurations/mysecondlc"
      }

.. http:put:: /api/v1.0/launchconfigurations/(launch_configuration_id)

   Update a launch configuration

   :statuscode 200: launch configuration updated

   **Example request**:

   .. sourcecode:: http

      PUT /api/v1.0/launchconfigurations/mysecondlc HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

      {
        "id": "mysecondlc",
        "cloud_params": {
          "hotel": {
            "image_id": "hello-cloud",
            "instance_type": "m1.large",
            "max_vms": 5,
            "common": true,
            "rank": 1,
            "user_data": "Hello World"
          }
        }
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json
      Location: /api/v1.0/launchconfigurations/mysecondlc

      {
        "id": "mysecondlc",
        "cloud_params": {
          "hotel": {
            "image_id": "hello-cloud",
            "instance_type": "m1.large",
            "max_vms": 5,
            "common": true,
            "rank": 1,
            "user_data": "Hello World"
          }
        },
        "uri": "/api/v1.0/launchconfigurations/mysecondlc"
      }

.. http:delete:: /api/v1.0/launchconfigurations/(launch_configuration_id)

   Delete a launch configuration

   :statuscode 204: launch configuration deleted

   **Example request**:

   .. sourcecode:: http

      DELETE /api/v1.0/launchconfigurations/myfirstlc HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No Content
      Content-Type: application/json


Domain Resources
================

.. http:get:: /api/v1.0/domains

   List all domains for the authenticated user

   :statuscode 200: no error

   **Example request**:

   .. sourcecode:: http

      GET /api/v1.0/domains HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      [
        {
          "id": "myfirstdomain",
          "de_name": "multicloud",
          "launchconfiguration": "/api/v1.0/launchconfigurations/myfirstlc",
          "vm_count": 1,
          "uri": "/api/v1.0/domains/myfirstdomain"
        }
      ]

.. http:get:: /api/v1.0/domains/(domain_id)

   Get details for the domain `domain_id`

   :statuscode 200: no error
   :statuscode 404: domain is unknown

   **Example request**:

   .. sourcecode:: http

      GET /api/v1.0/domains/myfirstdomain HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "id": "myfirstdomain",
        "de_name": "multicloud",
        "launchconfiguration": "/api/v1.0/launchconfigurations/myfirstlc",
        "vm_count": 1,
        "uri": "/api/v1.0/domains/myfirstdomain"
      }

.. http:post:: /api/v1.0/domains

   Create a new domain

   :statuscode 201: domain created

   **Example request**:

   .. sourcecode:: http

      POST /api/v1.0/domains HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

      {
        "id": "myseconddomain",
        "de_name": "sensor",
        "lc_name": "mysecondlc",
        "monitor_sensors": "proc.loadavg.1min,df.inodes.free",
        "sensor_minimum_vms": 1,
        "sensor_maximum_vms": 10,
        "sensor_metric": "proc.loadavg.1min",
        "sensor_scale_down_threshold": "0.5",
        "sensor_scale_down_vms": 1,
        "sensor_scale_up_threshold": 1,
        "sensor_scale_up_vms": 1,
        "sensor_cooldown": 60
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 201 Created
      Content-Type: application/json
      Location: /api/v1.0/domains/myseconddomain

      {
        "id": "myseconddomain",
        "de_name": "sensor",
        "launchconfiguration": "/api/v1.0/launchconfigurations/mysecondlc",
        "monitor_sensors": "proc.loadavg.1min,df.inodes.free",
        "sensor_minimum_vms": 1,
        "sensor_maximum_vms": 10,
        "sensor_metric": "proc.loadavg.1min",
        "sensor_scale_down_threshold": "0.5",
        "sensor_scale_down_vms": 1,
        "sensor_scale_up_threshold": 1,
        "sensor_scale_up_vms": 1,
        "sensor_cooldown": 60
        "uri": "/api/v1.0/domains/myseconddomain"
      }

.. http:put:: /api/v1.0/domains/(domain_id)

   Update a domain

   :statuscode 200: domain updated

   **Example request**:

   .. sourcecode:: http

      PUT /api/v1.0/domains/mysecondomain HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

      {
        "id": "myseconddomain",
        "de_name": "sensor",
        "lc_name": "mysecondlc",
        "monitor_sensors": "proc.loadavg.1min,df.inodes.free",
        "sensor_minimum_vms": 1,
        "sensor_maximum_vms": 5,
        "sensor_metric": "proc.loadavg.1min",
        "sensor_scale_down_threshold": "0.5",
        "sensor_scale_down_vms": 1,
        "sensor_scale_up_threshold": 1,
        "sensor_scale_up_vms": 1,
        "sensor_cooldown": 60
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json
      Location: /api/v1.0/domains/myseconddomain

      {
        "id": "myseconddomain",
        "de_name": "sensor",
        "launchconfiguration": "/api/v1.0/launchconfigurations/mysecondlc",
        "monitor_sensors": "proc.loadavg.1min,df.inodes.free",
        "sensor_minimum_vms": 1,
        "sensor_maximum_vms": 5,
        "sensor_metric": "proc.loadavg.1min",
        "sensor_scale_down_threshold": "0.5",
        "sensor_scale_down_vms": 1,
        "sensor_scale_up_threshold": 1,
        "sensor_scale_up_vms": 1,
        "sensor_cooldown": 60,
        "uri": "/api/v1.0/domains/myseconddomain"
      }

.. http:delete:: /api/v1.0/domains/(domain_id)

   Terminate a domain

   :statuscode 204: domain terminated

   **Example request**:

   .. sourcecode:: http

      DELETE /api/v1.0/domains/myfirstdomain HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No Content
      Content-Type: application/json


Instances Resources
===================

Each domain can have a number of instances attached to it.

.. http:get:: /api/v1.0/domains/(domain_id)/instances

   List all instances attached to the domain `domain_id`

   :statuscode 200: no error

   **Example request**:

   .. sourcecode:: http

      GET /api/v1.0/domains/myfirstdomain/instances HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      [
        {
          "instance_id": "i-75c0b81b",
          "lifecycle_state": "400-PENDING",
          "hostname": "vm-25.sdsc.futuregrid.org",
          "cloud": "/api/v1.0/sites/sierra",
          "image_id": "hello-phantom.gz",
          "instance_type": "m1.small",
          "keyname": "phantomkey",
          "uri": "/api/v1.0/domains/myfirstdomain/instances/i-75c0b81b"
        }
      ]

.. http:get:: /api/v1.0/domains/(domain_id)/instances/(instance_id)

   Get details for the instance `instance_id` attached to the domain `domain_id`

   :statuscode 200: no error
   :statuscode 404: instance is unknown

   **Example request**:

   .. sourcecode:: http

      GET /api/v1.0/domains/myfirstdomain/instances/i-75c0b81b HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "instance_id": "i-75c0b81b",
        "lifecycle_state": "400-PENDING",
        "hostname": "vm-25.sdsc.futuregrid.org",
        "cloud": "/api/v1.0/sites/sierra",
        "image_id": "hello-phantom.gz",
        "instance_type": "m1.small",
        "keyname": "phantomkey",
        "uri": "/api/v1.0/domains/myfirstdomain/instances/i-75c0b81b"
      }

.. http:delete:: /api/v1.0/domains/(domain_id)/instances/(instance_id)

   Terminate the instance `instance_id` within the domain `domain_id`

   :statuscode 204: instance terminated

   **Example request**:

   .. sourcecode:: http

      DELETE /api/v1.0/domains/myfirstdomain/instances/i-75c0b81b HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No Content
      Content-Type: application/json
