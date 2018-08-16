# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pydefault 3
%else
%global pydefault 2
%endif

%global pydefault_bin python%{pydefault}
%global pydefault_sitelib %python%{pydefault}_sitelib
%global pydefault_install %py%{pydefault}_install
%global pydefault_build %py%{pydefault}_build
# End of macros for py2/py3 compatibility

# guard for package OSP does not support
%global rhosp 0

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           openstack-tripleo-heat-templates
Summary:        Heat templates for TripleO
Version:        XXX
Release:        XXX
License:        ASL 2.0
Group:          System Environment/Base
URL:            https://wiki.openstack.org/wiki/TripleO
Source0:        https://tarballs.openstack.org/tripleo-heat-templates/tripleo-heat-templates-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{pydefault}-devel
BuildRequires:  python%{pydefault}-setuptools
BuildRequires:  python%{pydefault}-pbr
%if %{pydefault} == 2
BuildRequires:  python-d2to1
%else
BuildRequires:  python%{pydefault}-d2to1
%endif

Requires:       ansible-pacemaker
Requires:       ansible-tripleo-ipsec
Requires:       ansible-role-container-registry
Requires:       python%{pydefault}-jinja2
Requires:       python%{pydefault}-six
Requires:       openstack-tripleo-common >= 7.1.0
%if %{pydefault} == 2
Requires:       PyYAML
%else
Requires:       python%{pydefault}-PyYAML
%endif
%if 0%{rhosp} == 1
Requires:       ansible-role-redhat-subscription
%endif

%description
OpenStack TripleO Heat Templates is a collection of templates and tools for
building Heat Templates to do deployments of OpenStack.

%prep
%setup -q -n tripleo-heat-templates-%{upstream_version}

%build
%{pydefault_build}

%install
%{pydefault_install}
install -d -m 755 %{buildroot}/%{_datadir}/%{name}
cp -ar *.yaml %{buildroot}/%{_datadir}/%{name}
cp -ar puppet %{buildroot}/%{_datadir}/%{name}
cp -ar common %{buildroot}/%{_datadir}/%{name}
cp -ar docker %{buildroot}/%{_datadir}/%{name}
if [ -d docker_config_scripts ]; then
  cp -ar docker_config_scripts %{buildroot}/%{_datadir}/%{name}
fi
cp -ar firstboot %{buildroot}/%{_datadir}/%{name}
cp -ar extraconfig %{buildroot}/%{_datadir}/%{name}
cp -ar environments %{buildroot}/%{_datadir}/%{name}
cp -ar network %{buildroot}/%{_datadir}/%{name}
if [ -d networks ]; then
  cp -ar networks %{buildroot}/%{_datadir}/%{name}
fi
cp -ar validation-scripts %{buildroot}/%{_datadir}/%{name}
cp -ar deployed-server %{buildroot}/%{_datadir}/%{name}
cp -ar ci %{buildroot}/%{_datadir}/%{name}
cp -ar plan-samples %{buildroot}/%{_datadir}/%{name}
cp -ar roles %{buildroot}/%{_datadir}/%{name}
cp -ar scripts %{buildroot}/%{_datadir}/%{name}
cp -ar tools %{buildroot}/%{_datadir}/%{name}
if [ -d examples ]; then
  rm -rf examples
fi

if [ -d %{buildroot}/%{pydefault_sitelib}/tripleo_heat_merge ]; then
  rm -rf %{buildroot}/%{pydefault_sitelib}/tripleo_heat_merge
  rm -f %{buildroot}/%{_bindir}/tripleo-heat-merge
fi

%files
%doc README*
%license LICENSE
%{pydefault_sitelib}/tripleo_heat_templates-*.egg-info
%{_datadir}/%{name}

%changelog
