=============================
Nimbus Platform Documentation
=============================

Docs are in a "transitional" state for Nimbus right now. Infrastructure docs
live with most of the code in the main nimbus repository. They are HTML+M4.
Docs for some of the Nimbus Platform components live here and are built
using Sphinx. Right now there is:

    cloudinitd/
    ctxbroker/

Each of these is a distinct Sphinx project but they share a common html theme
located in themes/. On the server, these docs are pushed to staticdocs/ in the
EE root directory (/mcs/ee.mcs.anl.gov/nimbus/). The structure of this looks
like:
    cloudinitd/
      1.0/
      latest -> 1.0

    ctxbroker/
      2.8/
      latest -> 2.8

Some PHP is in place in EE to handle wrapping docs into the site skin and to
do URL mangling. So if you for example access /doc/cloudinitd/ you will be
redirected to /doc/cloudinitd/latest/.


-------------
BUILDING DOCS
-------------

To build and push docs, you must have SSH access to the MCS login systems.

You must have fabric available on your Python path, and have Python >=2.5

Use the `nimbusdocs-build-push` tool to build and push doc projects:
    
    Push all doc projects:
    $ bin/nimbusdocs-build-push

    Push specific doc project:
    $ bin/nimbusdocs-build-push cloudinitd

    Check -h for details.


