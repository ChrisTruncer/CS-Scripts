#!/usr/bin/env python

# Author: Chris Truncer (@ChrisTruncer)
# Version 0.1
# parser for sessions.tsv output

with open('pathtofile', 'r') as session_file:
    sessions_lines = session_file.readlines()

systems = {}

for line in sessions_lines:
    if 'internal' and 'computer' in line:
        pass
    else:
        systems[line.split('\t')[3]] = line.split('\t')[5]

for key, value in systems.iteritems():
    print key + ',' + value + ',<teamserverIP>'
