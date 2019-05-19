%define url_ver %(echo %{version}|cut -d. -f1,2)

%define oname	mateweather
%define major	1
%define libname	%mklibname %{oname} %{major}
%define devname	%mklibname -d %{oname}

Summary:	MATE Weather applet library
Name:		libmateweather
Version:	1.22.0
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	libxml2-utils
BuildRequires:	mate-common
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(libsoup-gnome-2.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	timezone

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides a library to provide Weather data to the MATE panel
applet.

%files -f %{name}.lang
%doc AUTHORS NEWS README
%{_datadir}/glib-2.0/schemas/org.mate.weather.gschema.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/locations.dtd
%{_datadir}/%{name}/Locations.xml
%{_iconsdir}/mate/*/status/weather*

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	MATE Weather applet library
Group:		System/Libraries

%description -n %{libname}
This is a library to provide Weather data to the MATE panel applet.

%files -n %{libname}
%{_libdir}/libmateweather.so.%{major}*

#---------------------------------------------------------------------------

%package -n %{devname}
Summary:	MATE Weather applet library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This is a library to provide Weather data to the MATE panel applet.

%files -n %{devname}
%doc ChangeLog
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%dir %{_datadir}/gtk-doc/html/%{name}
%{_datadir}/gtk-doc/html/%{name}/*

#---------------------------------------------------------------------------

%prep
%setup -q

%build
#NOCONFIGURE=yes ./autogen.sh
%configure \
	--disable-schemas-compile \
	--enable-gtk-doc-html \
	%{nil}
%make_build

%install
%make_install

# locales
%find_lang %{name} --with-gnome --all-name
for xmlfile in %{buildroot}%{_datadir}/%{name}/Locations.*.xml; do
	echo "%lang($(basename $xmlfile|sed -e s/Locations.// -e s/.xml//)) $(echo $xmlfile | sed s!%{buildroot}!!)" >> %{name}.lang
done
