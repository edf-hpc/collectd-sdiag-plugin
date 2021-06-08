#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2021 EDF SA
#
# Authors: CCN - HPC <dsp-cspit-ccn-hpc@edf.fr>
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

import sys
import collectd_sdiag
debug = False
if len(sys.argv) > 1 and sys.argv[1] == 'debug':
  debug = True
collectd_sdiag.print_metrics(debug)

