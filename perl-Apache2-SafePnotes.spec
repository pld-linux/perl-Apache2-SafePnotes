#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	apxs	/usr/sbin/apxs
%define	pdir	Apache2
%define	pnam	SafePnotes
Summary:	Apache2::SafePnotes - a safer replacement for Apache2::RequestUtil::pnotes
Summary(pl):	Apache2::SafePnotes - bezpieczniejszy zamiennik Apache2::RequestUtil::pnotes
Name:		perl-Apache2-SafePnotes
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ef1c270b94997042be2300848c0d50d3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-mod_perl
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module cures a problem with Apache2::RequestRec::pnotes and
Apache2::Connection::pnotes (available since mod_perl 2.0.3).
These functions store perl variables making them accessible from
various phases of the Apache request cycle.

%description -l pl
Ten modu³ usuwa problem z Apache2::RequestRec::pnotes i
Apache2::Connection::pnotes (dostêpnymi w mod_perlu od wersji 2.0.3).
Funkcje te zapisuj± zmienne perlowe czyni±c je dostêpnymi z ró¿nych
faz cyklu ¿±dania Apache'a.

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
