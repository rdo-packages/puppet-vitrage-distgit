%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           puppet-vitrage
Version:        1.0.0
Release:        1%{?dist}
Summary:        Puppet module for OpenStack Vitrage
License:        ASL 2.0

URL:            https://launchpad.net/puppet-vitrage

Source0:        https://github.com/openstack/%{name}/archive/%{upstream_version}.tar.gz

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
%if 0%{?dlrn}
%setup -q -n openstack-vigrage-%{upstream_version}
%else
%setup -q -n %{name}-%{upstream_version}
%endif

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
* Mon Oct 30 2017 Alfredo Moralejo <amoralej@redhat.com> - 1.0.0-1
- Update to 1.0.0

* Tue Aug 29 2017 hguemar <hguemar@benihime.seireitei> - 0.0.1-1.e5f1e917git
- Pike update 0.0.1 (e5f1e917b6a8f7f6b9827ac419b5a846e60e7451)

