%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-vitrage
Version:        3.3.1
Release:        1%{?dist}
Summary:        Puppet module for OpenStack Vitrage
License:        ASL 2.0

URL:            https://launchpad.net/puppet-vitrage

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-inifile
Requires:       puppet-openstacklib
Requires:       puppet-oslo
Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0
Requires:       puppet-keystone

%description
Puppet module for OpenStack Vitrage

%prep
%setup -q -n openstack-vitrage-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/vitrage/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/vitrage/



%files
%{_datadir}/openstack-puppet/modules/vitrage/


%changelog
* Mon Oct 15 2018 RDO <dev@lists.rdoproject.org> 3.3.1-1
- Update to 3.3.1

* Mon Aug 20 2018 RDO <dev@lists.rdoproject.org> 3.3.0-1
- Update to 3.3.0


