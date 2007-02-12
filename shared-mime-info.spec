Summary:	Shared MIME-info specification
Summary(pl.UTF-8):   Wspólna specyfikacja MIME-info
Name:		shared-mime-info
Version:	0.18
Release:	2
License:	GPL
Group:		Applications
#Source0:	http://freedesktop.org/software/shared-mime-info/%{name}-%{version}.tar.gz
Source0:	http://freedesktop.org/~hadess/%{name}-%{version}.tar.gz
# Source0-md5:	63398294a078dd9f72a7c4e122a668c8
Patch0:		%{name}-dtd_path.patch
Patch1:		%{name}-dicom.patch
Patch2:		%{name}-directory_alias_fix.patch
Patch3:		%{name}-debug.patch
Patch4:		%{name}-pl.patch
URL:		http://www.freedesktop.org/wiki/Software/shared-mime-info
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-utils
BuildRequires:	glib2-devel >= 1:2.12.2
BuildRequires:	intltool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
To jest wspólna baza informacji MIME freedesktop.org.

Wiele programów oraz pulpitów używa systemu MIME do reprezentacji
typów plików. Często, zachodzi potrzeba opracowania prawidłowego typu
MIME dla pliku. Przeważnie jest to robione poprzez sprawdzenie nazwy
lub zawartości pliku i znalezienie odpowiedniego typu MIME w bazie.

W ramach współpracy, użytecznym jest używanie tej samej bazy przez
różne programy. Dzięki temu pozycja dodana do bazy realizowana jest we
wszystkich programach.

Ta specyfikacja ma za zadanie zunifikowanie systemów odpytujących o
typ używanych przez GNOME, KDE i ROX. W tym pakiecie zawarte są
jedynie mapowania nazwa-typ i zawartość-typ. Inne informacje MIME,
takie jak domyślna procedura obsługi dla poszczególnych typów, czy
ikona używana podczas wyświetlania w zarządcy plików, nie są zawarte,
gdyż zależą od gustu.

Dlatego freedesktop.org udostępnia wspólne bazy w tym formacie aby
uniknąć niekonsekwencji między pulpitami. Ta baza została stworzona
poprzez konwersję istniejących baz KDE i GNOME do nowego formatu i
połączenie ich.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-update-mimedb
%{__make}

db2html shared-mime-info-spec.xml

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


rm -rf $RPM_BUILD_ROOT%{_datadir}/locale

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%preun
# remove dirs and files created by update-mime-database
if [ "$1" = "0" ]; then
	rm -rf /usr/share/mime/*
fi

%files
%defattr(644,root,root,755)
%doc shared-mime-info-spec README NEWS
%attr(755,root,root) %{_bindir}/update-mime-database
%dir %{_datadir}/mime
%dir %{_datadir}/mime/packages
%{_datadir}/mime/packages/freedesktop.org.xml
%{_mandir}/man*/*
%{_pkgconfigdir}/*.pc
