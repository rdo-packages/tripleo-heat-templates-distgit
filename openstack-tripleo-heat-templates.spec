%global project tripleo-heat-templates

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           openstack-tripleo-heat-templates
Summary:        Heat templates for TripleO
Version:        2.2.0
Release:        1%{?dist}
License:        ASL 2.0
Group:          System Environment/Base
URL:            https://wiki.openstack.org/wiki/TripleO
Source0:        https://tarballs.openstack.org/%{project}/%{project}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-d2to1
BuildRequires:  python-pbr
BuildRequires:  git

Requires:       PyYAML

%description
OpenStack TripleO Heat Templates is a collection of templates and tools for
building Heat Templates to do deployments of OpenStack.

%prep
%autosetup -n %{project}-%{upstream_version} -S git

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
* Tue May 23 2017 Alfredo Moralejo <amoralej@redhat.com> 2.2.0-1
- Update to 2.2.0

* Fri Apr 15 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 2.0.0-3.f3215d2git
- Fix BR: git

* Sat Apr  2 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 2.0.0-2.f3215d2git
- Fix MariaDB and Pacemaker issues

* Wed Mar 30 2016 RDO <rdo-list@redhat.com> 2.0.0-1
- RC1 Rebuild for Mitaka RC1 
