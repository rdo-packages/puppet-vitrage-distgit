%{!?upstream_version: %global upstream_version %{commit}}
%global commit e5f1e917b6a8f7f6b9827ac419b5a846e60e7451
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

Name:           puppet-vitrage
Version:        0.0.1
Release:        1%{?alphatag}%{?dist}
Summary:        Puppet module for OpenStack Vitrage
License:        ASL 2.0

URL:            https://launchpad.net/puppet-vitrage

Source0:        https://github.com/openstack/%{name}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

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
%setup -q -n %{name}-%{upstream_version}

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
* Tue Aug 29 2017 hguemar <hguemar@benihime.seireitei> - 0.0.1-1.e5f1e917git
- Pike update 0.0.1 (e5f1e917b6a8f7f6b9827ac419b5a846e60e7451)

