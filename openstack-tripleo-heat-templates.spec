%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           openstack-tripleo-heat-templates
Summary:        Heat templates for TripleO
Version:        5.3.10
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
if [ -d ci ]; then
  cp -ar ci %{buildroot}/%{_datadir}/%{name}
fi
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
* Wed Mar 07 2018 RDO <dev@lists.rdoproject.org> 5.3.10-1
- Update to 5.3.10

* Tue Jan 23 2018 RDO <dev@lists.rdoproject.org> 5.3.9-1
- Update to 5.3.9

* Mon Jan 08 2018 RDO <dev@lists.rdoproject.org> 5.3.8-1
- Update to 5.3.8

* Sat Dec 09 2017 RDO <dev@lists.rdoproject.org> 5.3.7-1
- Update to 5.3.7

* Wed Nov 22 2017 RDO <dev@lists.rdoproject.org> 5.3.6-1
- Update to 5.3.6

* Wed Nov 15 2017 RDO <dev@lists.rdoproject.org> 5.3.5-1
- Update to 5.3.5

* Fri Nov 03 2017 RDO <dev@lists.rdoproject.org> 5.3.4-1
- Update to 5.3.4

* Wed Oct 11 2017 rdo-trunk <javier.pena@redhat.com> 5.3.3-1
- Update to 5.3.3

* Thu Oct 05 2017 rdo-trunk <javier.pena@redhat.com> 5.3.2-1
- Update to 5.3.2

* Mon Sep 04 2017 rdo-trunk <javier.pena@redhat.com> 5.3.1-1
- Update to 5.3.1

* Thu Apr 27 2017 rdo-trunk <javier.pena@redhat.com> 5.3.0-1
- Update to 5.3.0

* Tue Jan 10 2017 Alfredo Moralejo <amoralej@redhat.com> 5.2.0-1
- Update to 5.2.0

* Tue Nov 15 2016 Alfredo Moralejo <amoralej@redhat.com> 5.1.0-1
- Update to 5.1.0

* Thu Oct 20 2016 Haikel Guemar <hguemar@fedoraproject.org> 5.0.0-1
- Update to 5.0.0

* Tue Oct 18 2016 Alfredo Moralejo <amoralej@redhat.com> 5.0.0-0.4.0rc3
- Update to 5.0.0.0rc3

* Thu Sep 29 2016 Haikel Guemar <hguemar@fedoraproject.org> 5.0.0-0.3.0rc2
- Update to 5.0.0.0rc2

* Wed Sep 21 2016 Alfredo Moralejo <amoralej@redhat.com> 5.0.0-0.2.0rc1
- Update to 5.0.0.0rc1

* Fri Sep 16 2016 Haikel Guemar <hguemar@fedoraproject.org> 5.0.0-0.1.0b3
- Update to 5.0.0.0b3

