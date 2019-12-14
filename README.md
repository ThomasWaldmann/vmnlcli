![velomobiel.nl QuattroVelo](https://gallery.welmers.net/main.php?g2_view=core.DownloadItem&g2_itemId=47348)

# vmnlcli

This is a command line interface for the http://www.velomobiel.nl/ website.

Using it, you can script updating / publishing your velomobile's odometer value (overall km distance of your velomobile),
so you do not need to manually log in / fill out a form / log out.


## Installation

You need to have Python >= 3.5 installed.
See https://www.python.org/ if you don't have it already.

On a shell (linux terminal, windows cmd.exe), enter this to install the vmnlcli software:

    pip3 install vmnlcli         # system-wide installation, might require root/admin
    or
    pip3 install --user vmnlcli  # install into user's home/profile directory

Only once, you need to find out the VMID (internal numerical identifier of velomobiel.nl for your velomobile):

    vmnlcli --email 'you@example.org' --password 'CarsS*ck' vmid

Let's assume it displayed that your VMID is 12345678.

Now you can write 2 small wrapper scripts (they slightly differ for linux vs. windows).

### Linux wrapper scripts

#### myvm-now-km

    vmnlcli --email 'you@example.org' --password 'CarsS*ck' --vmid 12345678 update $1

#### myvm-date-km

    vmnlcli --email 'you@example.org' --password 'CarsS*ck' --vmid 12345678 update --date $1 $2

### Windows wrapper scripts

#### myvm-now-km.cmd

    vmnlcli --email 'you@example.org' --password 'CarsS*ck' --vmid 12345678 update %1

#### myvm-date-km.cmd

    vmnlcli --email 'you@example.org' --password 'CarsS*ck' --vmid 12345678 update --date %1 %2

## Usage

You just came home, odometer showed 4321 km and you want to update the site:

    myvm-now-km 4321

Or, you noted that your odometer showed 4321 km at 2019-12-31 and you want to update the site with that:

    myvm-date-km 2019-12-31 4321
