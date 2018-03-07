%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           openstack-tripleo-heat-templates
Summary:        Heat templates for TripleO
Version:        6.2.11
Release:        1%{?dist}
License:        ASL 2.0
Group:          System Environment/Base
URL:            https://wiki.openstack.org/wiki/TripleO
Source0:        https://tarballs.openstack.org/tripleo-heat-templates/tripleo-heat-templates-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-d2to1
BuildRequires:  python-pbr

Requires:       PyYAML
Requires:       python-jinja2
Requires:       python-six

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
cp -ar docker %{buildroot}/%{_datadir}/%{name}
cp -ar firstboot %{buildroot}/%{_datadir}/%{name}
cp -ar extraconfig %{buildroot}/%{_datadir}/%{name}
cp -ar environments %{buildroot}/%{_datadir}/%{name}
cp -ar network %{buildroot}/%{_datadir}/%{name}
cp -ar validation-scripts %{buildroot}/%{_datadir}/%{name}
cp -ar deployed-server %{buildroot}/%{_datadir}/%{name}
cp -ar ci %{buildroot}/%{_datadir}/%{name}
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
* Wed Mar 07 2018 RDO <dev@lists.rdoproject.org> 6.2.11-1
- Update to 6.2.11

* Thu Feb 08 2018 RDO <dev@lists.rdoproject.org> 6.2.10-1
- Update to 6.2.10

* Thu Jan 25 2018 RDO <dev@lists.rdoproject.org> 6.2.9-1
- Update to 6.2.9

* Mon Jan 08 2018 RDO <dev@lists.rdoproject.org> 6.2.8-1
- Update to 6.2.8

* Sat Dec 09 2017 RDO <dev@lists.rdoproject.org> 6.2.7-1
- Update to 6.2.7

* Wed Nov 22 2017 RDO <dev@lists.rdoproject.org> 6.2.6-1
- Update to 6.2.6

* Tue Nov 14 2017 RDO <dev@lists.rdoproject.org> 6.2.5-1
- Update to 6.2.5

* Fri Nov 03 2017 RDO <dev@lists.rdoproject.org> 6.2.4-1
- Update to 6.2.4

* Tue Oct 10 2017 rdo-trunk <javier.pena@redhat.com> 6.2.3-1
- Update to 6.2.3

* Thu Oct 05 2017 rdo-trunk <javier.pena@redhat.com> 6.2.2-1
- Update to 6.2.2

* Tue Sep 05 2017 rdo-trunk <javier.pena@redhat.com> 6.2.1-1
- Update to 6.2.1

* Thu Jul 20 2017 rdo-trunk <javier.pena@redhat.com> 6.2.0-1
- Update to 6.2.0

* Fri Jul 14 2017 Alfredo Moralejo <amoralej@redhat.com> 6.1.0-1
- Update to 6.1.0

* Wed Mar 08 2017 Alfredo Moralejo <amoralej@redhat.com> 6.0.0-1
- Update to 6.0.0

* Mon Mar 06 2017 Alfredo Moralejo <amoralej@redhat.com> 6.0.0-0.2.0rc2
- Update to 6.0.0.0rc2

* Fri Feb 17 2017 Alfredo Moralejo <amoralej@redhat.com> 6.0.0-0.1.0rc1
- Update to 6.0.0.0rc1

