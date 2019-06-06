# Collectd Slurm stats Python Plugin 

## Overview

This project contains a Python script `sdiag_stats.py` that collects all Slurm
workload manager statistics, similarlty to what is returned by `sdiag` CLI
utility provided by Slurm.

This script is designed to be used as a collectd Python plugin and directly
from CLI (mostly for testing purpose).

This Python script relies on PySLURM library to get statistics from Slurm
controller.

## Usage

### CLI

Once the script is deployed on one of your Slurm cluster node (eg. batch
controller), just run the Python script:

```
python sdiag_stats.py
```

### Collectd plugin

Deploy the script on one of your Slurm cluster node (eg. batch controller) in
the directory of your choice (eg. `/opt/collectd/`). Then add the module to
your `collectd.conf`:

```
    LoadPlugin python

    <Plugin python>
       ModulePath "/opt/collectd"
       Import "sdiag_stats"
    </Plugin>
```

Make sure to adjust the `ModulePath` value.

## Licensing

This script is distributed under the terms of the GNU General Public License
version 3, or any later version.
