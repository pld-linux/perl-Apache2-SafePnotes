#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	apxs	/usr/sbin/apxs
%define	pdir	Apache2
%define	pnam	SafePnotes
%include	/usr/lib/rpm/macros.perl
Summary:	Apache2::SafePnotes - a safer replacement for Apache2::RequestUtil::pnotes
Summary(pl.UTF-8):	Apache2::SafePnotes - bezpieczniejszy zamiennik Apache2::RequestUtil::pnotes
Name:		perl-Apache2-SafePnotes
Version:	0.03
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ef1c270b94997042be2300848c0d50d3
URL:		http://search.cpan.org/dist/Apache2-SafePnotes/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-mod_perl
%endif
Requires:	perl-dirs >= 1.0-4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module cures a problem with Apache2::RequestRec::pnotes and
Apache2::Connection::pnotes (available since mod_perl 2.0.3). These
functions store perl variables making them accessible from various
phases of the Apache request cycle.

%description -l pl.UTF-8
Ten moduł usuwa problem z Apache2::RequestRec::pnotes i
Apache2::Connection::pnotes (dostępnymi w mod_perlu od wersji 2.0.3).
Funkcje te zapisują zmienne perlowe czyniąc je dostępnymi z różnych
faz cyklu żądania Apache'a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

APACHE_TEST_APXS=%{apxs} \
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Apache2/*.pm
%{_mandir}/man3/*
