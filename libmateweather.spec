%define url_ver %(echo %{version}|cut -d. -f1,2)

%define major	1
%define libname	%mklibname mateweather %{major}
%define devname	%mklibname -d mateweather

Summary:	MATE Weather applet library
Name:		libmateweather
Version:	1.8.0
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libsoup-gnome-2.4)
BuildRequires:	pkgconfig(pygtk-2.0)

%description
This is a library to provide Weather data to the MATE panel applet.

%package -n %{libname}
Summary:	MATE Weather applet library
Group:		System/Libraries

%description -n %{libname}
This is a library to provide Weather data to the MATE panel applet.

%package -n %{devname}
Summary:	MATE Weather applet library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This is a library to provide Weather data to the MATE panel applet.

%prep
%setup -q
NOCONFIGURE=yes ./autogen.sh

%build
%configure2_5x \
	--disable-static \
	--enable-python

%make 

%install
%makeinstall_std

%find_lang %{name} --with-gnome --all-name
for xmlfile in %{buildroot}%{_datadir}/%{name}/Locations.*.xml; do
	echo "%lang($(basename $xmlfile|sed -e s/Locations.// -e s/.xml//)) $(echo $xmlfile | sed s!%{buildroot}!!)" >> %{name}.lang
done

%files -f %{name}.lang
%doc AUTHORS NEWS
%{_datadir}/glib-2.0/schemas/org.mate.weather.gschema.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/locations.dtd
%{_datadir}/%{name}/Locations.xml
%{_iconsdir}/mate/*/status/weather*

%files -n %{libname}
%{_libdir}/libmateweather.so.%{major}*

%files -n %{devname}
%doc ChangeLog
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%dir %{_datadir}/gtk-doc/html/%{name}
%{_datadir}/gtk-doc/html/%{name}/*

