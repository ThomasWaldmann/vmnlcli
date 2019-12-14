"""
Command line interface for velomobiel.nl.

(c) 2019 by Thomas Waldmann <twaldmann@thinkmo.de>.
Licensed under the MIT license.
"""

import argparse
import re
import sys
from contextlib import contextmanager

import requests


LOGIN_URL = 'http://en.velomobiel.nl/user/login.php'
DISTANCE_URL = 'http://en.velomobiel.nl/user/kmstand.php'


class Error(Exception):
    """raised in case of internal errors"""


@contextmanager
def login(email, password):
    if not email:
        raise Error('no EMAIL was given, use --email')
    if not password:
        raise Error('no PASSWORD was given, use --password')
    with requests.Session() as session:
        r = session.post(LOGIN_URL, data={'email': email, 'password': password})
        if r.status_code != 200:
            raise Error('got http status %d' % r.status_code)
        yield session


def get_vmid(email, password):
    with login(email, password) as session:
        r = session.get(DISTANCE_URL)
        if r.status_code != 200:
            raise Error('got http status %d' % r.status_code)
        extract_re = re.compile(r"""
            <h3>(?P<vmname>.+?)</h3>
            .*?
            <table
            .*?
            distance_new\[(?P<vmid>\d+)\]
            .*?
            </table>
        """, re.VERBOSE | re.MULTILINE | re.DOTALL)
        for m in extract_re.finditer(r.text):
            vmname = m.group('vmname')
            vmid = int(m.group('vmid'))
            print("%s == vmid %d" % (vmname, vmid))


def put_distance(email, password, vmid, date, distance):
    if not vmid:
        raise Error('no VMID was given, use --vmid')

    with login(email, password) as session:
        yyyy, mm, dd = date.split('-')
        r = session.post(DISTANCE_URL,
                data={
                    'nieuw_datum_jaar[%d]' % vmid: yyyy,
                    'nieuw_datum_maand[%d]' % vmid: mm,
                    'nieuw_datum_dag[%d]' % vmid: dd,
                    'distance_new[%d]' % vmid: str(distance),
                }
        )
        if r.status_code != 200:
            raise Error('got http status %d' % r.status_code)


def create_parser():
    parser = argparse.ArgumentParser(description='velomobiel.nl command line interface')
    parser.add_argument('--verbose', action='store_true', help='more verbose output')
    parser.add_argument('--email', type=str, help='email address to use for logging in')
    parser.add_argument('--password', type=str, help='password to use for logging in')
    parser.add_argument('--vmid', metavar='VMID', type=int, default=0, help='ID of the velomobile')
    subparsers = parser.add_subparsers(dest='cmd')

    help_parser = subparsers.add_parser('help', help='print help')

    update_parser = subparsers.add_parser('update', help='update distance value')
    update_parser.add_argument('--date', metavar='YYYY-MM-DD', type=str, default='YYYY-MM-DD', help='respective date for the overall km value (default: today)')
    update_parser.add_argument('distance', metavar='km', type=int, help='overall km value at the respective date')

    vmid_parser = subparsers.add_parser('vmid', help='show the vm name / vmid')

    return parser


def main(argv=None):
    pure_func_call = argv is not None  # for testing: give argv, get rc returned
    if not pure_func_call:
        argv = sys.argv
    parser = create_parser()
    args = parser.parse_args(argv[1:])
    try:
        if args.cmd == 'vmid':
            get_vmid(args.email, args.password)
        elif args.cmd == 'update':
            put_distance(args.email, args.password, args.vmid, args.date, args.distance)
        else:  # either 'help' or no cmd given
            parser.print_help()
    except Error as err:
        print(str(err))
        rc = 1
    else:
        rc = 0
    if pure_func_call:
        return rc
    else:
        sys.exit(rc)


if __name__ == '__main__':
    main()

