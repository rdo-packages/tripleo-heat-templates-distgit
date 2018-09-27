%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           openstack-tripleo-heat-templates
Summary:        Heat templates for TripleO
Version:        7.0.17
Release:        1%{?dist}
License:        ASL 2.0
Group:          System Environment/Base
URL:            https://wiki.openstack.org/wiki/TripleO
Source0:        https://tarballs.openstack.org/tripleo-heat-templates/tripleo-heat-templates-%{upstream_version}.tar.gz

#

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-d2to1
BuildRequires:  python-pbr

Requires:       ansible-pacemaker
Requires:       PyYAML
Requires:       python-jinja2
Requires:       python-six
Requires:       openstack-tripleo-common >= 7.1.0

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
* Thu Sep 27 2018 RDO <dev@lists.rdoproject.org> 7.0.17-1
- Update to 7.0.17

* Wed Aug 08 2018 RDO <dev@lists.rdoproject.org> 7.0.15-1
- Update to 7.0.15

* Mon Jul 09 2018 RDO <dev@lists.rdoproject.org> 7.0.14-1
- Update to 7.0.14

* Tue May 29 2018 RDO <dev@lists.rdoproject.org> 7.0.13-1
- Update to 7.0.13

* Mon Apr 23 2018 RDO <dev@lists.rdoproject.org> 7.0.12-1
- Update to 7.0.12

* Tue Mar 27 2018 RDO <dev@lists.rdoproject.org> 7.0.11-1
- Update to 7.0.11

* Wed Mar 07 2018 RDO <dev@lists.rdoproject.org> 7.0.10-1
- Update to 7.0.10

* Mon Feb 12 2018 RDO <dev@lists.rdoproject.org> 7.0.9-1
- Update to 7.0.9

* Wed Jan 24 2018 RDO <dev@lists.rdoproject.org> 7.0.8-1
- Update to 7.0.8

* Mon Jan 08 2018 RDO <dev@lists.rdoproject.org> 7.0.7-1
- Update to 7.0.7

* Sat Dec 09 2017 RDO <dev@lists.rdoproject.org> 7.0.6-1
- Update to 7.0.6

* Wed Nov 22 2017 RDO <dev@lists.rdoproject.org> 7.0.5-1
- Update to 7.0.5

* Tue Nov 14 2017 RDO <dev@lists.rdoproject.org> 7.0.4-1
- Update to 7.0.4

* Fri Nov 03 2017 RDO <dev@lists.rdoproject.org> 7.0.3-1
- Update to 7.0.3

* Tue Oct 10 2017 rdo-trunk <javier.pena@redhat.com> 7.0.2-1
- Update to 7.0.2

* Wed Oct 04 2017 rdo-trunk <javier.pena@redhat.com> 7.0.1-1
- Update to 7.0.1

* Thu Sep 14 2017 rdo-trunk <javier.pena@redhat.com> 7.0.0-1
- Update to 7.0.0

* Sun Sep 10 2017 rdo-trunk <javier.pena@redhat.com> 7.0.0-0.2.0rc1
- Update to 7.0.0.0rc2

* Fri Aug 25 2017 Alfredo Moralejo <amoralej@redhat.com> 7.0.0-0.1.0rc1
- Update to 7.0.0.0rc1

