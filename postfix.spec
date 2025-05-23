#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v25
# autospec commit: 9594167
#
Name     : postfix
Version  : 3.10.2
Release  : 45
URL      : https://archive.mgm51.com/mirrors/postfix-source/official/postfix-3.10.2.tar.gz
Source0  : https://archive.mgm51.com/mirrors/postfix-source/official/postfix-3.10.2.tar.gz
Source1  : postfix.service
Source2  : postfix.tmpfiles
Summary  : Mail transfer agent (MTA) that routes and delivers electronic mail. SMTP server.
Group    : Development/Tools
License  : BSD-4-Clause EPL-1.0 EPL-2.0 GPL-2.0 IPL-1.0
Requires: postfix-bin = %{version}-%{release}
Requires: postfix-config = %{version}-%{release}
Requires: postfix-data = %{version}-%{release}
Requires: postfix-lib = %{version}-%{release}
Requires: postfix-libexec = %{version}-%{release}
Requires: postfix-license = %{version}-%{release}
Requires: postfix-man = %{version}-%{release}
Requires: postfix-services = %{version}-%{release}
BuildRequires : db-dev
BuildRequires : mariadb-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(libnsl)
BuildRequires : pkgconfig(libpcre)
BuildRequires : pkgconfig(libsasl2)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : postgresql-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Purpose of this document
========================
This document describes how to add your own SASL implementation to
Postfix.  You don't have to provide both the server and client side.
You can provide just one and omit the other. The examples below
assume you do both.

%package bin
Summary: bin components for the postfix package.
Group: Binaries
Requires: postfix-data = %{version}-%{release}
Requires: postfix-libexec = %{version}-%{release}
Requires: postfix-config = %{version}-%{release}
Requires: postfix-license = %{version}-%{release}
Requires: postfix-services = %{version}-%{release}

%description bin
bin components for the postfix package.


%package config
Summary: config components for the postfix package.
Group: Default

%description config
config components for the postfix package.


%package data
Summary: data components for the postfix package.
Group: Data

%description data
data components for the postfix package.


%package doc
Summary: doc components for the postfix package.
Group: Documentation
Requires: postfix-man = %{version}-%{release}

%description doc
doc components for the postfix package.


%package lib
Summary: lib components for the postfix package.
Group: Libraries
Requires: postfix-data = %{version}-%{release}
Requires: postfix-libexec = %{version}-%{release}
Requires: postfix-license = %{version}-%{release}

%description lib
lib components for the postfix package.


%package libexec
Summary: libexec components for the postfix package.
Group: Default
Requires: postfix-config = %{version}-%{release}
Requires: postfix-license = %{version}-%{release}

%description libexec
libexec components for the postfix package.


%package license
Summary: license components for the postfix package.
Group: Default

%description license
license components for the postfix package.


%package man
Summary: man components for the postfix package.
Group: Default

%description man
man components for the postfix package.


%package services
Summary: services components for the postfix package.
Group: Systemd services
Requires: systemd

%description services
services components for the postfix package.


%prep
%setup -q -n postfix-3.10.2
cd %{_builddir}/postfix-3.10.2
pushd ..
cp -a postfix-3.10.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1745421412
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make  %{?_smp_mflags}  CCARGS=" \
-DUSE_TLS \
-DUSE_SASL_AUTH -DUSE_CYRUS_SASL -I/usr/include/sasl \
`pkg-config --cflags openssl` \
-DHAS_MYSQL -I/usr/include/mysql \
-DHAS_PGSQL -I/usr/include/postgresql \
-DHAS_SQLITE \
-DHAS_PCRE -I/usr/include/pcre \
-DDEF_PID_DIR=\\\"/run/postfix\\\" \
" \
AUXLIBS=" \
`pkg-config --libs openssl` \
-lsasl2 \
-lmysqlclient \
-lpq \
-lsqlite3 \
-lpcre \
" \
shared=yes \
dynamicmaps=yes

pushd ../buildavx2
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
make  %{?_smp_mflags}  CCARGS=" \
-DUSE_TLS \
-DUSE_SASL_AUTH -DUSE_CYRUS_SASL -I/usr/include/sasl \
`pkg-config --cflags openssl` \
-DHAS_MYSQL -I/usr/include/mysql \
-DHAS_PGSQL -I/usr/include/postgresql \
-DHAS_SQLITE \
-DHAS_PCRE -I/usr/include/pcre \
-DDEF_PID_DIR=\\\"/run/postfix\\\" \
" \
AUXLIBS=" \
`pkg-config --libs openssl` \
-lsasl2 \
-lmysqlclient \
-lpq \
-lsqlite3 \
-lpcre \
" \
shared=yes \
dynamicmaps=yes
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1745421412
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/postfix
cp %{_builddir}/postfix-%{version}/COPYRIGHT %{buildroot}/usr/share/package-licenses/postfix/51ed8894ca9a43ac82b3e637508197c3a1f6de30 || :
cp %{_builddir}/postfix-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/postfix/0f78113e577104ec27d59b2b02c0d595c62ae6b4 || :
cp %{_builddir}/postfix-%{version}/conf/LICENSE %{buildroot}/usr/share/package-licenses/postfix/0f78113e577104ec27d59b2b02c0d595c62ae6b4 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
make non-interactive-package install_root=%{buildroot} manpage_directory=/usr/share/man_v3
popd
GOAMD64=v2
make non-interactive-package install_root=%{buildroot} manpage_directory=/usr/share/man
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/postfix.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/tmpfiles.d/postfix.conf
## install_append content
mkdir -p %{buildroot}/usr/bin
mv %{buildroot}/usr/sbin/sendmail %{buildroot}/usr/bin/sendmail-postfix
mkdir -p %{buildroot}/usr/share/doc/postfix/defconfig
cp -v conf/* %{buildroot}/usr/share/doc/postfix/defconfig/
mv %{buildroot}/usr/sbin/* %{buildroot}/usr/bin/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%attr(2755,root,postdrop) /usr/bin/postdrop
%attr(2755,root,postdrop) /usr/bin/postqueue
/usr/bin/mailq
/usr/bin/newaliases
/usr/bin/postalias
/usr/bin/postcat
/usr/bin/postconf
/usr/bin/postfix
/usr/bin/postkick
/usr/bin/postlock
/usr/bin/postlog
/usr/bin/postmap
/usr/bin/postmulti
/usr/bin/postsuper
/usr/bin/sendmail-postfix

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/postfix.conf

%files data
%defattr(-,root,root,-)
/usr/share/man_v3/man1/mailq.1
/usr/share/man_v3/man1/newaliases.1
/usr/share/man_v3/man1/postalias.1
/usr/share/man_v3/man1/postcat.1
/usr/share/man_v3/man1/postconf.1
/usr/share/man_v3/man1/postdrop.1
/usr/share/man_v3/man1/postfix-tls.1
/usr/share/man_v3/man1/postfix.1
/usr/share/man_v3/man1/postkick.1
/usr/share/man_v3/man1/postlock.1
/usr/share/man_v3/man1/postlog.1
/usr/share/man_v3/man1/postmap.1
/usr/share/man_v3/man1/postmulti.1
/usr/share/man_v3/man1/postqueue.1
/usr/share/man_v3/man1/postsuper.1
/usr/share/man_v3/man1/sendmail.1
/usr/share/man_v3/man5/access.5
/usr/share/man_v3/man5/aliases.5
/usr/share/man_v3/man5/body_checks.5
/usr/share/man_v3/man5/bounce.5
/usr/share/man_v3/man5/canonical.5
/usr/share/man_v3/man5/cidr_table.5
/usr/share/man_v3/man5/generic.5
/usr/share/man_v3/man5/header_checks.5
/usr/share/man_v3/man5/ldap_table.5
/usr/share/man_v3/man5/lmdb_table.5
/usr/share/man_v3/man5/master.5
/usr/share/man_v3/man5/memcache_table.5
/usr/share/man_v3/man5/mongodb_table.5
/usr/share/man_v3/man5/mysql_table.5
/usr/share/man_v3/man5/nisplus_table.5
/usr/share/man_v3/man5/pcre_table.5
/usr/share/man_v3/man5/pgsql_table.5
/usr/share/man_v3/man5/postconf.5
/usr/share/man_v3/man5/postfix-wrapper.5
/usr/share/man_v3/man5/regexp_table.5
/usr/share/man_v3/man5/relocated.5
/usr/share/man_v3/man5/socketmap_table.5
/usr/share/man_v3/man5/sqlite_table.5
/usr/share/man_v3/man5/tcp_table.5
/usr/share/man_v3/man5/transport.5
/usr/share/man_v3/man5/virtual.5
/usr/share/man_v3/man8/anvil.8
/usr/share/man_v3/man8/bounce.8
/usr/share/man_v3/man8/cleanup.8
/usr/share/man_v3/man8/defer.8
/usr/share/man_v3/man8/discard.8
/usr/share/man_v3/man8/dnsblog.8
/usr/share/man_v3/man8/error.8
/usr/share/man_v3/man8/flush.8
/usr/share/man_v3/man8/lmtp.8
/usr/share/man_v3/man8/local.8
/usr/share/man_v3/man8/master.8
/usr/share/man_v3/man8/oqmgr.8
/usr/share/man_v3/man8/pickup.8
/usr/share/man_v3/man8/pipe.8
/usr/share/man_v3/man8/postlogd.8
/usr/share/man_v3/man8/postscreen.8
/usr/share/man_v3/man8/proxymap.8
/usr/share/man_v3/man8/qmgr.8
/usr/share/man_v3/man8/qmqpd.8
/usr/share/man_v3/man8/scache.8
/usr/share/man_v3/man8/showq.8
/usr/share/man_v3/man8/smtp.8
/usr/share/man_v3/man8/smtpd.8
/usr/share/man_v3/man8/spawn.8
/usr/share/man_v3/man8/tlsmgr.8
/usr/share/man_v3/man8/tlsproxy.8
/usr/share/man_v3/man8/trace.8
/usr/share/man_v3/man8/trivial-rewrite.8
/usr/share/man_v3/man8/verify.8
/usr/share/man_v3/man8/virtual.8

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/postfix/*

%files lib
%defattr(-,root,root,-)
/usr/lib/postfix/libpostfix-dns.so
/usr/lib/postfix/libpostfix-global.so
/usr/lib/postfix/libpostfix-master.so
/usr/lib/postfix/libpostfix-tls.so
/usr/lib/postfix/libpostfix-util.so
/usr/lib/postfix/postfix-mysql.so
/usr/lib/postfix/postfix-pcre.so
/usr/lib/postfix/postfix-pgsql.so
/usr/lib/postfix/postfix-sqlite.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/postfix/anvil
/usr/libexec/postfix/bounce
/usr/libexec/postfix/cleanup
/usr/libexec/postfix/discard
/usr/libexec/postfix/dnsblog
/usr/libexec/postfix/error
/usr/libexec/postfix/flush
/usr/libexec/postfix/lmtp
/usr/libexec/postfix/local
/usr/libexec/postfix/master
/usr/libexec/postfix/nqmgr
/usr/libexec/postfix/oqmgr
/usr/libexec/postfix/pickup
/usr/libexec/postfix/pipe
/usr/libexec/postfix/post-install
/usr/libexec/postfix/postfix-script
/usr/libexec/postfix/postfix-tls-script
/usr/libexec/postfix/postfix-wrapper
/usr/libexec/postfix/postlogd
/usr/libexec/postfix/postmulti-script
/usr/libexec/postfix/postscreen
/usr/libexec/postfix/proxymap
/usr/libexec/postfix/qmgr
/usr/libexec/postfix/qmqpd
/usr/libexec/postfix/scache
/usr/libexec/postfix/showq
/usr/libexec/postfix/smtp
/usr/libexec/postfix/smtpd
/usr/libexec/postfix/spawn
/usr/libexec/postfix/tlsmgr
/usr/libexec/postfix/tlsproxy
/usr/libexec/postfix/trivial-rewrite
/usr/libexec/postfix/verify
/usr/libexec/postfix/virtual

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/postfix/0f78113e577104ec27d59b2b02c0d595c62ae6b4
/usr/share/package-licenses/postfix/51ed8894ca9a43ac82b3e637508197c3a1f6de30

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mailq.1
/usr/share/man/man1/newaliases.1
/usr/share/man/man1/postalias.1
/usr/share/man/man1/postcat.1
/usr/share/man/man1/postconf.1
/usr/share/man/man1/postdrop.1
/usr/share/man/man1/postfix-tls.1
/usr/share/man/man1/postfix.1
/usr/share/man/man1/postkick.1
/usr/share/man/man1/postlock.1
/usr/share/man/man1/postlog.1
/usr/share/man/man1/postmap.1
/usr/share/man/man1/postmulti.1
/usr/share/man/man1/postqueue.1
/usr/share/man/man1/postsuper.1
/usr/share/man/man1/sendmail.1
/usr/share/man/man5/access.5
/usr/share/man/man5/aliases.5
/usr/share/man/man5/body_checks.5
/usr/share/man/man5/bounce.5
/usr/share/man/man5/canonical.5
/usr/share/man/man5/cidr_table.5
/usr/share/man/man5/generic.5
/usr/share/man/man5/header_checks.5
/usr/share/man/man5/ldap_table.5
/usr/share/man/man5/lmdb_table.5
/usr/share/man/man5/master.5
/usr/share/man/man5/memcache_table.5
/usr/share/man/man5/mongodb_table.5
/usr/share/man/man5/mysql_table.5
/usr/share/man/man5/nisplus_table.5
/usr/share/man/man5/pcre_table.5
/usr/share/man/man5/pgsql_table.5
/usr/share/man/man5/postconf.5
/usr/share/man/man5/postfix-wrapper.5
/usr/share/man/man5/regexp_table.5
/usr/share/man/man5/relocated.5
/usr/share/man/man5/socketmap_table.5
/usr/share/man/man5/sqlite_table.5
/usr/share/man/man5/tcp_table.5
/usr/share/man/man5/transport.5
/usr/share/man/man5/virtual.5
/usr/share/man/man8/anvil.8
/usr/share/man/man8/bounce.8
/usr/share/man/man8/cleanup.8
/usr/share/man/man8/defer.8
/usr/share/man/man8/discard.8
/usr/share/man/man8/dnsblog.8
/usr/share/man/man8/error.8
/usr/share/man/man8/flush.8
/usr/share/man/man8/lmtp.8
/usr/share/man/man8/local.8
/usr/share/man/man8/master.8
/usr/share/man/man8/oqmgr.8
/usr/share/man/man8/pickup.8
/usr/share/man/man8/pipe.8
/usr/share/man/man8/postlogd.8
/usr/share/man/man8/postscreen.8
/usr/share/man/man8/proxymap.8
/usr/share/man/man8/qmgr.8
/usr/share/man/man8/qmqpd.8
/usr/share/man/man8/scache.8
/usr/share/man/man8/showq.8
/usr/share/man/man8/smtp.8
/usr/share/man/man8/smtpd.8
/usr/share/man/man8/spawn.8
/usr/share/man/man8/tlsmgr.8
/usr/share/man/man8/tlsproxy.8
/usr/share/man/man8/trace.8
/usr/share/man/man8/trivial-rewrite.8
/usr/share/man/man8/verify.8
/usr/share/man/man8/virtual.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/postfix.service
