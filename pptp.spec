Name:         pptp
Version:      1.10.0
Release:      8
Summary:      Point-to-Point Tunneling Protocol (PPTP) Client
License:      GPLv2+
URL:          http://pptpclient.sourceforge.net/
Source0:      http://downloads.sf.net/pptpclient/pptp-%{version}.tar.gz
Source1:      pptp-tmpfs.conf
Patch0:       pptp-fix-cc.patch
BuildRequires:gcc perl-generators perl-podlators
Requires:     ppp >= 2.4.2 iproute systemd-units
Requires:     %{name}-help = %{version}-%{release}
Provides:     pptp-setup
Obsoletes:    pptp-setup

%description
Client for the proprietary Microsoft Point-to-Point Tunneling
Protocol, PPTP. Allows connection to a PPTP based VPN as used
by employers and some cable and ADSL service providers.

%package      help
Summary:      Help documents for pptp

%description  help
This package provides help documents for pptp.

%prep
%autosetup -p1
perl -pi -e 's/install -o root -m 555 pptp/install -m 755 pptp/;' Makefile

%build
OUR_CFLAGS="-Wall %{optflags} -Wextra -Wstrict-aliasing=2 -Wnested-externs -Wstrict-prototypes"
%make_build CFLAGS="$OUR_CFLAGS" LDFLAGS="$RPM_LD_FLAGS" IP=/sbin/ip

%install
rm -rf %{buildroot}
%make_install
install -d -m 750 %{buildroot}%{_localstatedir}/run/pptp
install -d -m 755 %{buildroot}%{_prefix}/lib/tmpfiles.d
install -p -m 644 %{SOURCE1} %{buildroot}%{_prefix}/lib/tmpfiles.d/pptp.conf

%files
%doc AUTHORS COPYING DEVELOPERS NEWS README TODO USING
%doc ChangeLog Documentation/DESIGN.PPTP PROTOCOL-SECURITY
%{_sbindir}/pptp
%{_sbindir}/pptpsetup
%{_prefix}/lib/tmpfiles.d/pptp.conf
%config(noreplace) %{_sysconfdir}/ppp/options.pptp
%dir %attr(750,root,root) %{_localstatedir}/run/pptp/

%files help
%{_mandir}/man8/pptp.8*
%{_mandir}/man8/pptpsetup.8*

%changelog
* Sat Apr 15 2023 Xiaoya Huang <huangxiaoya@iscas.ac.cn> - 1.10.0-8
- Fix CC compiler support

* Fri Nov 06 2020 caodongxia <caodongxia@huawei.com> - 1.10.0-7
- Add install requires help package into main package 

* Fri Feb 14 2020 Senlin Xia <xiasenlin1@huawei.com> - 1.10.0-6
- Pakcage init
