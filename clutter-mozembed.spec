Name: clutter-mozembed
Summary: Clutter mozembed
Group: Applications/Internet
Version: 0.10.3
License: LGPL
URL: http://www.moblin.org
Release: %mkrel 1
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: clutter-devel
BuildRequires: libmesagl-devel
BuildRequires: libgtk+2-devel
BuildRequires: mozilla-headless-services-devel
BuildRequires: gnome-common
BuildRequires: xulrunner-headless-devel

%description
Widget to enable embedding of mozilla browser in your clutter applications
%package devel

Summary: Development libraries for %{name}
Group: Development/Libraries

Requires: %{name} = %{version}-%{release}

%description devel
Development environment for using clutter mozembed
%prep
%setup -q -n clutter-mozembed-%{version}

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
%{_bindir}/clutter-mozheadless
%exclude %{_libdir}/libcluttermozembed.la
%{_libdir}/libcluttermozembed.so.*
%{_datadir}/cluttermozembed

%files devel
%defattr(-,root,root,-)
%{_includedir}/cluttermozembed/*.h
%{_libdir}/libcluttermozembed.so
%{_libdir}/pkgconfig/cluttermozembed.pc
