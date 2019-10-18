# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver 3
%else
%global pyver 2
%endif

%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
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
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-pbr

Requires:       ansible-pacemaker
Requires:       ansible-tripleo-ipsec
Requires:       ansible-role-atos-hsm
Requires:       ansible-role-container-registry
Requires:       ansible-role-chrony
Requires:       ansible-role-thales-hsm
Requires:       python%{pyver}-paunch
Requires:       python%{pyver}-jinja2
Requires:       python%{pyver}-six
Requires:       openstack-tripleo-common >= 7.1.0
Requires:       tripleo-ansible
%if %{pyver} == 2
Requires:       PyYAML
%else
Requires:       python%{pyver}-PyYAML
%endif
%if 0%{rhosp} == 1
Requires:       ansible-role-redhat-subscription
%endif

%description
OpenStack TripleO Heat Templates is a collection of templates and tools for
building Heat Templates to do deployments of OpenStack.

%prep
%setup -q -n tripleo-heat-templates-%{upstream_version}
# Replace "env python" shebag to the correct python executable for the system
# if we don't do that brp-mangle-shebangs will change it to python2
for python_script in $(grep "/usr/bin/env python" . -rl)
do
    sed -i "s#/usr/bin/env python.*#/usr/bin/%{pyver_bin}#g" $python_script
done

%build
%{pyver_build}

%install
%{pyver_install}
install -d -m 755 %{buildroot}/%{_datadir}/%{name}
cp -ar *.yaml %{buildroot}/%{_datadir}/%{name}
cp -ar puppet %{buildroot}/%{_datadir}/%{name}
cp -ar common %{buildroot}/%{_datadir}/%{name}
if [ -d docker ] ; then
  cp -ar docker %{buildroot}/%{_datadir}/%{name}
fi
cp -ar deployment %{buildroot}/%{_datadir}/%{name}

# docker_config_scripts will be removed in Stein
if [ -d docker_config_scripts ]; then
  cp -ar docker_config_scripts %{buildroot}/%{_datadir}/%{name}
fi
if [ -d container_config_scripts ]; then
  cp -ar container_config_scripts %{buildroot}/%{_datadir}/%{name}
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

if [ -d %{buildroot}/%{pyver_sitelib}/tripleo_heat_merge ]; then
  rm -rf %{buildroot}/%{pyver_sitelib}/tripleo_heat_merge
  rm -f %{buildroot}/%{_bindir}/tripleo-heat-merge
fi

%files
%doc README*
%license LICENSE
%{pyver_sitelib}/tripleo_heat_templates-*.egg-info
%{_datadir}/%{name}

%changelog
