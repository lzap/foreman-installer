Name:       foreman-installer
Version:    1.1.4
Release:    1%{?dist}
Summary:    Puppet-based installer for The Foreman

Group:      Applications/System
License:    GPLv3+ and ASL 2.0
URL:        http://theforeman.org
Source0:    %{name}-%{version}.tar.gz

%if 0%{?rhel} && 0%{?rhel} == 5
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%endif

BuildArch:  noarch

Requires:   puppet

%description
Script to generate answers for puppet-based installer of The Foreman life-cycle
management system.

%prep
%setup -q

%build
echo "%{VERSION}" > VERSION

%install
cp -dpR * %{buildroot}/%{_datadir}/%{name}

%if 0%{?rhel} && 0%{?rhel} == 5
%clean
%{__rm} -rf $RPM_BUILD_ROOT
%endif

%files
%defattr(-,root,root,-)
%doc README.*
%{_datadir}/%{name}

%changelog
* Thu May 23 2013 Lukas Zapletal <lzap+git@redhat.com> 1.1.4-1
- wip (lzap+git@redhat.com)

* Thu May 23 2013 Lukas Zapletal <lzap+git@redhat.com>
- wip (lzap+git@redhat.com)

* Wed May 23 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.1.2-1
- initial version
