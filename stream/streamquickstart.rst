.. _stream-quickstart:

====================================================
Getting Started With the Stream Management Framework
====================================================

Introduction
------------

The Stream Manager and Stream Agent provide a service to manage streams of data, and operations that transform them.

Using the Stream Manager
------------------------

The stream manager includes a few command line tools to manage streams and processes.

The first thing you might want to do is create a stream::

    $ #SYNTAX: ./create_stream.py STREAMNAME
    $ ./create_stream.py mystream

This will cause the stream manager to create a stream. This can be our input stream. We can next create an operation that will act on this stream::

    $ #SYNTAX: ./create_operation.py OPERATIONNAME PROCESS_DEFINITION_ID INPUTSTREAM OUTPUTSTREAM
    $ ./create_operation.py my-operation 5 mystream outputstream

Now that we've created our stream and operation, we can start consuming our output stream::

    $ #SYNTAX ./consume.py STREAMNAME
    $ ./consume.py outputstream

Now we are consuming the output stream. Let's publish something to it::

    $ #SYNTAX ./publish.py STREAMNAME
    $ ./publish.py outputstream
    Some value
    ^C

You should now see the "Some value" text on your consumer. If you want the text transformed, you can see this by publishing to the input stream::

    $ #SYNTAX ./publish.py STREAMNAME
    $ ./publish.py mystream
    Some other text
    ^C

This text will be transformed and the resulting output will be displayed by your consumer.

Streaming Large Data Objects
----------------------------

While streaming on the AMQP bus is reasonable for smaller data, it might not be practical for large data. One option is sending your data objects to an S3 data store and then the stream manager will handle sending the file URL to the stream agent, downloading the file on the local node, and then feeding the contents of that file to the process. To do this::

    $ #SYNTAX ./stream_file.py STREAMNAME BUCKET FILENAME
    $ ./stream_file.py mystream tmpdata myhugefile.dat

This will send the file to S3, send the file URL to the agent, which will download the file, and feed it to the process as if it were regular data on the stream. No special modification is necessary for this to work with your process.

Archiving Streams and Replaying Archived Streams
------------------------------------------------

When managing your streams, you may want a way to save the results of everything that is sent to that stream. The Stream Management Framework includes a tool to archive your stream to S3. To begin archiving your stream, use the archive_stream.py program::

    $ #SYNTAX ./archive_stream.py STREAMNAME
    $ ./archive_stream.py mystream

This will begin saving your stream to an S3 bucket.

If you would like to stream the archived results back to a stream at a later date, you can do this with the stream_archive.py program::

    $ #SYNTAX ./stream_archive.py STREAMNAME
    $ ./stream_archive.py mystream

This will take the archive of the stream, and replay it onto the same stream.

Adapting a Process to Work With the Stream Agent
------------------------------------------------

Stream processes that you would like to use as operations need to be able to take their output from stdin, and put their output on stdout. Any logging or informational messages should go on stderr, otherwise they will be put on your stream output, polluting it.

Your process will be launched by the Stream Agent which will in turn run it, and feed messages from the input stream as stdin, and take output on stdout and feed it to the output stream. Note that the stream agent can invoke your process in two ways: as a single instance per message, or as a long running service that can constantly take stdin and produce stderr.

Single Type Processes
`````````````````````

As an example of a process that you might want to run once for each message::

    $ tr [a-z] [A-Z]

This process will take a string from stdin, and make it uppercase, and put that on stdout.

Another example process that would work well this way: imagemagick::

    $ convert - -resize "50%" -

Or a full example::

    $ cat example.png| convert - -resize "50%" - | display png:-

Service Type Processes
``````````````````````

Other processes should be expected to be long running, and constantly taking input and streaming output. The stream agent will take each message put on the stream and feed it to the process as a new line on stdin, and will take each line of output and feed it onto the output stream as a message. An example python process that replaces instances of the word "pancake" from a text stream with "waffle"::

    import fileinput

    for line in fileinput.input():
        print line.replace("pancake", "waffle")

Building a Stream Operation Appliance
-------------------------------------

A Stream Operation Appliance is a Virtual Machine image with the software to perform a transform operation on a stream. The best way to do this is start from the public "stream-agent" image, and add your software. As an example, using the hotel cloud on FutureGrid::

    $ ./nimbus-cloud-client-021/bin/cloud-client.sh --conf hotel.conf --run --name stream-agent --hours 744
    $ ssh root@the-new-vm.fg.org
    $ #install software, note how to invoke it
    $ ./nimbus-cloud-client-021/bin/cloud-client.sh --conf hotel.conf --common --save --handle vm-xxx --newname my-operation

Now you can create a process definition for this operation. To do so, you can either use the web interface, or use the command line. To use the command line to do this, you must create a process definition. As an example::

    $ cat definition.json
    {
    "definition": {
        "exec": "/opt/my-operation/my-operation.py",
        "application": "my-operation",
        "name": "My Operation"
    }
    }
    $ curl -u username:password -H "Content-Type: application/json" -X POST --data @definition.json http://$PROCESS_REGISTRY_HOST:8081/api/process_definition/

Now you have created a Stream Operation Appliance!

Installing and Running Stream Manager
-------------------------------------

The simplest way to run the stream manager is to run the Stream Manager Appliance on Hotel::

    $ ./nimbus-cloud-client-021/bin/cloud-client.sh --conf hotel.conf --common --run --name stream-manager --hours 744

Next, start up the stream manager services::

    $ ssh root@$STREAM_MANAGER_VM
    # screen -S pd
    # su - epu
    $ /home/epu/app-venv/bin/python /home/epu/app-venv/bin/epu-processdispatcher-service pd.yml
    $ ^A-D
    # screen -S streamboss
    # su - epu
    $ cd streamboss-master
    $ . venv/bin/activate
    $ ./stream_boss.py
    $ ^A-D
