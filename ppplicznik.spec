Summary:	A modem connection timer
Summary(pl):	Licznik czasu po��czenia modemowego
Name:		ppplicznik
Version:	1.0.0
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narz�dzia
URL:		http://gruesome.republika.pl/
Source0:	http://gruesome.republika.pl/%{name}-%{version}.tar.bz2
Patch0:		ppplicznik-ncurses-path.patch
BuildRequires:	gcc-c++
BuildRequires:	gettext-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ppplicznik is a program which during modem connection lets you to
control it's remaining time and amount of received data. Informations
are being displayed in a window on terminal. After terminating the
connection it's stats would be saved to a file. ppplicznik called with
appriopriate command-line option will read it and show every or only
the last-month connections saved in the file.

%description -l pl
ppplicznik to program, kt�ry w czasie trwania po��czenia modemowego
pozwoli Ci kontrolowa� jego d�ugo�� oraz ilo�� pobieranych danych.
Informacje prezentowane s� w okienku na terminalu tekstowym. Po
zako�czeniu po��czenia dane o nim zostan� zapisane do pliku.
ppplicznik wywo�any z odpowiedni� opcj� odczyta go i przedstawi
wszystkie po��czenia zapisane w pliku lub tylko te z danego miesi�ca.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_datadir}/%{name}} \
	$RPM_BUILD_ROOT{%{_mandir}/man1,%{_mandir}/pl/man1,%{_datadir}/locale/pl/LC_MESSAGES}

install src/ppplicznik $RPM_BUILD_ROOT%{_bindir}
install misc/sound.wav $RPM_BUILD_ROOT%{_datadir}/ppplicznik
install misc/ppplicznik.1 $RPM_BUILD_ROOT%{_mandir}/man1
# install misc/pl/ppplicznik.1 $RPM_BUILD_ROOT%{_mandir}/pl/man1
sed s/"\/usr\/local\/share"/"\/usr\/share"/ < misc/ppplicznik.conf > $RPM_BUILD_ROOT%{_sysconfdir}/ppplicznik.conf
install po/pl.gmo $RPM_BUILD_ROOT%{_datadir}/locale/pl/LC_MESSAGES/%{name}.mo

gzip -9nf AUTHORS ChangeLog NEWS 

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/ppplicznik
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/%{name}.conf
%{_mandir}/man1/*
# %lang(pl) %{_mandir}/pl/man1/*
