%global snapshot 1

Name:           libpinyin
Version:        0.9.93
Release:        4%{?dist}
Summary:        Library to deal with pinyin

License:        GPLv2+
URL:            https://github.com/libpinyin/libpinyin
Source0:        http://downloads.sourceforge.net/libpinyin/libpinyin/%{name}-%{version}.tar.gz
%if %snapshot
Patch0:         libpinyin-0.10.x-head.patch
%endif

BuildRequires:  libdb-devel, glib2-devel
Requires:       %{name}-data%{?_isa} = %{version}-%{release}

%description
The libpinyin project aims to provide the algorithms core
for intelligent sentence-based Chinese pinyin input methods.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        data
Summary:        Data files for %{name}
Requires:       %{name} = %{version}-%{release}

%description data
The %{name}-data package contains data files.


%package        tools
Summary:        Tools for %{name}
Requires:       %{name} = %{version}-%{release}

%description tools
The %{name}-tools package contains tools.


%prep
%setup -q

%if %snapshot
%patch0 -p1 -b .head
%endif

%build
%configure --disable-static
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING README
%{_libdir}/*.so.*
%dir %{_libdir}/libpinyin

%files devel
%doc
%dir %{_includedir}/libpinyin-%{version}
%{_includedir}/libpinyin-%{version}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libpinyin.pc

%files data
%doc
%{_libdir}/libpinyin/data

%files tools
%{_bindir}/gen_binary_files
%{_bindir}/import_interpolation
%{_bindir}/gen_unigram
%{_mandir}/man1/*.1.*

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.9.93-4
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.9.93-3
- Mass rebuild 2013-12-27

* Tue Jul 30 2013 Peng Wu <pwu@redhat.com> - 0.9.93-2
- Fixes load table.conf in German locale

* Thu Jun 27 2013 Peng Wu <pwu@redhat.com> - 0.9.93-1
- Update to 0.9.93

* Sun Jun  9 2013 Peng Wu <pwu@redhat.com> - 0.9.92-1
- Update to 0.9.92

* Sun Apr 28 2013 Peng Wu <pwu@redhat.com> - 0.9.91-1
- Update to 0.9.91

* Sat Mar 23 2013 Peng Wu <pwu@redhat.com> - 0.8.93-2
- Fixes import dictionary

* Mon Mar 18 2013 Peng Wu <pwu@redhat.com> - 0.8.93-1
- Update to 0.8.93

* Fri Mar  8 2013 Peng Wu <pwu@redhat.com> - 0.8.92-1
- Update to 0.8.92

* Mon Mar  4 2013 Peng Wu <pwu@redhat.com> - 0.8.91-1
- Update to 0.8.91

* Thu Feb 28 2013 Peng Wu <pwu@redhat.com> - 0.8.1-1
- Update to 0.8.1
- Fixes pinyin_init crashes

* Mon Jan 28 2013 Peng Wu <pwu@redhat.com> - 0.8.0-3
- Fixes incomplete pinyin

* Wed Dec 12 2012 Peng Wu <pwu@redhat.com> - 0.8.0-2
- Fixes chewing input

* Wed Nov 14 2012  Peng Wu <pwu@redhat.com> - 0.8.0-1
- Update to 0.8.0

* Mon Oct 15 2012  Peng Wu <pwu@redhat.com> - 0.7.92-1
- Update to 0.7.92

* Mon Sep 17 2012  Peng Wu <pwu@redhat.com> - 0.7.91-1
- Update to 0.7.91

* Wed Aug 15 2012  Peng Wu <pwu@redhat.com> - 0.7.1-1
- Update to 0.7.1

* Fri Jul 27 2012  Peng Wu <pwu@redhat.com> - 0.7.0-1
- Update to 0.7.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012  Peng Wu <pwu@redhat.com> - 0.6.92-2
- Update libpinyin-0.7.x-head.patch

* Wed Jul 04 2012  Peng Wu <pwu@redhat.com> - 0.6.92-1
- Update to 0.6.92

* Tue Jun 12 2012  Peng Wu <pwu@redhat.com> - 0.6.0-3
- Removes provides ibus-pinyin-db

* Thu Jun 07 2012  Peng Wu <pwu@redhat.com> - 0.6.0-2
- Fixes "jv" => "ju"

* Mon May 28 2012  Peng Wu <pwu@redhat.com> - 0.6.0-1
- Update to 0.6.0

* Tue Mar 27 2012  Peng Wu <pwu@redhat.com> - 0.5.92-1
- Update to 0.5.92

* Wed Feb 15 2012  Peng Wu <pwu@redhat.com> - 0.5.91-3
- Provides ibus-pinyin-db

* Tue Feb 14 2012  Peng Wu <pwu@redhat.com> - 0.5.91-2
- Improves full pinyin parser2

* Mon Feb 13 2012  Peng Wu <pwu@redhat.com> - 0.5.91-1
- Update to 0.5.91

* Sun Jan 29 2012  Peng Wu <pwu@redhat.com> - 0.5.0-2
- Fixes pinyin parsers

* Wed Jan 18 2012  Peng Wu <pwu@redhat.com> - 0.5.0-1
- Update to 0.5.0

* Fri Jan 13 2012  Peng Wu <pwu@redhat.com> - 0.4.93-1
- Update to 0.4.93

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 29 2011  Peng Wu <pwu@redhat.com> - 0.4.92-1
- Update to 0.4.92

* Tue Dec 27 2011  Peng Wu <pwu@redhat.com> - 0.4.91-1
- Update to 0.4.91

* Fri Nov 25 2011  Peng Wu <pwu@redhat.com> - 0.3.0-2
- Increase train factor

* Fri Nov 18 2011  Peng Wu <pwu@redhat.com> - 0.3.0-1
- Update to 0.3.0

* Thu Nov 03 2011  Peng Wu <pwu@redhat.com> - 0.2.99.3-1
- Update to 0.2.99.3

* Mon Oct 31 2011  Peng Wu <pwu@redhat.com> - 0.2.99.2-5
- Fixes memory leak and save_db

* Thu Oct 27 2011  Peng Wu <pwu@redhat.com> - 0.2.99.2-4
- Update libpinyin-0.3.x-head.patch

* Thu Oct 27 2011  Peng Wu <pwu@redhat.com> - 0.2.99.2-3
- Add requires

* Thu Oct 27 2011  Peng Wu <pwu@redhat.com> - 0.2.99.2-2
- Add patch libpinyin-0.3.x-head.patch

* Tue Oct 11 2011  Peng Wu <pwu@redhat.com> - 0.2.99.2-1
- Update to 0.2.99.2

* Wed Sep 28 2011  Peng Wu <pwu@redhat.com> - 0.2.99.1-1
- Update to 0.2.99.1

* Thu Sep 08 2011  Peng Wu <pwu@redhat.com> - 0.2.99-2
- Split data sub package

* Wed Aug 31 2011  Peng Wu <alexepico@gmail.com> - 0.2.99-1
- Initial version
