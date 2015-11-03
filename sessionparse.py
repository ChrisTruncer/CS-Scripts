#!/usr/bin/env python

# Author: Chris Truncer (@ChrisTruncer)
# Version 0.1
# parser for sessions.tsv output

import argparse
import glob
import sys


def cli_parser():
    parser = argparse.ArgumentParser(
        add_help=False, description="This script parses sessions.tsv files from Cobalt Strike")
    parser.add_argument('-h', '-?', '--h', '-help',
                        '--help', action="store_true", help=argparse.SUPPRESS)

    options = parser.add_argument_group('Parsing Options')
    options.add_argument(
        '-d', '--directory', default=None, metavar="/tmp/directory",
        help="Directory containing exported sessions.tsv files")
    options.add_argument(
        '-o', '--output', default=False, metavar="outputfile.csv",
        help='Optional CSV file for saving output')
    options.add_argument(
        '--ip', default="n/a", metavar='8.8.8.8',
        help='IP Address of C2 Server')
    options.add_argument(
        '--domain', default="n/a", metavar="totallylegit.com",
        help='C2 Domain')
    options.add_argument(
        '--dates', default="n/a", metavar="\"10/22 - 10/25\"",
        help='Dates team server is used')

    args = parser.parse_args()

    if args.h:
        parser.print_help()
        sys.exit()

    if args.d is None:
        print "[*] Error: -d/--directory option is required to point to\
            session.tsv files!"
        print "[*] Error: Please re-run and provide this option!"
        sys.exit(1)

    # Check to make sure it ends with a forward slash
    if args.directory.endswith('/'):
        pass
    else:
        args.directory = args.directory + '/'

    return args

cli_args = cli_parser()

session_files = []
systems = {}

# Find all .tsv files in the provided directory
for name in glob.glob(cli_args.directory + '*.tsv'):
    session_files.append(name)

if len(session_files) == 0:
    print "[*] Error: You didn't provide the correct directory containing tsv files!"
    print "[*] Error: Please re-run and provide the correct directory!"
    sys.exit(1)

try:
    # Loop over all .tsv session files, read them in, and prep for parsing
    for session_file in session_files:

        with open(session_file, 'r') as open_session_file:
            sessions_lines = open_session_file.readlines()

        for line in sessions_lines:
            if 'internal' and 'computer' in line:
                pass
            else:
                systems[line.split('\t')[3]] = line.split('\t')[5]

    for ip, fqdn in systems.iteritems():
        if not cli_args.output:
            print ip + ',' + fqdn + ',' + cli_args.ip + ',' +\
                cli_args.domain + ',' + cli_args.dates
        else:
            with open(cli_args.output, 'a') as csv_output:
                csv_output.write(
                    ip + ',' + fqdn + ',' + cli_args.ip + ',' +
                    cli_args.domain + ',' + cli_args.dates + '\n')

except IndexError:
    print "[*] Error: Could not parse tsv files!"
    print "[*] Error: Please ensure you are using session.tsv files!"
    sys.exit(1)
