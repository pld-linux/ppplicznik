Summary:	A modem connection timer
Summary(pl):	Licznik czasu po³±czenia modemowego
Name:		ppplicznik
Version:	0.2b2
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
URL:		http://gruesome.republika.pl
Source0:	http://gruesome.republika.pl/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-c++
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ppplicznik is a program which during modem connection lets you to
control it's remaining time and amount of received data. Information
are being displayed in a window on terminal. After terminating the
connection it's data would be saved to a file. \fIppplicznik\fP called
with appriopriate command-line option will read it and show every or
only the last-month connections saved in the file. Configuration is
read from configuration file (default: /etc/ppplicznik.conf).


%description -l pl
ppplicznik to program, który w czasie trwania po³±czenia modemowego
pozwoli Ci kontrolowaæ jego d³ugo¶æ oraz ilo¶æ pobieranych danych.
Informacje prezentowane s± w okienku na terminalu tekstowym. Po
zakoñczeniu po³±czenia dane o nim zostan± zapisane do pliku. ppplicznik
wywo³any z odpowiedni± opcj± odczyta go i przedstawi wszystkie
po³±czenia zapisane w pliku lub tylko te z danego miesi±ca. Parametry
konfiguracyjne program odczytuje z pliku konfiguracyjnego

%prep
%setup -q

%build
aclocal
autoconf
autoheader
automake -a
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_datadir}/%{name}} \
	$RPM_BUILD_ROOT{%{_mandir}/man1,%{_mandir}/pl/man1}

install src/ppplicznik $RPM_BUILD_ROOT%{_bindir}
install misc/dzwiek.wav $RPM_BUILD_ROOT%{_datadir}/ppplicznik
install misc/ppplicznik.1 $RPM_BUILD_ROOT%{_mandir}/man1
install misc/ppplicznik.1.pl $RPM_BUILD_ROOT%{_mandir}/pl/man1/ppplicznik.1
sed s/"\/usr\/local\/share"/"\/usr\/share"/ < misc/ppplicznik.conf > $RPM_BUILD_ROOT%{_sysconfdir}/ppplicznik.conf

gzip -9nf AUTHORS ChangeLog INSTALL* NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/ppplicznik
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/%{name}.conf
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*
