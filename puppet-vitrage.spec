%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x5d2d1e4fb8d38e6af76c50d53d4fec30cf5ce3da
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-vitrage
Version:        8.4.0
Release:        1%{?dist}
Summary:        Puppet module for OpenStack Vitrage
License:        ASL 2.0

URL:            https://launchpad.net/puppet-vitrage

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

Requires:       puppet-inifile
Requires:       puppet-openstacklib
Requires:       puppet-oslo
Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0
Requires:       puppet-keystone

%description
Puppet module for OpenStack Vitrage

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
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
* Fri Apr 02 2021 RDO <dev@lists.rdoproject.org> 8.4.0-1
- Update to 8.4.0


