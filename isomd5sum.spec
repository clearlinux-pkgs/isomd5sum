#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : isomd5sum
Version  : 1.2.3
Release  : 14
URL      : https://github.com/rhinstaller/isomd5sum/archive/1.2.3.tar.gz
Source0  : https://github.com/rhinstaller/isomd5sum/archive/1.2.3.tar.gz
Summary  : Utilities for working with md5sum implanted in ISO images
Group    : Development/Tools
License  : GPL-2.0
Requires: isomd5sum-bin = %{version}-%{release}
Requires: isomd5sum-license = %{version}-%{release}
Requires: isomd5sum-man = %{version}-%{release}
Requires: isomd5sum-python = %{version}-%{release}
Requires: isomd5sum-python3 = %{version}-%{release}
BuildRequires : popt-dev
BuildRequires : python3-dev

%description
isomd5sum provides a way of making use of the ISO9660 application data
area to store md5sum data about the iso.  This allows you to check the
iso given nothing more than the iso itself.

%package bin
Summary: bin components for the isomd5sum package.
Group: Binaries
Requires: isomd5sum-license = %{version}-%{release}

%description bin
bin components for the isomd5sum package.


%package dev
Summary: dev components for the isomd5sum package.
Group: Development
Requires: isomd5sum-bin = %{version}-%{release}
Provides: isomd5sum-devel = %{version}-%{release}
Requires: isomd5sum = %{version}-%{release}

%description dev
dev components for the isomd5sum package.


%package license
Summary: license components for the isomd5sum package.
Group: Default

%description license
license components for the isomd5sum package.


%package man
Summary: man components for the isomd5sum package.
Group: Default

%description man
man components for the isomd5sum package.


%package python
Summary: python components for the isomd5sum package.
Group: Default
Requires: isomd5sum-python3 = %{version}-%{release}

%description python
python components for the isomd5sum package.


%package python3
Summary: python3 components for the isomd5sum package.
Group: Default
Requires: python3-core

%description python3
python3 components for the isomd5sum package.


%prep
%setup -q -n isomd5sum-1.2.3
cd %{_builddir}/isomd5sum-1.2.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635742984
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1635742984
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/isomd5sum
cp %{_builddir}/isomd5sum-1.2.3/COPYING %{buildroot}/usr/share/package-licenses/isomd5sum/075d599585584bb0e4b526f5c40cb6b17e0da35a
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/checkisomd5
/usr/bin/implantisomd5

%files dev
%defattr(-,root,root,-)
/usr/include/libcheckisomd5.h
/usr/include/libimplantisomd5.h
/usr/lib64/pkgconfig/isomd5sum.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/isomd5sum/075d599585584bb0e4b526f5c40cb6b17e0da35a

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/checkisomd5.1
/usr/share/man/man1/implantisomd5.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
