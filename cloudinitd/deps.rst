========================
cloudinit.d Dependencies
========================

The document explains how cloudinit.d sends dependency information from
lower level services to higher level services which depend on them.  All
communication links from cloudinit.d to the machines (or virtual machines)
that host the services are formed with SSH.  The dependency information is
distributed via these links.

Specifying a Dependency
=======================

There are two values in the level configuration file that are needed to 
set services dependencies.

.. code-block:: none

    bootconf: <a path to a json file>
    deps: <a path to a ini file>

The deps file should contain a single section called [deps].  Each entry in
that section is a user defined key value pair.  The key is a unique name 
that can be referenced by the bootpgm and readypgm and by higher level 
services as well.  

The bootconf file is a json formatted file that allows the user to assemble
variables into a format that the services bootpgm/readypgm can process.
Variable substitution is performed on this file by processing both the 
deps file, and all lower level services dep files if they were specified.
The variable format is:

.. code-block:: none

    ${<service name>.<variable key>}

If no service name is specified then the local service is assumed.  This 
json file template will be filled out and copied to the /tmp directory
of the service's host machine next to the bootpgm program in a file called
bootconf.json.  Similarly, a file called bootenv.sh is copied to the same
directory.  The bootenv.sh is a series of lines that set bash environment
variables.  Both of these files are there for the bootpgm program to open
and process.  In this way the dependency information is propagated to all
the services.


WordPress Example
=================

To illustrate how to setup up dependency information we will look back at the
:wordpress: example.  In this example two VMs are created.  The first runs
a MySQL data base, and the second runs an web server and connects to that 
web server.  In order for the web server to connect to the MySQL server it
needs the following information:

.. code-block:: none

    database name
    database username
    database password
    database hostname

In order for the web server to look up this information the MySQL service
must export it.  This is done with a 'deps' file.  If we look at the 
wordpress example we see the file mysql_deps.conf:

.. code-block:: none

    [deps]
    dbname: wordpress
    dbuser: root
    dbpassword: monkey

This information is used by the MySQL service when configuring itself, but 
it is also added to the 'attribute bag' of the service itself.  This allows
the information to be discovered by higher level services.

If we look in the wordpress services dep file we see:

.. code-block:: none

    [deps]
    mysql_dbname: ${mysql.dbname}
    mysql_dbuser: ${mysql.dbuser}
    mysql_dbpassword: ${mysql.dbpassword}
    mysql_dbhost: ${mysql.hostname}

Just like in the MySQL service, this adds values to the services 'attribute
bag' which can be used this service to configure itself.  The difference here
is that the values of the service are variables.  Here we see that cloudinit.d
is told to find the service named 'mysql', and ask it for the values
dbname, dbuser, dbpassword, and hostname.

This information is sent to the hosting machine in the same directory as
the bootpgm.  The directory is /tmp/nimbusready/<service name>/.  As part
of the boot process the following 3 files are added:

    * bootconf.json : A JSON formatted file with all the attributes are key/value pairs
    * bootenv.sh : A series of export <key>="<value>" pairs
    * bootpgm : an executable script that can read the above two files


The wordpress bootpgm opens the json file (it could work with the bootenv.sh
file instead if it were more convenient) and extracts all the values
needed to configure the wordpress service to connect to the MySQL data base.

The bootconf.json file looks like this when expanded:

.. code-block:: none

    {"dbpassword": "monkey", "dbuser": "root", "dbname": "wordpress"}

The bootenv.sh file looks like this when expanded:

.. code-block:: none

    export dbuser="root"
    export dbname="wordpress"
    export dbpassword="monkey"


