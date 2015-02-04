RPi.version
===========

This library provides a break down of the new 32bit revision bitfield,
detailing the Pi type, origins, amount of memory and CPU details.

Reference
---------

Start with:

    import RPi.version

Processor version:

    RPi.version.processor

Memory amount ( in MB ):

    RPi.version.memory

Raspberry Pi Type:

    RPi.version.type

Manufacturer:

    RPi.version.manufacturer

Revision:

    RPi.version.revision

Pi Model, returns either A, B or CM for Computer Module.

    RPi.version.model

Pi version, returns either 1 or 2 for Pi 2

    RPi.version.version

Info, returns all info as a dictionary

    RPi.version.info
