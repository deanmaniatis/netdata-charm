# Overview

> *New to netdata? Here is a live demo: [http://my-netdata.io](http://my-netdata.io)*

**netdata** is a system for **distributed real-time performance and health monitoring**.
It provides **unparalleled insights, in real-time**, of everything happening on the
system it runs (including applications such as web and database servers), using
**modern interactive web dashboards**.

_netdata is **fast** and **efficient**, designed to permanently run on all systems
(**physical** & **virtual** servers, **containers**, **IoT** devices), without
disrupting their core function._

# Usage

You can install `netdata` to a running unit (e.g. etcd) by issuing:

    juju deploy etcd
    juju deploy netdata
    juju add-relation netdata etcd

You can then browse to `http://ip-address:19999` to view the web user interface of netdata.


# Configuration

netdata comes in two installation flavors, a basic installation (system monitoring and many applications, without `mysql` / `mariadb`, `postgres`, `named`, hardware sensors and `SNMP`) and a full installation monitoring everything that is possible. Currently there is no configuration for opting either and by default the full installation will take place.

# Contact Information
Any bugs/features related to netdata itself should be directed to the upstream project maintainer and any juju related bugs/features to Dean Maniatis <dean.maniatis_at_gmail> or deanman@freenode IRC.

## netdata

- [Upstream website](http://my-netdata.io/)
- [Upstream source code](https://github.com/firehol/netdata)
- [Upstream bug tracker](https://github.com/firehol/netdata/issues)
