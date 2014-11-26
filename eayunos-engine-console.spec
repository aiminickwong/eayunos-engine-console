Name:		eayunos-engine-console
Version:	0.5
Release:	2%{?dist}
Summary:	Management Tool

Group:		Application
License:	GPL
URL:		http://www.eayun.com
Source0:	eayunos-engine-console-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	/bin/bash
Requires:	ovirt-engine
Requires:	engine-reports-config-passwd

%description
EayunOS Engine Management Tool.

%prep
%setup -q


%build


%install
rm -rf %{buildroot}
rm -rf .git
mkdir -p %{buildroot}/usr/libexec/
mkdir -p %{buildroot}/usr/share/doc/eayunos-engine-console/
cp eayunos-engine-console %{buildroot}/usr/libexec/
cp README.md %{buildroot}/usr/share/doc/eayunos-engine-console/

%post
useradd engineadm &> /dev/null
passwd -d engineadm &> /dev/null
passwd -e engineadm &> /dev/null
sed -i "/engineadm/ s/\/bin\/bash/\/usr\/libexec\/eayunos-engine-console/g" /etc/passwd
echo 'engineadm   ALL=(ALL)       NOPASSWD:ALL' >> /etc/sudoers
cat >> /etc/rsyslog.conf <<EOF
# Save eayunos-engine-console messages
local3.*                                                /var/log/eayunos-engine-console.log
EOF
service rsyslog restart &> /dev/null

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%attr(0755,root,root)/usr/libexec/eayunos-engine-console
%doc /usr/share/doc/eayunos-engine-console/README.md




%changelog
* Fri Nov 26 2014 MaZhe <zhe.ma@eayun.com> 0.5-2
- Fix network configuration bug [issue #6]

* Fri Nov 26 2014 MaZhe <zhe.ma@eayun.com> 0.5-1
- Add oVirt Engine Reports Portal user password configuration function

* Fri Nov 21 2014 MaZhe <zhe.ma@eayun.com> 0.4-6
- fix interactive infomation (issues #2)

* Fri Oct 17 2014 MaZhe <zhe.ma@eayun.com> 0.1-1
- Initial package tagging.
