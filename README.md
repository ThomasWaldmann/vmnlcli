# vmnlcli.py

This is a command line interface for the velomobiel.nl website.

Using it, you can script updating / publishing your velomobile's odometer value (overall km distance of your velomobile),
so you do not need to manually log in / fill out a form / log out.


## Installation

- you need Python 3.5+
- you need the "requests" python library

  - pip3 install requests  # anywhere
  - apt-get install python3-requests  # debian/ubuntu

Only once, you need to find out the VMID (internal numerical identifier of velomobiel.nl for your velomobile):

    python3 vmnlcli.py --email 'youremail@example.org' --password 'CarsS*ck' vmid

Let's assume it displayed that your VMID is 12345678.

Now you can write 2 small wrapper scripts:

### myvm-now-km

    python3 vmnlcli.py --email 'youremail@example.org' --password 'CarsS*ck' --vmid 12345678 update $1

### myvm-date-km

    python3 vmnlcli.py --email 'youremail@example.org' --password 'CarsS*ck' --vmid 12345678 update --date $1 $2

## Usage

You just came home, odometer showed 4321 km and you want to update the site:

    myvm-now-km 4321

Or, you noted that your odometer showed 4321 km at 2019-12-31 and you want to update the site with that:

    myvm-date-km 2019-12-31 4321

