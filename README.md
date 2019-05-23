# Collectd Slurm stats Python Plugin 
This project contains a Python plugin script for slurm statistics.
The script uses pyslurm library to get statistics data.

- 'sdiags_stats.py': Collect all slurm statistics returned by sdiag utility

## Configuration

Copy the desired Python files to your target system. Then add the module to
your `collectd.conf`. Make sure to adjust the `ModulePath` value. The following
example assumes the plugins were copied to `/opt/collectd_plugins`.

  <LoadPlugin python>
    Globals true
  </LoadPlugin>

  <Plugin python>
    ModulePath "/opt/collectd_plugins"
    Import "sdiag_stats"
    <Module "sdiag_stats">

    </Module>
  </Plugin>

