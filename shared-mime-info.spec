# TODO: update polish patch
Summary:	Shared MIME-info specification
Summary(pl):	Wspólna specyfikacja MIME-info
Name:		shared-mime-info
Version:	0.17
Release:	0.2
License:	GPL
Group:		Applications
#Source0:	http://freedesktop.org/software/shared-mime-info/%{name}-%{version}.tar.gz
Source0:	http://freedesktop.org/~hadess/%{name}-%{version}.tar.gz
# Source0-md5:	f1014ad243b5245279c0abe1b95d9e38
Patch0:		%{name}-dtd_path.patch
Patch1:		%{name}-locale-names.patch
Patch2:		%{name}-dicom.patch
Patch3:		%{name}-polish.patch
Patch4:		%{name}-word.patch
Patch5:		%{name}-directory_alias_fix.patch
URL:		http://www.freedesktop.org/wiki/Software/shared-mime-info
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-utils
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	intltool
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	pkgconfig
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

%description -l pl
To jest wspólna baza informacji MIME freedesktop.org.

Wiele programów oraz pulpitów u¿ywa systemu MIME do reprezentacji
typów plików. Czêsto, zachodzi potrzeba opracowania prawid³owego typu
MIME dla pliku. Przewa¿nie jest to robione poprzez sprawdzenie nazwy
lub zawarto¶ci pliku i znalezienie odpowiedniego typu MIME w bazie.

W ramach wspó³pracy, u¿ytecznym jest u¿ywanie tej samej bazy przez
ró¿ne programy. Dziêki temu pozycja dodana do bazy realizowana jest we
wszystkich programach.

Ta specyfikacja ma za zadanie zunifikowanie systemów odpytuj±cych o
typ u¿ywanych przez GNOME, KDE i ROX. W tym pakiecie zawarte s±
jedynie mapowania nazwa-typ i zawarto¶æ-typ. Inne informacje MIME,
takie jak domy¶lna procedura obs³ugi dla poszczególnych typów, czy
ikona u¿ywana podczas wy¶wietlania w zarz±dcy plików, nie s± zawarte,
gdy¿ zale¿± od gustu.

Dlatego freedesktop.org udostêpnia wspólne bazy w tym formacie aby
unikn±æ niekonsekwencji miêdzy pulpitami. Ta baza zosta³a stworzona
poprzez konwersjê istniej±cych baz KDE i GNOME do nowego formatu i
po³±czenie ich.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
#%patch3 -p1
#%patch4 -p0
%patch5 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

db2html shared-mime-info-spec.xml

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
%{_bindir}/update-mime-database %{_datadir}/mime ||:

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc shared-mime-info-spec README NEWS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
%ghost %{_datadir}/mime/globs
%ghost %{_datadir}/mime/magic
%ghost %{_datadir}/mime/XMLnamespaces
%ghost %{_datadir}/mime/application
%ghost %{_datadir}/mime/audio
%ghost %{_datadir}/mime/image
%ghost %{_datadir}/mime/inode
%ghost %{_datadir}/mime/message
%ghost %{_datadir}/mime/model
%ghost %{_datadir}/mime/multipart
%ghost %{_datadir}/mime/text
%ghost %{_datadir}/mime/video
%dir %{_datadir}/mime
%dir %{_datadir}/mime/packages
%{_datadir}/mime/packages/*

%{_pkgconfigdir}/*.pc
