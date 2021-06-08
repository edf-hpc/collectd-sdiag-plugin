#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright (C) 2021 EDF SA
#
# This file is part of collectd-sdiag-plugin
#
# collectd-sdiag-plugin is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# collectd-sdiag-plugin is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with collectd-sdiag-plugin.  If not, see
# <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

# get __version__
exec(open('collectd_sdiag/version.py').read())

setup(name='collectd_sdiag',
      version=__version__,
      packages=find_packages(),
      scripts=['scripts/sdiag_stats.py'],
      author='EDF CCN-HPC',
      author_email='dsp-cspite-ccn-hpc@edf.fr',
      license='CeCILL v2.1',
      url='http://edf-hpc.github.io/collectd-sdiag-plugin',
      download_url='http://github.com/edf-hpc/collectd-sdiag-plugin/',
      platforms=['GNU/Linux', 'BSD'],
      keywords=['hpc', 'supercomputers', 'jobs', 'slurm'],
      install_requires=['pyslurm'],
      description="Collectd SLURM sdiag plugin",
      classifiers=[
          "Environment :: Console",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: System :: Clustering",
          "Topic :: System :: Distributed Computing"
      ]
     )
