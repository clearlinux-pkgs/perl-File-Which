#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Which
Version  : 1.22
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/File-Which-1.22.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/File-Which-1.22.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-which-perl/libfile-which-perl_1.21-1.debian.tar.xz
Summary  : 'Perl implementation of the which utility as an API'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-Which-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
File::Which - Perl implementation of the which utility as an API
VERSION
version 1.22

%package dev
Summary: dev components for the perl-File-Which package.
Group: Development
Provides: perl-File-Which-devel = %{version}-%{release}

%description dev
dev components for the perl-File-Which package.


%package license
Summary: license components for the perl-File-Which package.
Group: Default

%description license
license components for the perl-File-Which package.


%prep
%setup -q -n File-Which-1.22
cd ..
%setup -q -T -D -n File-Which-1.22 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/File-Which-1.22/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-Which
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-File-Which/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-File-Which/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.1/File/Which.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::Which.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-Which/LICENSE
/usr/share/package-licenses/perl-File-Which/deblicense_copyright
