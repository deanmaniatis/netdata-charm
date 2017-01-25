import subprocess
from charms.reactive import when, when_not
from charms.reactive import set_state, remove_state, is_state
from charmhelpers.core import hookenv, host


@when_not("netdata.installed")
def install_netdata():
    hookenv.status_set('maintenance', 'Installing netdata')
    subprocess.check_call(["/usr/bin/git", "clone", "https://github.com/firehol/netdata.git", "--depth=1"])
    with host.chdir("netdata"):
        subprocess.check_call(["./netdata-installer.sh"])
    hookenv.open_port(19999)
    hookenv.status_set('active', 'Ready')
    set_state("netdata.installed")
