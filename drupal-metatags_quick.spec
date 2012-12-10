%define modname		metatags_quick
%define drupal_version	7
%define module_version	2.5
%define version		%{drupal_version}.x.%{module_version}
%define tarname		%{modname}-%{drupal_version}.x-%{module_version}

Name:		drupal-%{modname}
Summary:	Meta tags quick module for Drupal
Version:	%{version}
Release:	1
License:	GPLv2+
Group:		Networking/WWW
URL:		https://drupal.org/project/%{modname}
Source0:	http://ftp.drupal.org/files/projects/%{tarname}.tar.gz
BuildArch:	noarch
Requires:	drupal >= %{drupal_version}
Requires:	drupal < %{lua: print(rpm.expand("%{drupal_version}")+1)}

%description
Meta tags support for Drupal 7 sites based on Fields API.

%prep
%setup -q -n %{modname}

%build

%install
%__install -d -m 0755 %{buildroot}%{_var}/www/drupal/modules/
cp -a . %{buildroot}%{_var}/www/drupal/modules/%{modname}
rm -f %{buildroot}%{_var}/www/drupal/modules/%{modname}/*.txt

%files
%{_var}/www/drupal/modules/%{modname}
%doc README.txt


%changelog
* Thu Aug 09 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 7.x.2.5-1
+ Revision: 813305
- update to 7.x.2.5

* Sat May 12 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 7.x.2.4-1
+ Revision: 798458
- imported package drupal-metatags_quick

