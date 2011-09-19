Summary:          C++ API for the cairo graphics library
Name:             cairomm
Version:          1.8.0
Release:          2.1%{?dist}
URL:              http://www.cairographics.org
License:          LGPLv2+
Group:            System Environment/Libraries
Source:           http://www.cairographics.org/releases/%{name}-%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:    cairo-devel >= 1.5.10 pkgconfig
BuildRequires:    libsigc++20-devel

%description
Cairomm is the C++ API for the cairo graphics library. It offers all the power
of cairo with an interface familiar to C++ developers, including use of the 
Standard Template Library where it makes sense.

%package        devel
Summary:        Headers for developing programs that will use %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       cairo-devel >= 1.4.0 pkgconfig
Requires:       libsigc++20-devel

%description    devel
Cairomm is the C++ API for the cairo graphics library. It offers all the power
of cairo with an interface familiar to C++ developers, including use of the 
Standard Template Library where it makes sense.

This package contains the libraries and header files needed for
developing %{name} applications.

%prep
%setup -q 

%build
%configure --enable-static=no --enable-docs=no
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README NEWS
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/cairomm-1.0/
%doc ChangeLog docs/reference

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.8.0-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 1.8.0-1
- Update to 1.8.0
- Added libsigc++20-devel dependency

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Denis Leroy <denis@poolshark.org> - 1.6.2-1
- Update to upstream 1.6.2
- atsui patch upstreamed

* Sun Mar 23 2008 Denis Leroy <denis@poolshark.org> - 1.5.0-1
- Update to 1.5.0
- Added patch from Mamoru Tasaka to fix font type enum (#438600)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4.4-2
- Autorebuild for GCC 4.3

* Fri Aug 17 2007 Denis Leroy <denis@poolshark.org> - 1.4.4-1
- Update to upstream version 1.4.4
- Fixed License tag

* Fri Jul 20 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 1.4.2-1
- New upstream release
- Changed install to preserve timestamps
- Removed mv of docs/reference and include files directly

* Wed Jan 17 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 1.2.4-1
- New release

* Sat Oct 14 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 1.2.2-1
- New upstream release

* Sun Aug 27 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 1.2.0-4
- Bumped release for make tag

* Sun Aug 27 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 1.2.0-3
- Bumped release for mass rebuild

* Sun Aug 20 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 1.2.0-2
- Bumped release for make tag

* Sun Aug 20 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 1.2.0-1
- New upstream release
- Updated summary and description

* Thu Aug  3 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 1.1.10-1
- First release for cairo 1.2
- Adjusted cairo dependencies for new version
- Docs were in html, moved to reference/html

* Sun Apr  9 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.6.0-1
- New upstream version should fix the upstream issues like AUTHORS and README
- Added pkgconfig to cairomm BuildRequires and cairomm-devel Requires
- Replaced makeinstall
- Fixed devel package description
- Modified includedir syntax
- docs included via the mv in install and in the devel files as html dir

* Sun Mar  5 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.5.0-10
- Removed duplicate Group tag in devel
- Disabled docs till they're fixed upstream 

* Sun Mar  5 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.5.0-9
- Removed requires since BuildRequires is present
- Cleaned up Source tag

* Fri Feb 24 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.5.0-7
- Fixed URL and SOURCE tags
- Fixed header include directory

* Fri Feb 24 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.5.0-6
- Fixed URL tag

* Wed Feb 22 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.5.0-5
- Remove epoch 'leftovers'

* Wed Feb 22 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.5.0-4
- Cleanup for FE

* Wed Feb 22 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.5.0-3
- Added pre-release alphatag

* Wed Feb 22 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.5.0-2
- Updated to current cairomm CVS
- Added documentation to devel package

* Fri Feb 03 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.5.0-1
- Updated to current cairomm CVS

* Fri Jan 27 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.4.0-1
- Initial creation from papyrus.spec.in

