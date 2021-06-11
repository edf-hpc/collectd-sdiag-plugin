%global debug_package %{nil}
%global pypi_name collectd_sdiag
%global module_name collectd_sdiag
%define version 2.0

Summary: Collectd SLURM sdiag plugin
Name: python3-collectd_sdiag
Version: 2.0
Release: 2%{?dist}.edf
Source0: collectd_sdiag-%{version}.tar.gz
License: GPLv3
Group: Application/System
Prefix: %{_prefix}
Vendor: EDF CCN HPC <dsp-cspito-ccn-hpc@edf.fr>
Url: https://github.com/edf-hpc/%{__name}

%{?python_provide:%python_provide python3-%{module_name}}

Requires: python3dist(pyslurm)
Requires: collectd-python

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
This package provide a Python script that can be used as a Collectd plugin to
collect metrics (scheduling, backfilling, RPC, throughput, etc) about Slurm
workload manager on HPC clusters.

%prep
%autosetup -n %{module_name}-%{version}

%build
%py3_build

%install
%py3_install

%postun
%systemd_postun_with_restart collectd.service

%files
%doc README.md CHANGELOG.md
/usr/bin/sdiag_stats.py
%{python3_sitelib}/%{module_name}
%{python3_sitelib}/%{module_name}-%{version}-py?.?.egg-info

%changelog
* Fri Jun 11 2021 Thomas HAMEL <thomas-t.hamel@edf.fr> - 2.0-2.el8.edf
- Set version in a variable
* Mon Jun 07 2021 Thomas HAMEL <thomas-t.hamel@edf.fr> - 2.0-1.el8.edf
- Initial RPM packaging
