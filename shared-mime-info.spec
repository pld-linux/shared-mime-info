# TODO
# - *.pc file to -devel, however harmless due it's not pulling any extra deps
# - try to move generated files in /usr/share/mime to /var/cache/mime for FHS.
Summary:	Shared MIME-info specification
Summary(pl.UTF-8):	Wspólna specyfikacja MIME-info
Name:		shared-mime-info
Version:	0.80
Release:	1
Epoch:		1
License:	GPL
Group:		Applications
Source0:	http://people.freedesktop.org/~hadess/%{name}-%{version}.tar.bz2
# Source0-md5:	eb8d24a6a80888849c9db7f30232ba6a
URL:		http://www.freedesktop.org/wiki/Software/shared-mime-info
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-utils
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires:	glib2 >= 1:2.18.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noarchpkgconfigdir	/usr/share/pkgconfig

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

%package doc
Summary:	Manual for %{name}
Summary(fr.UTF-8):	Documentation pour %{name}
Summary(it.UTF-8):	Documentazione di %{name}
Summary(pl.UTF-8):	Dokumentacja do %{name}
Group:		Documentation

%description doc
Documentation for %{name}.

%description doc -l fr.UTF-8
Documentation pour %{name}.

%description doc -l it.UTF-8
Documentazione di %{name}.

%description doc -l pl.UTF-8
Dokumentacja do %{name}.

%prep
%setup -q

%build
%{__intltoolize}
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

# convience symlink
ln -s t1.html shared-mime-info-spec/index.html

# ghost generated files
# see update-mime-database.c const char *media_types
install -d $RPM_BUILD_ROOT%{_datadir}/mime/{application,audio,image,inode,message,model,multipart,text,video,x-content,x-epoc}
# see specification, also grep -F .new update-mime-database.c
touch $RPM_BUILD_ROOT%{_datadir}/mime/globs
touch $RPM_BUILD_ROOT%{_datadir}/mime/globs2
touch $RPM_BUILD_ROOT%{_datadir}/mime/magic
touch $RPM_BUILD_ROOT%{_datadir}/mime/XMLnamespaces
touch $RPM_BUILD_ROOT%{_datadir}/mime/subclasses
touch $RPM_BUILD_ROOT%{_datadir}/mime/aliases
touch $RPM_BUILD_ROOT%{_datadir}/mime/types
touch $RPM_BUILD_ROOT%{_datadir}/mime/generic-icons
touch $RPM_BUILD_ROOT%{_datadir}/mime/icons
touch $RPM_BUILD_ROOT%{_datadir}/mime/treemagic
touch $RPM_BUILD_ROOT%{_datadir}/mime/mime.cache

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%preun
# remove dirs and files created by update-mime-database
if [ "$1" = "0" ]; then
	rm -rf %{_datadir}/mime/*
fi

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_bindir}/update-mime-database
%dir %{_datadir}/mime
%dir %{_datadir}/mime/packages
%{_datadir}/mime/packages/freedesktop.org.xml
%{_mandir}/man1/update-mime-database.1*
%{_noarchpkgconfigdir}/shared-mime-info.pc

# generated content
%dir %{_datadir}/mime/application
%dir %{_datadir}/mime/audio
%dir %{_datadir}/mime/image
%dir %{_datadir}/mime/inode
%dir %{_datadir}/mime/message
%dir %{_datadir}/mime/model
%dir %{_datadir}/mime/multipart
%dir %{_datadir}/mime/text
%dir %{_datadir}/mime/video
%dir %{_datadir}/mime/x-content
%dir %{_datadir}/mime/x-epoc
%ghost %{_datadir}/mime/globs
%ghost %{_datadir}/mime/globs2
%ghost %{_datadir}/mime/magic
%ghost %{_datadir}/mime/XMLnamespaces
%ghost %{_datadir}/mime/subclasses
%ghost %{_datadir}/mime/aliases
%ghost %{_datadir}/mime/types
%ghost %{_datadir}/mime/generic-icons
%ghost %{_datadir}/mime/icons
%ghost %{_datadir}/mime/treemagic
%ghost %{_datadir}/mime/mime.cache

%files doc
%defattr(644,root,root,755)
%doc shared-mime-info-spec/*
