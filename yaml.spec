#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : yaml
Version  : 0.2.5
Release  : 26
URL      : https://pyyaml.org/download/libyaml/yaml-0.2.5.tar.gz
Source0  : https://pyyaml.org/download/libyaml/yaml-0.2.5.tar.gz
Summary  : Library to parse and emit YAML
Group    : Development/Tools
License  : MIT
Requires: yaml-lib = %{version}-%{release}
Requires: yaml-license = %{version}-%{release}

%description
## LibYAML - A C library for parsing and emitting YAML.
To build and install the library, run:

%package dev
Summary: dev components for the yaml package.
Group: Development
Requires: yaml-lib = %{version}-%{release}
Provides: yaml-devel = %{version}-%{release}
Requires: yaml = %{version}-%{release}

%description dev
dev components for the yaml package.


%package lib
Summary: lib components for the yaml package.
Group: Libraries
Requires: yaml-license = %{version}-%{release}

%description lib
lib components for the yaml package.


%package license
Summary: license components for the yaml package.
Group: Default

%description license
license components for the yaml package.


%prep
%setup -q -n yaml-0.2.5
cd %{_builddir}/yaml-0.2.5
pushd ..
cp -a yaml-0.2.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656342346
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1656342346
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/yaml
cp %{_builddir}/yaml-0.2.5/License %{buildroot}/usr/share/package-licenses/yaml/e99e74d048726c39136dc992f1fb5998972e3b4e
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/yaml.h
/usr/lib64/glibc-hwcaps/x86-64-v3/libyaml.so
/usr/lib64/libyaml.so
/usr/lib64/pkgconfig/yaml-0.1.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libyaml-0.so.2
/usr/lib64/glibc-hwcaps/x86-64-v3/libyaml-0.so.2.0.9
/usr/lib64/libyaml-0.so.2
/usr/lib64/libyaml-0.so.2.0.9

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/yaml/e99e74d048726c39136dc992f1fb5998972e3b4e
