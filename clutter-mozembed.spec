%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name: clutter-mozembed
Summary: Clutter mozembed
Group: Networking/WWW
Version: 0.10.3
License: LGPL
URL: http://www.moblin.org
Release: %mkrel 1
Source0: %{name}-%{version}.tar.gz
Patch0: moblin-repack.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: clutter-devel
BuildRequires: libmesagl-devel
BuildRequires: libgtk+2-devel
BuildRequires: mozilla-headless-services-devel
BuildRequires: gnome-common
BuildRequires: xulrunner-headless-devel
BuildRequires: zip

%description
Widget to enable embedding of mozilla browser in your clutter applications

%package -n %{libname}
Summary: Clutter mozembed library
Group: System/Libraries
Requires: %{name}

%description -n %{libname}
Widget to enable embedding of mozilla browser in your clutter applications

%package -n %{develname}
Summary: Development libraries for %{name}
Group: Development/Other
Requires: %{name} = %{version}-%{release}

%description -n %{develname}
Development environment for using clutter mozembed

%prep
%setup -q -n clutter-mozembed-%{version}
%patch0 -p1 -b .moblin-repack

%build
NOCONFIGURE=1 ./autogen.sh
%configure --enable-plugins --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

mkdir -p %{buildroot}/%{_datadir}/doc/%{name}-%{version}
for f in `ls %{buildroot}/%{_datadir}/doc/`; do
	if [ -f %{buildroot}/%{_datadir}/doc/$f ]; then
		mv %{buildroot}/%{_datadir}/doc/$f %{buildroot}/%{_datadir}/doc/%{name}-%{version}
	fi
done

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_libdir}/clutter-mozheadless
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.rdf
%dir %{_datadir}/%{name}/chrome
%{_datadir}/%{name}/chrome/*

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/lib%{name}-*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root,-)
%dir %{_includedir}/clutter*/%{name}
%{_includedir}/clutter*/%{name}/*.h
%{_libdir}/lib%{name}-*.so
%{_libdir}/lib%{name}-*.la
%{_libdir}/pkgconfig/%{name}-*.pc
