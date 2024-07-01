#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Which
Version  : 1.27
Release  : 30
URL      : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/File-Which-1.27.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/File-Which-1.27.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-which-perl/libfile-which-perl_1.21-1.debian.tar.xz
Summary  : 'Perl implementation of the which utility as an API'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-Which-license = %{version}-%{release}
Requires: perl-File-Which-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
File::Which - Perl implementation of the which utility as an API
VERSION
version 1.27

%package dev
Summary: dev components for the perl-File-Which package.
Group: Development
Provides: perl-File-Which-devel = %{version}-%{release}
Requires: perl-File-Which = %{version}-%{release}

%description dev
dev components for the perl-File-Which package.


%package license
Summary: license components for the perl-File-Which package.
Group: Default

%description license
license components for the perl-File-Which package.


%package perl
Summary: perl components for the perl-File-Which package.
Group: Default
Requires: perl-File-Which = %{version}-%{release}

%description perl
perl components for the perl-File-Which package.


%prep
%setup -q -n File-Which-1.27
cd %{_builddir}
tar xf %{_sourcedir}/libfile-which-perl_1.21-1.debian.tar.xz
cd %{_builddir}/File-Which-1.27
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/File-Which-1.27/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-Which
cp %{_builddir}/File-Which-1.27/LICENSE %{buildroot}/usr/share/package-licenses/perl-File-Which/9e9c2342163676b67e70ae492b987da7325f2747
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-File-Which/555d692969cc4c557c3e7a36cb224c1fde9bce68
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::Which.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-Which/555d692969cc4c557c3e7a36cb224c1fde9bce68
/usr/share/package-licenses/perl-File-Which/9e9c2342163676b67e70ae492b987da7325f2747

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
