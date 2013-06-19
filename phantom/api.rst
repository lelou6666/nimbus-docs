=======================
Nimbus Phantom HTTP API
=======================

.. contents::
    :local:

Authentication and Tokens
=========================

The Phantom API uses tokens and Basic Authentication for authentication. Users
must request a token to access most endpoints in the API.

.. http:post:: /api/v1.0/token

   Get the user's token.

   :statuscode 200: no error

   **Example request**:

   .. sourcecode:: http

      POST /api/v1.0/token HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

      {
        "username": "alice",
        "password": "restaurant",
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "token": "xgy-4h324h2i4h32oi4h23",
        "user": 1,
        "success": true
      }

All other requests must be authenticated using this token. To use this token with curl, 
for example:

   .. sourcecode:: none

      $ curl -d "username=alice&password=restaurant" http://phantom.nimbusproject.org/api/dev/token
      {"token": "xgy-4h324h2i4h32oi4h23", "user": 1, "success": true}

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


Site Resources
==============

.. http:get:: /api/v1.0/sites

   List all clouds known to the authenticated user, and their details

   :statuscode 200: no error
   :query details: either ``true`` or ``false``. If ``true``, you will get extra details, but responses with details take longer to return.

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
          "instance_types": [
            "m1.small",
            "m1.large",
            "m1.xlarge"
          ],
          "uri": "/api/v1.0/sites/ec2"
        },
        {
          "id": "hotel",
          "credentials": "/api/v1.0/credentials/hotel",
          "instance_types": [
            "m1.small",
            "m1.large",
            "m1.xlarge"
          ],
          "uri": "/api/v1.0/sites/hotel"
        },
        {
          "id": "sierra",
          "credentials": "/api/v1.0/credentials/sierra",
          "instance_types": [
            "m1.small",
            "m1.large",
            "m1.xlarge"
          ],
          "uri": "/api/v1.0/sites/sierra"
        }
      ]

   **Example request**:

   .. sourcecode:: http

      GET /api/v1.0/sites?details=true HTTP/1.1
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
          "instance_types": [
            "m1.small",
            "m1.large",
            "m1.xlarge"
          ],
          "public_images": [
            "centos-5.5-x64-vine.gz",
            "hello-cloud",
          ],
          "user_images": [
            "myimage",
          ],
          "uri": "/api/v1.0/sites/ec2"
        },
        {
          "id": "hotel",
          "credentials": "/api/v1.0/credentials/hotel",
          "instance_types": [
            "m1.small",
            "m1.large",
            "m1.xlarge"
          ],
          "public_images": [
            "centos-5.5-x64-vine.gz",
            "hello-cloud",
          ],
          "user_images": [
            "myimage",
          ],
          "uri": "/api/v1.0/sites/hotel"
        },
        {
          "id": "sierra",
          "credentials": "/api/v1.0/credentials/sierra",
          "instance_types": [
            "m1.small",
            "m1.large",
            "m1.xlarge"
          ],
          "public_images": [
            "centos-5.5-x64-vine.gz",
            "hello-cloud",
          ],
          "user_images": [
            "myimage",
          ],
          "uri": "/api/v1.0/sites/sierra"
        }
      ]

.. http:get:: /api/v1.0/sites/(cloud_id)

   Get details for the cloud `cloud_id`

   :statuscode 200: no error
   :statuscode 404: cloud is unknown
   :query details: either ``true`` or ``false``. If ``true``, you will get extra details, but responses with details take longer to return.

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
        "instance_types": [
          "m1.small",
          "m1.large",
          "m1.xlarge"
        ],
        "credentials": "/api/v1.0/credentials/hotel",
        "uri": "/api/v1.0/sites/hotel"
      }

   **Example request**:

   .. sourcecode:: http

      GET /api/v1.0/sites/hotel?details=true HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "id": "hotel",
        "instance_types": [
          "m1.small",
          "m1.large",
          "m1.xlarge"
        ],
        "public_images": [
          "centos-5.5-x64-vine.gz",
          "hello-cloud",
        ],
        "user_images": [
          "myimage",
        ],
        "credentials": "/api/v1.0/credentials/hotel",
        "uri": "/api/v1.0/sites/hotel"
      }


Credentials Resources
=====================

.. http:get:: /api/v1.0/credentials

   List all cloud credentials for the authenticated user

   :statuscode 200: no error
   :query details: either ``true`` or ``false``. If ``true``, you will get extra details, but responses with details take longer to return.

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

   **Example request**:

   .. sourcecode:: http

      GET /api/v1.0/credentials?details=true HTTP/1.1
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
          "available_keys": [
            "phantom_ssh_key",
            "default"
          ],
          "key_name": "phantom_ssh_key",
          "uri": "/api/v1.0/credentials/ec2"
        },
        {
          "id": "hotel",
          "access_key": "hotel_access_key_id",
          "secret_key": "hotel_secret_access_key",
          "available_keys": [
            "phantom_ssh_key",
            "default"
          ],
          "key_name": "phantom_ssh_key",
          "uri": "/api/v1.0/credentials/hotel"
        }
      ]

.. http:get:: /api/v1.0/credentials/(cloud_id)

   Get cloud credentials for the cloud `cloud_id`

   :statuscode 200: no error
   :statuscode 404: cloud is unknown
   :query details: either ``true`` or ``false``. If ``true``, you will get extra details, but responses with details take longer to return.

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

   **Example request**:

   .. sourcecode:: http

      GET /api/v1.0/credentials/hotel?details=true HTTP/1.1
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
        "available_keys": [
          "default",
          "phantom_ssh_key"
        ],
        "uri": "/api/v1.0/credentials/hotel"
      }

.. http:post:: /api/v1.0/credentials

   Save new cloud credentials

   :jsonparameter id: ID of the cloud
   :jsonparameter access_key: the access key ID for this cloud
   :jsonparameter secret_key: the secret access key for this cloud
   :jsonparameter key_name: the SSH key pair that will be used on this cloud
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

   List all launch configurations known to the authenticated user

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
          "id": "fcfe9272-d03f-48e4-bd5f-4eb50ec396c7",
          "name": "myfirstlc",
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
            },
          },
          "owner": "johndoe",
          "uri": "/api/v1.0/launchconfigurations/fcfe9272-d03f-48e4-bd5f-4eb50ec396c7"
        }
      ]

.. http:get:: /api/v1.0/launchconfigurations/(launchconfiguration_id)

   Get details for the launch configuration `launch_configuration_id`

   :statuscode 200: no error
   :statuscode 404: launch configuration is unknown

   **Example request**:

   .. sourcecode:: http

      GET /api/v1.0/launchconfigurations/fcfe9272-d03f-48e4-bd5f-4eb50ec396c7 HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "id": "fcfe9272-d03f-48e4-bd5f-4eb50ec396c7",
        "name": "myfirstlc",
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
        "owner": "johndoe",
        "uri": "/api/v1.0/launchconfigurations/fcfe9272-d03f-48e4-bd5f-4eb50ec396c7"
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
        "name": "mysecondlc",
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
      Location: /api/v1.0/launchconfigurations/e99be9d3-8f09-4a6c-bb17-b00efd0d06df

      {
        "id": "e99be9d3-8f09-4a6c-bb17-b00efd0d06df",
        "name": "mysecondlc",
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
        "owner": "johndoe",
        "uri": "/api/v1.0/launchconfigurations/e99be9d3-8f09-4a6c-bb17-b00efd0d06df"
      }

.. http:put:: /api/v1.0/launchconfigurations/(launch_configuration_id)

   Update a launch configuration

   :statuscode 200: launch configuration updated

   **Example request**:

   .. sourcecode:: http

      PUT /api/v1.0/launchconfigurations/e99be9d3-8f09-4a6c-bb17-b00efd0d06df HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

      {
        "name": "mysecondlc",
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
      Location: /api/v1.0/launchconfigurations/e99be9d3-8f09-4a6c-bb17-b00efd0d06df

      {
        "id": "e99be9d3-8f09-4a6c-bb17-b00efd0d06df",
        "name": "mysecondlc",
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
        "owner": "johndoe",
        "uri": "/api/v1.0/launchconfigurations/e99be9d3-8f09-4a6c-bb17-b00efd0d06df"
      }

.. http:delete:: /api/v1.0/launchconfigurations/(launch_configuration_id)

   Delete a launch configuration

   :statuscode 204: launch configuration deleted

   **Example request**:

   .. sourcecode:: http

      DELETE /api/v1.0/launchconfigurations/fcfe9272-d03f-48e4-bd5f-4eb50ec396c7 HTTP/1.1
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
          "id": "1f8112a3-4abd-4629-a1b5-33f78cff504a",
          "name": "myfirstdomain",
          "de_name": "multicloud",
          "monitor_sensors": "",
          "monitor_domain_sensors": "my.domain.sensor",
          "launchconfiguration": "/api/v1.0/launchconfigurations/fcfe9272-d03f-48e4-bd5f-4eb50ec396c7",
          "vm_count": 1,
          "sensor_data": {
            "my.domain.sensor": {
              "series": [0.0],
              "average": 0.0
            }
          },
          "owner": "johndoe",
          "uri": "/api/v1.0/domains/1f8112a3-4abd-4629-a1b5-33f78cff504a"
        }
      ]

.. http:get:: /api/v1.0/domains/(domain_id)

   Get details for the domain `domain_id`

   :statuscode 200: no error
   :statuscode 404: domain is unknown

   **Example request**:

   .. sourcecode:: http

      GET /api/v1.0/domains/1f8112a3-4abd-4629-a1b5-33f78cff504a HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "id": "1f8112a3-4abd-4629-a1b5-33f78cff504a",
        "name": "myfirstdomain",
        "de_name": "multicloud",
        "monitor_sensors": "",
        "monitor_domain_sensors": "my.domain.sensor",
        "launchconfiguration": "/api/v1.0/launchconfigurations/fcfe9272-d03f-48e4-bd5f-4eb50ec396c7",
        "vm_count": 1,
        "sensor_data": {
          "my.domain.sensor": {
            "series": [0.0],
            "average": 0.0
          }
        },
        "owner": "johndoe",
        "uri": "/api/v1.0/domains/1f8112a3-4abd-4629-a1b5-33f78cff504a"
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
        "name": "myseconddomain",
        "de_name": "sensor",
        "lc_name": "mysecondlc",
        "monitor_sensors": "proc.loadavg.1min,df.inodes.free",
        "monitor_domain_sensors": "",
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
      Location: /api/v1.0/domains/bb03986c-ff70-4bc2-baec-10016e5db740

      {
        "id": "bb03986c-ff70-4bc2-baec-10016e5db740",
        "name": "myseconddomain",
        "de_name": "sensor",
        "launchconfiguration": "/api/v1.0/launchconfigurations/e99be9d3-8f09-4a6c-bb17-b00efd0d06df",
        "monitor_sensors": "proc.loadavg.1min,df.inodes.free",
        "monitor_domain_sensors": "",
        "sensor_minimum_vms": 1,
        "sensor_maximum_vms": 10,
        "sensor_metric": "proc.loadavg.1min",
        "sensor_scale_down_threshold": "0.5",
        "sensor_scale_down_vms": 1,
        "sensor_scale_up_threshold": 1,
        "sensor_scale_up_vms": 1,
        "sensor_cooldown": 60
        "owner": "johndoe",
        "uri": "/api/v1.0/domains/bb03986c-ff70-4bc2-baec-10016e5db740"
      }

.. http:put:: /api/v1.0/domains/(domain_id)

   Update a domain

   :statuscode 200: domain updated

   **Example request**:

   .. sourcecode:: http

      PUT /api/v1.0/domains/bb03986c-ff70-4bc2-baec-10016e5db740 HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

      {
        "name": "myseconddomain",
        "de_name": "sensor",
        "lc_name": "mysecondlc",
        "monitor_sensors": "proc.loadavg.1min,df.inodes.free",
        "monitor_domain_sensors": "",
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
      Location: /api/v1.0/domains/bb03986c-ff70-4bc2-baec-10016e5db740

      {
        "id": "bb03986c-ff70-4bc2-baec-10016e5db740",
        "name": "myseconddomain",
        "de_name": "sensor",
        "launchconfiguration": "/api/v1.0/launchconfigurations/e99be9d3-8f09-4a6c-bb17-b00efd0d06df",
        "monitor_sensors": "proc.loadavg.1min,df.inodes.free",
        "monitor_domain_sensors": "",
        "sensor_minimum_vms": 1,
        "sensor_maximum_vms": 5,
        "sensor_metric": "proc.loadavg.1min",
        "sensor_scale_down_threshold": "0.5",
        "sensor_scale_down_vms": 1,
        "sensor_scale_up_threshold": 1,
        "sensor_scale_up_vms": 1,
        "sensor_cooldown": 60,
        "owner": "johndoe",
        "uri": "/api/v1.0/domains/bb03986c-ff70-4bc2-baec-10016e5db740"
      }

.. http:delete:: /api/v1.0/domains/(domain_id)

   Terminate a domain

   :statuscode 204: domain terminated

   **Example request**:

   .. sourcecode:: http

      DELETE /api/v1.0/domains/1f8112a3-4abd-4629-a1b5-33f78cff504a HTTP/1.1
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

      GET /api/v1.0/domains/1f8112a3-4abd-4629-a1b5-33f78cff504a/instances HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      [
        {
          "id": "87554432-f140-4722-86bf-1e3cdb04dcdd",
          "iaas_instance_id": "i-75c0b81b",
          "lifecycle_state": "400-PENDING",
          "hostname": "vm-25.sdsc.futuregrid.org",
          "cloud": "/api/v1.0/sites/sierra",
          "image_id": "hello-phantom.gz",
          "instance_type": "m1.small",
          "sensor_data": {
            "proc.loadavg.1min": {
              "series": [0.0],
              "average": 0.0
            }
          },
          "keyname": "phantomkey",
          "uri": "/api/v1.0/domains/1f8112a3-4abd-4629-a1b5-33f78cff504a/instances/87554432-f140-4722-86bf-1e3cdb04dcdd"
        }
      ]

.. http:get:: /api/v1.0/domains/(domain_id)/instances/(instance_id)

   Get details for the instance `instance_id` attached to the domain `domain_id`

   :statuscode 200: no error
   :statuscode 404: instance is unknown

   **Example request**:

   .. sourcecode:: http

      GET /api/v1.0/domains/1f8112a3-4abd-4629-a1b5-33f78cff504a/instances/87554432-f140-4722-86bf-1e3cdb04dcdd HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "id": "87554432-f140-4722-86bf-1e3cdb04dcdd",
        "iaas_instance_id": "i-75c0b81b",
        "lifecycle_state": "400-PENDING",
        "hostname": "vm-25.sdsc.futuregrid.org",
        "cloud": "/api/v1.0/sites/sierra",
        "image_id": "hello-phantom.gz",
        "instance_type": "m1.small",
        "sensor_data": {
          "proc.loadavg.1min": {
            "series": [0.0],
            "average": 0.0
          }
        },
        "keyname": "phantomkey",
        "uri": "/api/v1.0/domains/1f8112a3-4abd-4629-a1b5-33f78cff504a/instances/87554432-f140-4722-86bf-1e3cdb04dcdd"
      }

.. http:delete:: /api/v1.0/domains/(domain_id)/instances/(instance_id)

   Terminate the instance `instance_id` within the domain `domain_id`

   :statuscode 204: instance terminated

   **Example request**:

   .. sourcecode:: http

      DELETE /api/v1.0/domains/1f8112a3-4abd-4629-a1b5-33f78cff504a/instances/87554432-f140-4722-86bf-1e3cdb04dcdd HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No Content
      Content-Type: application/json


Sensors Resources
=================

Phantom provides a number of sensors that can be used for auto scaling.

.. http:get:: /api/v1.0/sensors

   List all sensors

   :statuscode 200: no error

   **Example request**:

   .. sourcecode:: http

      GET /api/v1.0/sensors HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      [
        {
          "id": "df.1kblocks.free",
          "uri": "/api/v1.0/sensors/df.1kblocks.free"
        },
        {
          "id": "df.1kblocks.total",
          "uri": "/api/v1.0/sensors/df.1kblocks.total"
        },
        {
          "id": "df.1kblocks.used",
          "uri": "/api/v1.0/sensors/df.1kblocks.used"
        }
      ]

.. http:get:: /api/v1.0/sensors/(sensor_id)

   Get the sensor resource identified by `sensor_id`

   :statuscode 200: no error
   :statuscode 404: sensor is unknown

   **Example request**:

   .. sourcecode:: http

      GET /api/v1.0/sensors/df.1kblocks.free HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "id": "df.1kblocks.free",
        "uri": "/api/v1.0/sensors/df.1kblocks.free"
      }
