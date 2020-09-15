#!/usr/bin/env python

from __future__ import print_function, absolute_import


_memory_from_revision = [
    'Unkonwn',
    'Unkonwn',
    256,
    256,
    256,
    256,
    256,
    256,
    256,
    256,
    'Unkonwn',
    'Unkonwn',
    512,
    512,
    512,
    512,
    512,
    256,
    512,
    512,
    256,
]

_type_from_revision = [
    'Unknown',
    'Unknown',
    'Model B',
    'Model B',
    'Model B',
    'Model B',
    'Model B',
    'Model A',
    'Model A',
    'Model A',
    'Unknown',
    'Unknown',
    'Unknown',
    'Model B',
    'Model B',
    'Model B',
    'Model B+',
    'Computer Module',
    'Model A+',
    'Model B+',
    'Computer Module',
    'Model A+',
]

_manufacturer_from_revision = [
    'UNKNOWN',
    'UNKNOWN',
    'UNKNOWN',
    'UNKNOWN',
    'SONY',
    'QISDA',
    'EGOMAN',
    'EGOMAN',
    'SONY',
    'QISDA',
    'UNKNOWN',
    'UNKNOWN',
    'UNKNOWN',
    'EGOMAN',
    'SONY',
    'QISDA',
    'SONY',
    'SONY',
    'SONY',
    'EMBEST',
    'SONY',
    'SONY',
]

_pcb_from_revision = [
    0,
    0,
    1,
    1,
    2,
    2,
    2,
    2,
    2,
    2,
    0,
    0,
    0,
    2,
    2,
    2,
    1,
    1,
    1,
    1,
    1,
    1,
]

_model_from_revision = [
    'Unknown',
    'Unknown',
    'B',
    'B',
    'B',
    'B',
    'B',
    'A',
    'A',
    'A',
    'Unknown',
    'Unknown',
    'Unknown',
    'B',
    'B',
    'B',
    'B+',
    'Computer Module',
    'A+',
    'B+',
    'Computer Module',
    'MA+',
]

_version_from_revision = [
    'Unknown',
    'Unknown',
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    'Unknown',
    'Unknown',
    'Unknown',
    1,
    1,
    1,
    1,
    'Computer Module',
    1,
    1,
    'Computer Module',
    1,
]

_memory = [256, 512, 1024, 2048, 4096]

_manufacturer = ['SONY', 'EGOMAN', 'EMBEST', 'SONY JAPAN', 'EMBEST', 'STADIUM']

_processor = [2835, 2836, 2837, 2711]

_type = [
    'Model A',
    'Model B',
    'Model A+',
    'Model B+',
    'Model 2B',
    'Alpha',
    'Compute Module 1',
    'Unknown',
    'Model 3B',
    'Model Zero',
    'Compute Module 3',
    'Unknown',
    'Zero W',
    'Model 3B+',
    'Model 3A+',
    'Internal',
    'Compute Module 3+',
    'Model 4B',
]

_model = [
    'A',
    'B',
    'A',
    'B',
    'B',
    'Alpha',
    'Compute Module',
    'Unknown',
    'B',
    'Zero',
    'Compute Module',
    'Unknown',
    'Zero W',
    '3B+',
    '3A+',
    'Internal',
    '3+',
    '4B',
]

_version = [
    1,
    1,
    1,
    1,
    2,
    'Unknown',
    'Unknown',
    'Unknown',
    3,
    'Zero',
    3,
    'Unknown',
    'Zero W',
    3,
    3,
    'Unknown',
    3,
    4,
]

_cpuinfo = open('/proc/cpuinfo').read()

# Strip tabs
_cpuinfo = _cpuinfo.replace("\t", "")

# Turn into list at return
_cpuinfo = _cpuinfo.split("\n")

# Filter empty strings
_cpuinfo = list(filter(len, _cpuinfo))

# Split into key/value dict
_cpuinfo = dict(item.split(": ") for item in _cpuinfo)

# Convert revision string to integer
_revision = int(_cpuinfo['Revision'], 16)

# Bit field:
"""
11000000000000000000000000 = 0x3000000 = WARANTY 
00100000000000000000000000 = 0x0800000 = SCHEME
00011100000000000000000000 = 0x0700000 = MEMORY
00000011110000000000000000 = 0x00F0000 = MANUFACTURER
00000000001111000000000000 = 0x000F000 = CPU
00000000000000111111110000 = 0x0000FF0 = MODEL
00000000000000000000001111 = 0x000000F = PCB
"""

# Determine scheme
_scheme = (_revision & 0x800000) >> 23

warranty = "N/A"
memory = "N/A"
manufacturer = "N/A"
processor = "N/A"
board_type = "N/A"
model = "N/A"
version = "N/A"
pcb_revision = "N/A"
info = {}

if _scheme:

    warranty = int((_revision & 0x3000000) >> 24) > 0

    memory = _memory[(_revision & 0x700000) >> 20]

    manufacturer = _manufacturer[(_revision & 0xF0000) >> 16]

    processor = _processor[(_revision & 0xF000) >> 12]

    board_type = _type[(_revision & 0xFF0) >> 4]

    version = _version[(_revision & 0xFF0) >> 4]

    model = _model[(_revision & 0xFF0) >> 4]

    pcb_revision = _revision & 0xF

else:
    warranty = int((_revision & 0x40) >> 7) > 0

    memory = _memory_from_revision[_revision]

    manufacturer = _manufacturer_from_revision[_revision]

    board_type = _type_from_revision[_revision]

    version = _version_from_revision[_revision]

    model = _model_from_revision[_revision]

    pcb_revision = _pcb_from_revision[_revision]

info = {
    'memory': memory,
    'manufacturer': manufacturer,
    'processor': processor,
    'type': board_type,
    'revision': _cpuinfo['Revision'],
    'pcb_revision': pcb_revision,
    'model': model,
    'version': version,
    'warranty': warranty
}


def main():
    print("""---- Raspberry Pi Info ----
Type:\t\t{type}
Model:\t\t{model}
Version:\t{version}
RAM:\t\t{memory}
CPU:\t\t{processor}
Manufacturer:\t{manufacturer}
PCB Revision:\t{pcb_revision}
Revision:\t{revision}
Void warranty:\t{warranty}
---------------------------
""".format(**info))


if __name__ == '__main__':
    main()
