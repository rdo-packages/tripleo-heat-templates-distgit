%define old_version 2.1.0
%define old_name mitaka

Name:		openstack-tripleo-heat-templates
Summary:	Heat templates for TripleO
Version:    XXX
Release:    XXX
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
Source0:	http://tarballs.openstack.org/tripleo-heat-templates/tripleo-heat-templates-%{version}.tar.gz
Source1:    http://tarballs.openstack.org/tripleo-heat-templates/tripleo-heat-templates-%{old_version}.tar.gz

BuildArch:	noarch
BuildRequires:	python2-devel
BuildRequires:	python-setuptools
BuildRequires:	python-d2to1
BuildRequires:	python-pbr

Requires:	PyYAML
Requires:   %{name}-%{old_name} = %{version}-%{release}

%description
OpenStack TripleO Heat Templates is a collection of templates and tools for
building Heat Templates to do deployments of OpenStack.

%package %{old_name}
Summary:    Heat templates for the Red Hat OpenStack Platform 8 release
Group:      System Environment/Base

Requires:	PyYAML

%description %{old_name}
OpenStack TripleO Heat Templates is a collection of templates and tools for
building Heat Templates to do deployments of OpenStack.  This set of
templates is for use with the %{old_name} release.

%prep
%setup -q -n tripleo-heat-templates-%{upstream_version}
%setup -T -n %{project}-%{version} -D -a 1

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
if [ -d examples ]; then
  rm -rf examples
fi

if [ -d %{buildroot}/%{python2_sitelib}/tripleo_heat_merge ]; then
  rm -rf %{buildroot}/%{python2_sitelib}/tripleo_heat_merge
  rm -f %{buildroot}/%{_bindir}/tripleo-heat-merge
fi

cd %{project}-%{old_version}
install -d -m 755 %{buildroot}/%{_datadir}/%{name}/%{old_name}
cp -ar *.yaml %{buildroot}/%{_datadir}/%{name}/%{old_name}
cp -ar puppet %{buildroot}/%{_datadir}/%{name}/%{old_name}
cp -ar firstboot %{buildroot}/%{_datadir}/%{name}/%{old_name}
cp -ar extraconfig %{buildroot}/%{_datadir}/%{name}/%{old_name}
cp -ar environments %{buildroot}/%{_datadir}/%{name}/%{old_name}
cp -ar network %{buildroot}/%{_datadir}/%{name}/%{old_name}
if [ -d validation-scripts ]; then
  cp -ar validation-scripts %{buildroot}/%{_datadir}/%{name}/%{old_name}
fi
if [ -d examples ]; then
  rm -rf examples
fi
cd ..


%files
%doc README*
%license LICENSE
%{python2_sitelib}/tripleo_heat_templates-*.egg-info
%{_datadir}/%{name}

%files %{old_name}
%{_datadir}/%{name}/%{old_name}

%changelog
