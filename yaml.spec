#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : yaml
Version  : 0.1.7
Release  : 12
URL      : http://pyyaml.org/download/libyaml/yaml-0.1.7.tar.gz
Source0  : http://pyyaml.org/download/libyaml/yaml-0.1.7.tar.gz
Summary  : Library to parse and emit YAML
Group    : Development/Tools
License  : MIT
Requires: yaml-lib

%description
LibYAML - A C library for parsing and emitting YAML.
To build and install the library, run:
$ ./configure
$ make
# make install

%package dev
Summary: dev components for the yaml package.
Group: Development
Requires: yaml-lib
Provides: yaml-devel

%description dev
dev components for the yaml package.


%package lib
Summary: lib components for the yaml package.
Group: Libraries

%description lib
lib components for the yaml package.


%prep
%setup -q -n yaml-0.1.7

%build
export LANG=C
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -fno-semantic-interposition -falign-functions=32 -O3 "
export FCFLAGS="$CFLAGS -fno-semantic-interposition -falign-functions=32 -O3 "
export FFLAGS="$CFLAGS -fno-semantic-interposition -falign-functions=32 -O3 "
export CXXFLAGS="$CXXFLAGS -fno-semantic-interposition -falign-functions=32 -O3 "
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
