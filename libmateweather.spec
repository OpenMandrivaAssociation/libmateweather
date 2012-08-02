%define major	1
%define libname	%mklibname mateweather %{major}
%define devname	%mklibname -d mateweather

Summary:	MATE Weather applet library
Name:		libmateweather
Version:	1.4.0
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	pkgconfig(mateconf-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libsoup-gnome-2.4)

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

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static \

%make 

%install
%makeinstall_std
%find_lang %{name}

for xmlfile in %{buildroot}%{_datadir}/%{name}/Locations.*.xml; do
	echo "%lang($(basename $xmlfile|sed -e s/Locations.// -e s/.xml//)) $(echo $xmlfile | sed s!%{buildroot}!!)" >> %{name}.lang
done

%files -f %{name}.lang
%doc AUTHORS NEWS
%{_sysconfdir}/mateconf/schemas/mateweather.schemas
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

