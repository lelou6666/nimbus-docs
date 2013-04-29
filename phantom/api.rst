=======================
Nimbus Phantom HTTP API
=======================

.. contents::
    :local:


Site Resources
==============

.. http:get:: /api/v0.1/sites

   List all clouds known to the authenticated user

   **Example request**:

   .. sourcecode:: http

      GET /api/v0.1/sites HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      [
        {
          "id": "ec2",
          "credentials": "/api/v0.1/credentials/ec2",
          "uri": "/api/v0.1/sites/ec2"
        },
        {
          "id": "hotel",
          "credentials": "/api/v0.1/credentials/hotel",
          "uri": "/api/v0.1/sites/hotel"
        },
        {
          "id": "sierra",
          "credentials": "/api/v0.1/credentials/sierra",
          "uri": "/api/v0.1/sites/sierra"
        }
      ]

   :statuscode 200: no error


Credentials Resources
=====================

.. http:get:: /api/v0.1/credentials

   List all cloud credentials for the authenticated user

   **Example request**:

   .. sourcecode:: http

      GET /api/v0.1/credentials HTTP/1.1
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
          "uri": "/api/v0.1/credentials/ec2"
        },
        {
          "id": "hotel",
          "access_key": "hotel_access_key_id",
          "secret_key": "hotel_secret_access_key",
          "key_name": "phantom_ssh_key",
          "uri": "/api/v0.1/credentials/hotel"
        }
      ]

   :statuscode 200: no error

.. http:post:: /api/v0.1/credentials

   Save new cloud credentials

   **Example request**:

   .. sourcecode:: http

      POST /api/v0.1/credentials HTTP/1.1
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
      Location: /api/v0.1/credentials/sierra

      {
        "id": "sierra",
        "access_key": "sierra_access_key_id",
        "secret_key": "sierra_secret_access_key",
        "key_name": "phantom_ssh_key",
        "uri": "/api/v0.1/credentials/sierra"
      }

   :statuscode 201: credentials saved

.. http:put:: /api/v0.1/credentials/(site_id)

   Update cloud credentials

   **Example request**:

   .. sourcecode:: http

      PUT /api/v0.1/credentials/ec2 HTTP/1.1
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
      Location: /api/v0.1/credentials/ec2

      {
        "id": "ec2",
        "access_key": "updated_aws_access_key_id",
        "secret_key": "updated_aws_secret_access_key",
        "key_name": "phantom_ssh_key",
        "uri": "/api/v0.1/credentials/ec2"
      }

   :statuscode 200: credentials updated

.. http:delete:: /api/v0.1/credentials/(site_id)

   Delete cloud credentials

   **Example request**:

   .. sourcecode:: http

      DELETE /api/v0.1/credentials/ec2 HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No Content
      Content-Type: application/json

   :statuscode 204: credentials deleted


Launch Configuration Resources
==============================

.. http:get:: /api/v0.1/launchconfigurations

   List all launch configurations for the authenticated user

   **Example request**:

   .. sourcecode:: http

      GET /api/v0.1/launchconfigurations HTTP/1.1
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
          "uri": "/api/v0.1/launchconfigurations/myfirstlc"
        }
      ]

   :statuscode 200: no error

.. http:post:: /api/v0.1/launchconfigurations

   Create a new launch configuration

   **Example request**:

   .. sourcecode:: http

      POST /api/v0.1/launchconfigurations HTTP/1.1
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
      Location: /api/v0.1/launchconfigurations/mysecondlc

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
        "uri": "/api/v0.1/launchconfigurations/mysecondlc"
      }

   :statuscode 201: launch configuration created

.. http:put:: /api/v0.1/launchconfigurations/(launch_configuration_id)

   Update a launch configuration

   **Example request**:

   .. sourcecode:: http

      PUT /api/v0.1/launchconfigurations/mysecondlc HTTP/1.1
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
      Location: /api/v0.1/launchconfigurations/mysecondlc

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
        "uri": "/api/v0.1/launchconfigurations/mysecondlc"
      }

   :statuscode 200: launch configuration updated

.. http:delete:: /api/v0.1/launchconfigurations/(launch_configuration_id)

   Delete a launch configuration

   **Example request**:

   .. sourcecode:: http

      DELETE /api/v0.1/launchconfigurations/myfirstlc HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No Content
      Content-Type: application/json

   :statuscode 204: launch configuration deleted


Domain Resources
================

.. http:get:: /api/v0.1/domains

   List all domains for the authenticated user

   **Example request**:

   .. sourcecode:: http

      GET /api/v0.1/domains HTTP/1.1
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
          "lc_name": "myfirstlc",
          "vm_count": 1,
          "uri": "/api/v0.1/domains/myfirstdomain"
        }
      ]

   :statuscode 200: no error

.. http:post:: /api/v0.1/domains

   Create a new domain

   **Example request**:

   .. sourcecode:: http

      POST /api/v0.1/domains HTTP/1.1
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
      Location: /api/v0.1/domains/myseconddomain

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
        "uri": "/api/v0.1/domains/myseconddomain"
      }

   :statuscode 201: domain created

.. http:put:: /api/v0.1/domains/(domain_id)

   Update a domain

   **Example request**:

   .. sourcecode:: http

      PUT /api/v0.1/domains/mysecondomain HTTP/1.1
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
      Location: /api/v0.1/domains/myseconddomain

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
        "sensor_cooldown": 60,
        "uri": "/api/v0.1/domains/myseconddomain"
      }

   :statuscode 200: domain updated

.. http:delete:: /api/v0.1/domains/(domain_id)

   Terminate a domain

   **Example request**:

   .. sourcecode:: http

      DELETE /api/v0.1/domains/myfirstdomain HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No Content
      Content-Type: application/json

   :statuscode 204: domain terminated
