Summary:	Merges httpd log files by date
Name:		mergelog
Version:	4.5
Release:	%mkrel 4
Group:		System/Servers
License:	GPL
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

%configure

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README
%attr(0755,root,root) %{_sbindir}/mergelog
%attr(0755,root,root) %{_sbindir}/zmergelog
%attr(0640,root,root) %{_mandir}/man1/mergelog.1*
%attr(0640,root,root) %{_mandir}/man1/zmergelog.1*


