#
# Conditional build:
# _without_building_doc - don't build html documentation from xml source

Summary:	Shared MIME-Info Specification
Summary(pl):	Wsp�lna Specyfikacja MIME-Info
Name:		shared-mime-info
Version:	0.9
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.freedesktop.org/standards/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-fix-mime-info-path.patch
Patch1:		%{name}-am_fix.patch
%{!?_without_building_doc:BuildRequires:	docbook-utils}
BuildRequires:  libxml2-devel >= 2.4.0
URL:		http://www.freedesktop.org/standards/shared-mime-info.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This is the freedesktop.org shared MIME info database.

Many programs and desktops use the MIME system to represent the types
of files. Frequently, it is necessary to work out the correct MIME
type for a file. This is generally done by examining the file's name
or contents, and looking up the correct MIME type in a database.

For interoperability, it is useful for different programs to use the
same database so that different programs agree on the type of a file,
and new rules for determining the type apply to all programs.

This specification attempts to unify the type-guessing systems
currently in use by GNOME, KDE and ROX. Only the name-to-type and
contents-to-type mappings are covered by this spec; other MIME type
information, such as the default handler for a particular type, or the
icon to use to display it in a file manager, are not covered since
these are a matter of style.

In addition, freedesktop.org provides a shared database in this format
to avoid inconsistencies between desktops. This database has been
created by converting the existing KDE and GNOME databases to the new
format and merging them together.

%description -l pl
To jest wsp�lna baza informacji MIME freedesktop.org.

Wiele program�w oraz pulpit�w u�ywa systemu MIME do reprezentacji
typ�w plik�w. Cz�sto, zachodzi potrzeba opracowania prawid�owego typu
MIME dla pliku. Przewa�nie jest to robione poprzez sprawdzenie nazwy
lub zawarto�ci pliku i znale�ienie odpowiedniego typu MIME w bazie.

W ramach wsp�pracy, u�ytecznym jest u�ywanie tej samej bazy przez
r�ne programy. Dzi�ki temu pozycja dodana do bazy realizowana jest we
wszystkich programach.

Ta specyfikacja ma za zadanie zunifikowanie system�w odpytuj�cych o
typ u�ywanych przez GNOME, KDE i ROX. W tym pakiecie zawarte s�
jedynie mapowania nazwa-typ i zawarto��-typ. Inne informacje MIME,
takie jak domy�lna procedura obs�ugi dla poszczeg�lnych typ�w, czy
ikona u�ywana podczas wy�wietlania w menad�erze plik�w, nie s�
zawarte, gdy� zale�� od gustu.

Dlatego freedesktop.org udost�pnia wsp�lne bazy w tym formacie aby
unikn�� niekonsekwencji mi�dzy pulpitami. Ta baza zosta�a stworzona
poprzez przekonwertowanie istniej�cych baz KDE i GNOME do nowego
formatu i po��czenie ich razem.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
aclocal
%{__autoconf}
%{__automake}
%{configure}
%{__make}
%{!?_without_building_doc:db2html shared-mime-info-spec.xml}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%post
%{_bindir}/update-mime-database %{_datadir}/mime-info

%postun
%{_bindir}/update-mime-database %{_datadir}/mime-info

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc shared-mime-info-spec.* README NEWS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/mime-info/*
