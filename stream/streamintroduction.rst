.. _stream-introduction:

=====================================
Stream Manager Framework Introduction
=====================================

Streams of data have many applications, from real time weather data, to information that is currently trending on services like Twitter, to taking readings from instruments. Handling that data, and managing operations on it, is not as simple, however. Users need to figure out how to keep track of all of their streams, create some method of transforming and analyzing it or even archiving it.

The Stream Management Framework is a tool that makes it simpler to manage and operate on streams of data. It gives you the ability to manage a set of streams, transform them with operations that run on virtual machine instances that you can create, and even archive your streams to systems like Amazon S3.

The framework has two objects that it acts upon:

* *Streams* \- A stream is a queue of messages that are being produced, by a data source or an operation that can be consumed by a consumer application or another operation.
  * *Operations* \- Operations consume an input stream, transform that stream somehow, then push the result to an output stream

These objects are managed by two components, the Stream Manager and the Stream Agent.

The Stream Manager
------------------

  The Stream Manager is the top level component that users interact with to manage their streams. It keeps track of registered streams, the operations that can act on them, and the instances of these operations. It interacts with RabbitMQ to create instances of the streams, ready to begin accepting data and taking subscribers, as well as the Process Dispatcher, which starts instances of the Stream Agent to manage operations on a virtual machine.

The Stream Agent
----------------

  The Stream Agent runs on a virtual machine on behalf of the Stream Manager. When a user begins consuming a stream produced by an operation, the Stream Manager requests an instance of the Stream Agent be started by the Process Dispatcher, which starts an instance of the Agent on a virtual machine, which in turn starts instances of the operation as needed, and then handles taking messages from the input queue, handing them to the operation process, and then takes the output of that process, and puts it on the output stream.

Other Components
----------------

There are another of other components that support the system, including:

The Process Dispatcher
``````````````````````

  The Process Dispatcher takes process requests from the Stream Manager. When the Stream Manager determines that it needs instances of a Stream Agent process, it requests that the process be started by the Process Dispatcher, which in turn requests a new VM to run the stream agent on from Phantom.

  *Learn more.*

Execution Engine Agent
``````````````````````

The Execution Engine Agent runs on the virtual machines started for the Process Dispatcher, and

Phantom
```````

  Phantom is a service that provides auto-scaling and high availability for collections of resources deployed over multiple IaaS cloud providers allowing users to develop scalable and reliable applications.

Getting Started with the Stream Manager
---------------------------------------

  Now that you have an overview of how the system works, you can try :ref:`stream-quickstart`
