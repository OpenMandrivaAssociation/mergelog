Summary:	Merges httpd log files by date
Name:		mergelog
Version:	4.5
Release:	7
Group:		System/Servers
License:	GPLv2
URL:		http://mergelog.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/mergelog/%{name}-%{version}.tar.bz2
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
mergelog is a small and fast C program which merges by date httpd log files in
'Common Log Format' from web servers behind round-robin DNS. It has been
designed to easily manage huge log files from highly stressed servers. mergelog
is distributed with zmergelog which supports gzipped log files.

%prep
%setup -q

%build
%configure2_5x
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 src/mergelog %{buildroot}%{_sbindir}/
install -m0755 src/zmergelog %{buildroot}%{_sbindir}/

install -m0644 man/mergelog.1 %{buildroot}%{_mandir}/man1
install -m0644 man/zmergelog.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README
%attr(0755,root,root) %{_sbindir}/mergelog
%attr(0755,root,root) %{_sbindir}/zmergelog
%attr(0640,root,root) %{_mandir}/man1/mergelog.1*
%attr(0640,root,root) %{_mandir}/man1/zmergelog.1*




%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 4.5-6mdv2011.0
+ Revision: 612849
- the mass rebuild of 2010.1 packages

* Tue Mar 02 2010 Sandro Cazzaniga <kharec@mandriva.org> 4.5-5mdv2010.1
+ Revision: 513598
- Fixc license
- use configure2_5x
- fix clean section

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 4.5-4mdv2010.0
+ Revision: 430017
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 4.5-3mdv2009.0
+ Revision: 252311
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 4.5-1mdv2008.1
+ Revision: 136578
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Jan 15 2007 Oden Eriksson <oeriksson@mandriva.com> 4.5-1mdv2007.0
+ Revision: 109224
- Import mergelog

* Mon Jan 15 2007 Oden Eriksson <oeriksson@mandriva.com> 4.5-1mdv2007.1
- initial Mandriva package

