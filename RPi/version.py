#!/usr/bin/env python

_memory = [
    256,
    512,
    1024
]

_manufacturer = [
    'SONY',
    'EGOMAN',
    'EMBEST',
    'UNKNOWN',
    'EMBEST'
]

_processor = [
    2835,
    2836
]

_type = [
    'Model A',
    'Model B',
    'Model A+',
    'Model B+',
    'Model B Pi 2',
    'Alpha',
    'Compute Module'
]

_model = [
    'A',
    'B',
    'A',
    'B',
    'B',
    None,
    'CM'
]

_version = [
     1,
     1,
     1,
     1,
     2,
     1,
     1
]

_cpuinfo = open('/proc/cpuinfo').read()

# Strip tabs
_cpuinfo = _cpuinfo.replace("\t","")

# Turn into list at return
_cpuinfo = _cpuinfo.split("\n")

# Filter empty strings
_cpuinfo = filter(len, _cpuinfo)

# Split into key/value dict
_cpuinfo = dict(item.split(": ") for item in _cpuinfo)

# Convert revision string to integer
_revision = int(_cpuinfo['Revision'],16)

# Determine scheme
_scheme = (_revision & 0x800000) >> 23

memory 		= 0
manufacturer	= None
processor 	= None
type 		= None
model           = None
version         = 0
revision 	= 0
info            = {}

if _scheme:

    memory = _memory[(_revision & 0x700000) >> 20]

    manufacturer = _manufacturer[(_revision & 0xF0000) >> 16]

    processor = _processor[(_revision & 0xF000) >> 12]

    type = _type[(_revision & 0xFF0) >> 4]

    version = _version[(_revision & 0xFF0) >> 4]

    model = _model[(_revision & 0xFF0) >> 4]
    
    revision = (_revision & 0xF)

    info = {
        'memory': memory,
        'manufacturer':  manufacturer,
        'processor': processor,
        'type': type,
        'revision': revision,
        'model': model,
        'revision': revision
    }

if __name__ == "__main__":
    if _scheme:

        print("---- Raspberry Pi Info ----")
        print("Type:\t\t{}".format(type))
        print("RAM:\t\t{}".format(memory))
        print("CPU:\t\t{}".format(processor))
        print("Manufacturer:\t{}".format(manufacturer))
        print("Revision:\t{}".format(revision))
        print("---------------------------")

    else:

        print("Old scheme detected")
        print("Revision: {}".format(revision))

