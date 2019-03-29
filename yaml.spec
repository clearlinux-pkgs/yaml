#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : yaml
Version  : 0.2.1
Release  : 18
URL      : http://pyyaml.org/download/libyaml/yaml-0.2.1.tar.gz
Source0  : http://pyyaml.org/download/libyaml/yaml-0.2.1.tar.gz
Summary  : Library to parse and emit YAML
Group    : Development/Tools
License  : MIT
Requires: yaml-lib = %{version}-%{release}
Requires: yaml-license = %{version}-%{release}

%description
LibYAML - A C library for parsing and emitting YAML.
To build and install the library, run:
$ ./configure
$ make
# make install

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
%setup -q -n yaml-0.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552835306
export LDFLAGS="${LDFLAGS} -fno-lto"
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1552835306
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/yaml
cp LICENSE %{buildroot}/usr/share/package-licenses/yaml/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libyaml.so
/usr/lib64/pkgconfig/yaml-0.1.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libyaml-0.so.2
/usr/lib64/libyaml-0.so.2.0.5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/yaml/LICENSE
