# guard for package OSP does not support
%global rhosp 0

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           openstack-tripleo-heat-templates
Summary:        Heat templates for TripleO
Version:        8.2.0
Release:        1%{?dist}
License:        ASL 2.0
Group:          System Environment/Base
URL:            https://wiki.openstack.org/wiki/TripleO
Source0:        https://tarballs.openstack.org/tripleo-heat-templates/tripleo-heat-templates-%{upstream_version}.tar.gz

#

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python-d2to1
BuildRequires:  python2-pbr

Requires:       ansible-pacemaker
Requires:       ansible-tripleo-ipsec
Requires:       PyYAML
Requires:       python2-jinja2
Requires:       python2-six
Requires:       openstack-tripleo-common >= 7.1.0
%if 0%{rhosp} == 1
Requires:       ansible-role-redhat-subscription
%endif

%description
OpenStack TripleO Heat Templates is a collection of templates and tools for
building Heat Templates to do deployments of OpenStack.

%prep
%setup -q -n tripleo-heat-templates-%{upstream_version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}
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

if [ -d %{buildroot}/%{python2_sitelib}/tripleo_heat_merge ]; then
  rm -rf %{buildroot}/%{python2_sitelib}/tripleo_heat_merge
  rm -f %{buildroot}/%{_bindir}/tripleo-heat-merge
fi

%files
%doc README*
%license LICENSE
%{python2_sitelib}/tripleo_heat_templates-*.egg-info
%{_datadir}/%{name}

%changelog
* Tue Dec 18 2018 RDO <dev@lists.rdoproject.org> 8.2.0-1
- Update to 8.2.0

* Wed Dec 05 2018 RDO <dev@lists.rdoproject.org> 8.1.0-1
- Update to 8.1.0

* Thu Sep 27 2018 RDO <dev@lists.rdoproject.org> 8.0.7-1
- Update to 8.0.7

* Wed Aug 08 2018 RDO <dev@lists.rdoproject.org> 8.0.5-1
- Update to 8.0.5

* Mon Jul 09 2018 RDO <dev@lists.rdoproject.org> 8.0.4-1
- Update to 8.0.4

* Mon Jun 04 2018 RDO <dev@lists.rdoproject.org> 8.0.3-1
- Update to 8.0.3

* Mon Apr 23 2018 RDO <dev@lists.rdoproject.org> 8.0.2-1
- Update to 8.0.2

* Tue Mar 27 2018 RDO <dev@lists.rdoproject.org> 8.0.1-1
- Update to 8.0.1

* Tue Mar 13 2018 RDO <dev@lists.rdoproject.org> 8.0.0-1
- Update to 8.0.0

* Thu Mar 08 2018 RDO <dev@lists.rdoproject.org> 8.0.0-0.1.0rc1
- Update to 8.0.0.0rc1

