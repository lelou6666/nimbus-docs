=======================
The Phantom HTTP API
=======================

.. contents::
    :local:

Authentication and Tokens
=========================

The Phantom API uses tokens and Basic Authentication for authentication. Users
must request a token to access most endpoints in the API.

.. http:post:: /api/dev/token

   Get the user's token.

   :statuscode 200: no error

   **Example request**:

   .. sourcecode:: http

      POST /api/dev/token HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/x-www-form-urlencoded

      username=alice&password=restaurant

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "token": "xgy-4h324h2i4h32oi4h23",
        "user": 1,
        "success": true
      }

All other requests must be authenticated using this token.

As an example, if the user 'alice' with the password 'restaurant' wants to get her token,
she could do the following with curl:

   .. sourcecode:: none

      $ curl -d "username=alice&password=restaurant" https://phantom.nimbusproject.org/api/dev/token
      {"token": "xgy-4h324h2i4h32oi4h23", "user": 1, "success": true}

Then, to use other endpoints, use this user id and token when querying. You can either include the 
user and token as request parameters in any call to phantom, or you can use the basic access authentication
scheme:

1. Combine user id and token into string "user:token"
2. Encode resulting string using Base64
3. Prepend "Basic " (including the trailing space) to the resulting Base64 encoded string

Curl (and most http libraries) do this automatically for you:

   .. sourcecode:: none

      $ curl -u 1:xgy-4h324h2i4h32oi4h23 https://phantom.nimbusproject.org/api/dev/sites
      []

You can also store your token in ``~/.netrc`` which will be read by some HTTP clients, including Curl:

   .. sourcecode:: none

      machine phantom.nimbusproject.org login 1 password xgy-4h324h2i4h32oi4h23

You can then use the ``-n`` or ``--netrc`` options of Curl:

   .. sourcecode:: none

      $ curl -n https://phantom.nimbusproject.org/api/dev/sites
      []

You can also append `?pretty=true` to any API call, and get pretty printed results.
You should probably only do this when debugging however, as it could decrease your
response time:

   .. sourcecode:: none

      $ curl -n https://phantom.nimbusproject.org/api/dev/sites
      [{"instance_types":["m1.small","m1.large","m1.xlarge"],"uri":"/api/dev/sites/ec2","credentials":"/api/dev/credentials/sites/ec2","id":"ec2"}]
      $ curl -n https://phantom.nimbusproject.org/api/dev/sites?pretty=true
      [
          {
          "instance_types": [
              "m1.small",
              "m1.large",
              "m1.xlarge"
          ],
          "uri": "/api/dev/sites/ec2",
          "credentials": "/api/dev/credentials/sites/ec2",
          "id": "ec2"
          }
      ]


Site Resources
==============

.. http:get:: /api/dev/sites

   List all clouds known to the authenticated user, and their details

   :statuscode 200: no error
   :query details: either ``true`` or ``false``. If ``true``, you will get extra details, but responses with details take longer to return.

   **Example request**:

   .. sourcecode:: http

      GET /api/dev/sites HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      [
        {
          "id": "ec2",
          "credentials": "/api/dev/credentials/sites/ec2",
          "instance_types": [
            "m1.small",
            "m1.large",
            "m1.xlarge"
          ],
          "uri": "/api/dev/sites/ec2"
        },
        {
          "id": "hotel",
          "credentials": "/api/dev/credentials/sites/hotel",
          "instance_types": [
            "m1.small",
            "m1.large",
            "m1.xlarge"
          ],
          "uri": "/api/dev/sites/hotel"
        },
        {
          "id": "sierra",
          "credentials": "/api/dev/credentials/sites/sierra",
          "instance_types": [
            "m1.small",
            "m1.large",
            "m1.xlarge"
          ],
          "uri": "/api/dev/sites/sierra"
        }
      ]

   **Example request**:

   .. sourcecode:: http

      GET /api/dev/sites?details=true HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      [
        {
          "id": "ec2",
          "credentials": "/api/dev/credentials/sites/ec2",
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
          "uri": "/api/dev/sites/ec2"
        },
        {
          "id": "hotel",
          "credentials": "/api/dev/credentials/sites/hotel",
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
          "uri": "/api/dev/sites/hotel"
        },
        {
          "id": "sierra",
          "credentials": "/api/dev/credentials/sites/sierra",
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
          "uri": "/api/dev/sites/sierra"
        }
      ]

.. http:get:: /api/dev/sites/(cloud_id)

   Get details for the cloud `cloud_id`

   :statuscode 200: no error
   :statuscode 404: cloud is unknown
   :query details: either ``true`` or ``false``. If ``true``, you will get extra details, but responses with details take longer to return.

   **Example request**:

   .. sourcecode:: http

      GET /api/dev/sites/hotel HTTP/1.1
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
        "credentials": "/api/dev/credentials/sites/hotel",
        "uri": "/api/dev/sites/hotel"
      }

   **Example request**:

   .. sourcecode:: http

      GET /api/dev/sites/hotel?details=true HTTP/1.1
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
        "credentials": "/api/dev/credentials/sites/hotel",
        "uri": "/api/dev/sites/hotel"
      }


Site Credentials Resources
=====================

.. http:get:: /api/dev/credentials/sites

   List all cloud credentials for the authenticated user

   :statuscode 200: no error
   :query details: either ``true`` or ``false``. If ``true``, you will get extra details, but responses with details take longer to return.

   **Example request**:

   .. sourcecode:: http

      GET /api/dev/credentials/sites HTTP/1.1
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
          "uri": "/api/dev/credentials/sites/ec2"
        },
        {
          "id": "hotel",
          "access_key": "hotel_access_key_id",
          "secret_key": "hotel_secret_access_key",
          "key_name": "phantom_ssh_key",
          "uri": "/api/dev/credentials/sites/hotel"
        }
      ]

   **Example request**:

   .. sourcecode:: http

      GET /api/dev/credentials/sites?details=true HTTP/1.1
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
          "uri": "/api/dev/credentials/sites/ec2"
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
          "uri": "/api/dev/credentials/sites/hotel"
        }
      ]

.. http:get:: /api/dev/credentials/sites/(cloud_id)

   Get cloud credentials for the cloud `cloud_id`

   :statuscode 200: no error
   :statuscode 404: cloud is unknown
   :query details: either ``true`` or ``false``. If ``true``, you will get extra details, but responses with details take longer to return.

   **Example request**:

   .. sourcecode:: http

      GET /api/dev/credentials/sites/hotel HTTP/1.1
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
        "uri": "/api/dev/credentials/sites/hotel"
      }

   **Example request**:

   .. sourcecode:: http

      GET /api/dev/credentials/sites/hotel?details=true HTTP/1.1
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
        "uri": "/api/dev/credentials/sites/hotel"
      }

.. http:post:: /api/dev/sites/credentials

   Save new cloud credentials

   :jsonparameter id: ID of the cloud
   :jsonparameter access_key: the access key ID for this cloud
   :jsonparameter secret_key: the secret access key for this cloud
   :jsonparameter key_name: the SSH key pair that will be used on this cloud
   :statuscode 201: credentials saved

   **Example request**:

   .. sourcecode:: http

      POST /api/dev/sites/credentials HTTP/1.1
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
      Location: /api/dev/credentials/sites/sierra

      {
        "id": "sierra",
        "access_key": "sierra_access_key_id",
        "secret_key": "sierra_secret_access_key",
        "key_name": "phantom_ssh_key",
        "uri": "/api/dev/credentials/sites/sierra"
      }

.. http:put:: /api/dev/credentials/sites/(cloud_id)

   Update cloud credentials

   :statuscode 200: credentials updated

   **Example request**:

   .. sourcecode:: http

      PUT /api/dev/credentials/sites/ec2 HTTP/1.1
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
      Location: /api/dev/credentials/sites/ec2

      {
        "id": "ec2",
        "access_key": "updated_aws_access_key_id",
        "secret_key": "updated_aws_secret_access_key",
        "key_name": "phantom_ssh_key",
        "uri": "/api/dev/credentials/sites/ec2"
      }

.. http:delete:: /api/dev/credentials/sites/(cloud_id)

   Delete cloud credentials for the cloud `cloud_id`

   :statuscode 204: credentials deleted

   **Example request**:

   .. sourcecode:: http

      DELETE /api/dev/credentials/sites/ec2 HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No Content
      Content-Type: application/json


Chef Credentials Resources
=====================

.. http:get:: /api/dev/credentials/chef

   List all chef credentials for the authenticated user

   :statuscode 200: no error

   **Example request**:

   .. sourcecode:: http

      GET /api/dev/credentials/chef HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      [
        {
          "id": "hostedchef",
          "server_url": "https://api.opscode.com/organizations/chefuser",
          "client_name": "chefuser",
          "validation_client_name": "chefuser-validator",
          "client_key": "-----BEGIN RSA PRIVATE KEY-----...",
          "validator_key": "-----BEGIN RSA PRIVATE KEY-----...",
          "uri": "/api/dev/credentials/chef/hostedchef"
        },
        {
          "id": "open_source_chef",
          "server_url": "https://ec2-host.aws.amazon.com",
          "client_name": "admin",
          "validation_client_name": "chef-validator",
          "client_key": "-----BEGIN RSA PRIVATE KEY-----...",
          "validator_key": "-----BEGIN RSA PRIVATE KEY-----...",
          "uri": "/api/dev/credentials/chef/open_source_chef"
        }
      ]

.. http:get:: /api/dev/credentials/chef/(chef_id)

   Get cloud credentials for the chef server `chef_id`

   :statuscode 200: no error
   :statuscode 404: chef server is unknown

   **Example request**:

   .. sourcecode:: http

      GET /api/dev/credentials/chef/hostedchef HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "id": "hostedchef",
        "server_url": "https://api.opscode.com/organizations/chefuser",
        "client_name": "chefuser",
        "validation_client_name": "chefuser-validator",
        "client_key": "-----BEGIN RSA PRIVATE KEY-----...",
        "validator_key": "-----BEGIN RSA PRIVATE KEY-----...",
        "uri": "/api/dev/credentials/chef/hostedchef"
      }

.. http:post:: /api/dev/credentials/chef

   Save new chef credentials

   :jsonparameter id: ID of the chef server
   :jsonparameter server_url: URL of the chef server
   :jsonparameter client_name: The client name of the chef user
   :jsonparameter validation_client_name: The validation client name. Often chef-validator
   :jsonparameter client_key: The RSA Private client key
   :jsonparameter validator_key: The RSA Private validator key
   :statuscode 201: credentials saved

   **Example request**:

   .. sourcecode:: http

      POST /api/dev/credentials/sites HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

      {
        "id": "hostedchef",
        "server_url": "https://api.opscode.com/organizations/chefuser",
        "client_name": "chefuser",
        "validation_client_name": "chefuser-validator",
        "client_key": "-----BEGIN RSA PRIVATE KEY-----...",
        "validator_key": "-----BEGIN RSA PRIVATE KEY-----...",
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 201 Created
      Content-Type: application/json
      Location: /api/dev/credentials/sites/sierra

      {
        "id": "hostedchef",
        "server_url": "https://api.opscode.com/organizations/chefuser",
        "client_name": "chefuser",
        "validation_client_name": "chefuser-validator",
        "client_key": "-----BEGIN RSA PRIVATE KEY-----...",
        "validator_key": "-----BEGIN RSA PRIVATE KEY-----...",
        "uri": "/api/dev/credentials/chef/hostedchef"
      }

.. http:put:: /api/dev/credentials/chef/(chef_id)

   Update chef credentials

   :statuscode 200: credentials updated

   **Example request**:

   .. sourcecode:: http

      PUT /api/dev/credentials/chef/hostedchef HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

      {
        "id": "hostedchef",
        "server_url": "https://api.opscode.com/organizations/chefuser",
        "client_name": "chefuser",
        "validation_client_name": "chefuser-validator",
        "client_key": "-----BEGIN RSA PRIVATE KEY-----...",
        "validator_key": "-----BEGIN RSA PRIVATE KEY-----...",
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json
      Location: /api/dev/credentials/chef/hostedchef

      {
        "id": "hostedchef",
        "server_url": "https://api.opscode.com/organizations/chefuser",
        "client_name": "chefuser",
        "validation_client_name": "chefuser-validator",
        "client_key": "-----BEGIN RSA PRIVATE KEY-----...",
        "validator_key": "-----BEGIN RSA PRIVATE KEY-----...",
        "uri": "/api/dev/credentials/chef/hostedchef"
      }

.. http:delete:: /api/dev/credentials/chef/(cloud_id)

   Delete chef credentials for the chef server `chef_id`

   :statuscode 204: credentials deleted

   **Example request**:

   .. sourcecode:: http

      DELETE /api/dev/credentials/chef/hostedchef HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No Content
      Content-Type: application/json

Launch Configuration Resources
==============================

   Launch Configuration resources are a list of sites in order, and 
   a contextualization method. Phantom currently supports "none", "user_data",
   and "chef".

.. http:get:: /api/dev/launchconfigurations

   List all launch configurations known to the authenticated user

   :statuscode 200: no error

   **Example request**:

   .. sourcecode:: http

      GET /api/dev/launchconfigurations HTTP/1.1
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
            },
            "ec2": {
              "image_id": "ami-deadbeef",
              "instance_type": "m1.small",
              "max_vms": -1,
              "common": false,
              "rank": 2,
            },
          },
          "contextualization_method": "user_data",
          "user_data": "my user data",
          "owner": "johndoe",
          "uri": "/api/dev/launchconfigurations/fcfe9272-d03f-48e4-bd5f-4eb50ec396c7"
        }
      ]

.. http:get:: /api/dev/launchconfigurations/(launchconfiguration_id)

   Get details for the launch configuration `launch_configuration_id`

   :statuscode 200: no error
   :statuscode 404: launch configuration is unknown

   **Example request**:

   .. sourcecode:: http

      GET /api/dev/launchconfigurations/fcfe9272-d03f-48e4-bd5f-4eb50ec396c7 HTTP/1.1
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
          },
          "ec2": {
            "image_id": "ami-deadbeef",
            "instance_type": "m1.small",
            "max_vms": -1,
            "common": false,
            "rank": 2,
          }
        },
        "contextualization_method": "none",
        "owner": "johndoe",
        "uri": "/api/dev/launchconfigurations/fcfe9272-d03f-48e4-bd5f-4eb50ec396c7"
      }

.. http:post:: /api/dev/launchconfigurations

   Create a new launch configuration

   :jsonparameter name: the name of the launch configuration
   :jsonparameter contextualization_method: the contextualization method, 
        currently phantom supports 'none', 'user_data', and 'chef'
   :jsonparameter user_data: data used by the user_data contextualization method
   :jsonparameter chef_runlist: json-encoded list of recipes to be installed on a VM using chef
        for the 'chef' contextualization method
   :jsonparameter chef_attributes: json-encoded dictionary of attributes to be used by chef on a
        VM using chef for the 'chef' contextualization method
   :statuscode 201: launch configuration created

   **Example request**:

   .. sourcecode:: http

      POST /api/dev/launchconfigurations HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

      {
        "name": "mysecondlc",
        "contextualization_method": "chef",
        "chef_runlist": "["recipe1", "recipe2"]",
        "chef_attributes": "{"my": "attribute"}",
        "cloud_params": {
          "hotel": {
            "image_id": "hello-cloud",
            "instance_type": "m1.large",
            "max_vms": -1,
            "common": true,
            "rank": 1,
          }
        }
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 201 Created
      Content-Type: application/json
      Location: /api/dev/launchconfigurations/e99be9d3-8f09-4a6c-bb17-b00efd0d06df

      {
        "id": "e99be9d3-8f09-4a6c-bb17-b00efd0d06df",
        "name": "mysecondlc",
        "contextualization_method": "chef",
        "run_list": "["recipe1", "recipe2"]",
        "attributes": "{"my": "attribute"}",
        "cloud_params": {
          "hotel": {
            "image_id": "hello-cloud",
            "instance_type": "m1.large",
            "max_vms": -1,
            "common": true,
            "rank": 1,
          }
        },
        "owner": "johndoe",
        "uri": "/api/dev/launchconfigurations/e99be9d3-8f09-4a6c-bb17-b00efd0d06df"
      }

.. http:put:: /api/dev/launchconfigurations/(launch_configuration_id)

   Update a launch configuration

   :statuscode 200: launch configuration updated

   **Example request**:

   .. sourcecode:: http

      PUT /api/dev/launchconfigurations/e99be9d3-8f09-4a6c-bb17-b00efd0d06df HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

      {
        "name": "mysecondlc",
        "contextualization_method": "user_data",
        "user_data": "Hello World"
        "cloud_params": {
          "hotel": {
            "image_id": "hello-cloud",
            "instance_type": "m1.large",
            "max_vms": 5,
            "common": true,
            "rank": 1,
          }
        }
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json
      Location: /api/dev/launchconfigurations/e99be9d3-8f09-4a6c-bb17-b00efd0d06df

      {
        "id": "e99be9d3-8f09-4a6c-bb17-b00efd0d06df",
        "name": "mysecondlc",
        "contextualization_method": "none"
        "cloud_params": {
          "hotel": {
            "image_id": "hello-cloud",
            "instance_type": "m1.large",
            "max_vms": 5,
            "common": true,
            "rank": 1,
          }
        },
        "owner": "johndoe",
        "uri": "/api/dev/launchconfigurations/e99be9d3-8f09-4a6c-bb17-b00efd0d06df"
      }

.. http:delete:: /api/dev/launchconfigurations/(launch_configuration_id)

   Delete a launch configuration

   :statuscode 204: launch configuration deleted

   **Example request**:

   .. sourcecode:: http

      DELETE /api/dev/launchconfigurations/fcfe9272-d03f-48e4-bd5f-4eb50ec396c7 HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No Content
      Content-Type: application/json


Domain Resources
================

.. http:get:: /api/dev/domains

   List all domains for the authenticated user

   :statuscode 200: no error

   **Example request**:

   .. sourcecode:: http

      GET /api/dev/domains HTTP/1.1
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
          "launchconfiguration": "/api/dev/launchconfigurations/fcfe9272-d03f-48e4-bd5f-4eb50ec396c7",
          "vm_count": 1,
          "sensor_data": {
            "my.domain.sensor": {
              "series": [0.0],
              "average": 0.0
            }
          },
          "owner": "johndoe",
          "uri": "/api/dev/domains/1f8112a3-4abd-4629-a1b5-33f78cff504a"
        }
      ]

.. http:get:: /api/dev/domains/(domain_id)

   Get details for the domain `domain_id`

   :statuscode 200: no error
   :statuscode 404: domain is unknown

   **Example request**:

   .. sourcecode:: http

      GET /api/dev/domains/1f8112a3-4abd-4629-a1b5-33f78cff504a HTTP/1.1
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
        "launchconfiguration": "/api/dev/launchconfigurations/fcfe9272-d03f-48e4-bd5f-4eb50ec396c7",
        "vm_count": 1,
        "sensor_data": {
          "my.domain.sensor": {
            "series": [0.0],
            "average": 0.0
          }
        },
        "owner": "johndoe",
        "uri": "/api/dev/domains/1f8112a3-4abd-4629-a1b5-33f78cff504a"
      }

.. http:post:: /api/dev/domains

   Create a new domain

   :statuscode 201: domain created

   **Example request**:

   .. sourcecode:: http

      POST /api/dev/domains HTTP/1.1
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
      Location: /api/dev/domains/bb03986c-ff70-4bc2-baec-10016e5db740

      {
        "id": "bb03986c-ff70-4bc2-baec-10016e5db740",
        "name": "myseconddomain",
        "de_name": "sensor",
        "launchconfiguration": "/api/dev/launchconfigurations/e99be9d3-8f09-4a6c-bb17-b00efd0d06df",
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
        "uri": "/api/dev/domains/bb03986c-ff70-4bc2-baec-10016e5db740"
      }

.. http:put:: /api/dev/domains/(domain_id)

   Update a domain

   :statuscode 200: domain updated

   **Example request**:

   .. sourcecode:: http

      PUT /api/dev/domains/bb03986c-ff70-4bc2-baec-10016e5db740 HTTP/1.1
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
      Location: /api/dev/domains/bb03986c-ff70-4bc2-baec-10016e5db740

      {
        "id": "bb03986c-ff70-4bc2-baec-10016e5db740",
        "name": "myseconddomain",
        "de_name": "sensor",
        "launchconfiguration": "/api/dev/launchconfigurations/e99be9d3-8f09-4a6c-bb17-b00efd0d06df",
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
        "uri": "/api/dev/domains/bb03986c-ff70-4bc2-baec-10016e5db740"
      }

.. http:delete:: /api/dev/domains/(domain_id)

   Terminate a domain

   :statuscode 204: domain terminated

   **Example request**:

   .. sourcecode:: http

      DELETE /api/dev/domains/1f8112a3-4abd-4629-a1b5-33f78cff504a HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No Content
      Content-Type: application/json


Instances Resources
===================

Each domain can have a number of instances attached to it.

.. http:get:: /api/dev/domains/(domain_id)/instances

   List all instances attached to the domain `domain_id`

   :statuscode 200: no error

   **Example request**:

   .. sourcecode:: http

      GET /api/dev/domains/1f8112a3-4abd-4629-a1b5-33f78cff504a/instances HTTP/1.1
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
          "cloud": "/api/dev/sites/sierra",
          "image_id": "hello-phantom.gz",
          "instance_type": "m1.small",
          "sensor_data": {
            "proc.loadavg.1min": {
              "series": [0.0],
              "average": 0.0
            }
          },
          "keyname": "phantomkey",
          "uri": "/api/dev/domains/1f8112a3-4abd-4629-a1b5-33f78cff504a/instances/87554432-f140-4722-86bf-1e3cdb04dcdd"
        }
      ]

.. http:get:: /api/dev/domains/(domain_id)/instances/(instance_id)

   Get details for the instance `instance_id` attached to the domain `domain_id`

   :statuscode 200: no error
   :statuscode 404: instance is unknown

   **Example request**:

   .. sourcecode:: http

      GET /api/dev/domains/1f8112a3-4abd-4629-a1b5-33f78cff504a/instances/87554432-f140-4722-86bf-1e3cdb04dcdd HTTP/1.1
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
        "cloud": "/api/dev/sites/sierra",
        "image_id": "hello-phantom.gz",
        "instance_type": "m1.small",
        "sensor_data": {
          "proc.loadavg.1min": {
            "series": [0.0],
            "average": 0.0
          }
        },
        "keyname": "phantomkey",
        "uri": "/api/dev/domains/1f8112a3-4abd-4629-a1b5-33f78cff504a/instances/87554432-f140-4722-86bf-1e3cdb04dcdd"
      }

.. http:delete:: /api/dev/domains/(domain_id)/instances/(instance_id)

   Terminate the instance `instance_id` within the domain `domain_id`

   :statuscode 204: instance terminated

   **Example request**:

   .. sourcecode:: http

      DELETE /api/dev/domains/1f8112a3-4abd-4629-a1b5-33f78cff504a/instances/87554432-f140-4722-86bf-1e3cdb04dcdd HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No Content
      Content-Type: application/json


Sensors Resources
=================

Phantom provides a number of sensors that can be used for auto scaling.

.. http:get:: /api/dev/sensors

   List all sensors

   :statuscode 200: no error

   **Example request**:

   .. sourcecode:: http

      GET /api/dev/sensors HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      [
        {
          "id": "df.1kblocks.free",
          "uri": "/api/dev/sensors/df.1kblocks.free"
        },
        {
          "id": "df.1kblocks.total",
          "uri": "/api/dev/sensors/df.1kblocks.total"
        },
        {
          "id": "df.1kblocks.used",
          "uri": "/api/dev/sensors/df.1kblocks.used"
        }
      ]

.. http:get:: /api/dev/sensors/(sensor_id)

   Get the sensor resource identified by `sensor_id`

   :statuscode 200: no error
   :statuscode 404: sensor is unknown

   **Example request**:

   .. sourcecode:: http

      GET /api/dev/sensors/df.1kblocks.free HTTP/1.1
      Host: phantom.nimbusproject.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "id": "df.1kblocks.free",
        "uri": "/api/dev/sensors/df.1kblocks.free"
      }
